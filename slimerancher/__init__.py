import typing
import os, json
from .Items import item_table, item_name_to_id, SlimeItem
from .Locations import location_table, events_table, location_name_to_id, SlimeLocation
from .Options import SlimeOptions
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Item, ItemClassification, Tutorial
from ..AutoWorld import World, WebWorld
from Utils import visualize_regions

client_version = 1


class SlimeWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Slime Rancher for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Axxroy"]
    )]


class SlimeWorld(World):
    """ 
    Slime Rancher: wrangle slimes and explore the far far range.
    """ 

    game: str = "Slime rancher"
    topology_present = False
    web = SlimeWeb()

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    data_version = 1

    options_dataclass = SlimeOptions

    def get_filler_item_name():
        return "Garbage"

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    def create_item(self, name: str, itemtype: ItemClassification) -> Item:
        return SlimeItem(name, itemtype, self.item_name_to_id.get(name, None), self.player)

    def create_items(self):
        items = []
        for itm_name, info in item_table.items():
            for _ in range(info[1]):
                items.append(self.create_item(itm_name, info[0]))

        for location in self.multiworld.get_unfilled_locations(self.player):
            if location.name in events_table:
                event_item = self.create_item(location.name, ItemClassification.progression)
                location.place_locked_item(event_item)

        needed_items = len(self.multiworld.get_unfilled_locations(self.player))
        while len(items) < needed_items:
            items.append(self.create_filler())
        self.multiworld.itempool += items

    def generate_basic(self):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.game}_{self.player}.puml")

    def fill_slot_data(self):
        return {
            "DeathLink": self.options.death_link.value
        }
