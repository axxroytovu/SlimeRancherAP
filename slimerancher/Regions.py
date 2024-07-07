import typing
from BaseClasses import MultiWorld, Region
from .Locations import SlimeLocation, location_table, location_name_to_id

region_table = {
    "Menu": {"TheRanch": []},
    "TheRanch": {
        "TheGrotto": ["Grotto Expansion"],
        "TheOvergrowth": ["Overgrowth Expansion"],
        "TheLab": ["Lab Expansion"],
        "DryDryReef": []
    },
    "TheGrotto": {
        "IndigoQuarry": ["Indigo Quarry Teleporter"]
    },
    "TheOvergrowth": {
        "TheDocks": ["Docks Expansion"],
        "TheBeach": []
    },
    "DryDryReef": {
        "TheBeach": ["The Beach Door"],
        "IndigoQuarry": ["Indigo Quarry Entry Door"],
        "MossBlanket": ["Moss Blanket Entry Door"],
        "MoustacheIsland": ["Moustache Island Teleporter"]
    },
    "TheBeach": {
        "RingIsland": ["Ring Island Teleporter"]
    },
    "RingIsland": {},
    "MoustacheIsland": {},
    "IndigoQuarry": {
        "Courtyard": ["Courtyard from Indigo Quarry Door"],
        "AshIsle": ["Ash Isle Teleporter"]
    },
    "AshIsle": {},
    "MossBlanket": {
        "Courtyard": ["Courtyard from Moss Blanket Door"]
    },
    "Courtyard": {
        "AncientRuins": ["Ancient Ruins Entry Door"]
    },
    "Ancient Ruins": {
        "WarpArea": ["Warp Area Entry Door"]
    },
    "WarpArea": {
        "GlassDesert": ["Glass Desert Teleporter"]
    },
    "GlassDesert": {
        "GlassDesert2": ["Glass Desert Eastern Door"],
        "GlassDesert3": ["Glass Desert Western Door"]
    },
    "GlassDesert2": {
        "GlassDesert4": []
    },
    "GlassDesert3": {
        "GlassDesert4": []
    },
    "GlassDesert4": {}
}


def create_regions(world: MultiWorld, player: int):
    for region_name in region_table.keys():
        region = Region(region_name, player, world)
        location_names = [k for k, v in location_table.items() if v[0] == region_name]
        region.locations += [SlimeLocation(player, loc_name, location_name_to_id[loc_name], region) for loc_name in location_names]
        world.regions.append(region)

