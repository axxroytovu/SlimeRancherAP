import typing
from ..generic.Rules import add_rule
from .Regions import region_table
from .Locations import location_table, events_table
import logging

def parse_rules(rule, combiner='and'):
    if isinstance(rule, list):
        subrules = [parse_rules(r) for r in rule]
        if combiner=='and':
            return lambda state, player: all(r(state, player) for r in subrules)
        elif combiner=='or':
            return lambda state, player: any(r(state, player) for r in subrules)
        else:
            logging.error("Improperly formatted access logic")
            raise ValueError("Improperly formatted access logic")
    elif isinstance(rule, str):
        logging.info(f"needs item {rule}")
        return lambda state, player, itm=rule: state.has(itm, player)
    elif isinstance(rule, tuple):
        if isinstance(rule[0], str) and isinstance(rule[1], int):
            return lambda state, player, itm=rule[0], cnt=rule[1]: state.has(itm, player, cnt)
        else:
            logging.error("Improperly formatted access logic")
            raise ValueError("Improperly formatted access logic")
    elif isinstance(rule, dict):
        if 'rule' in rule and 'combiner' in rule:
            return parse_rules(**rule)
        else:
            logging.error("Improperly formatted access logic")
            raise ValueError("Improperly formatted access logic")
    else:
        logging.error("Improperly formatted access logic")
        raise ValueError("Improperly formatted access logic")

def set_rules(multiworld, options, player):
    for region_name, connections in region_table.items():
        region_obj = multiworld.get_region(region_name, player)
        for connection, rule in connections.items():
            logging.info(f"Creating logic for {region_name} - {connection} connection")
            target_region = multiworld.get_region(connection, player)
            if rule: 
                final_function = parse_rules(rule)
                region_obj.connect(connecting_region=target_region,
                                   rule=lambda state, player=player, func=final_function: func(state, player))
            else:
                region_obj.connect(connecting_region=target_region)

    for location in multiworld.get_locations(player):
        logging.info(f"Creating logic for {location.name} location")
        if location.name in location_table:
            rule = location_table[location.name][1]
        elif location.name in events_table:
            rule = events_table[location.name][1]
        else:
            logging.error(f"Could not find location {location.name}")
            raise KeyError(f"Could not find location {location.name}")
        if rule:
            final_function = parse_rules(rule)
            add_rule(location, lambda state, player=player, func=final_function: func(state, player))

    multiworld.completion_condition[player] = lambda state: state.has("Hobson Final", player)
