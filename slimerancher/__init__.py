import typing
import os, json
from .Items import item_table, SlimeItem
from .Locations import location_table, SlimeLocation
from .Options import SlimeOptions
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Item, ItemClassification, Tutorial
from ..AutoWorld import World, WebWorld

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


class V6World(World):
    """ 
    Slime Rancher: wrangle slimes and explore the far far range.
    """ 

    game: str = "Slime rancher"
    topology_present = False
    web = SlimeWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 1

    area_connections: typing.Dict[int, int]
    area_cost_map: typing.Dict[int,int]

    music_map: typing.Dict[int,int]

    options_dataclass = SlimeOptions

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    def create_item(self, name: str, itemtype: ItemClassification) -> Item:
        return SlimeItem(name, ItemClassification.progression, item_table[name], self.player)

    def create_items(self):
        trinkets = [self.create_item("Trinket " + str(i+1).zfill(2)) for i in range(0,20)]
        self.multiworld.itempool += trinkets

    def generate_basic(self):
        musiclist_o = [1,2,3,4,9,12]
        musiclist_s = musiclist_o.copy()
        if self.options.music_rando:
            self.multiworld.random.shuffle(musiclist_s)
        self.music_map = dict(zip(musiclist_o, musiclist_s))

    def fill_slot_data(self):
        return {
            "MusicRando": self.music_map,
            "AreaRando": self.area_connections,
            "DoorCost": self.options.door_cost.value,
            "AreaCostRando": self.area_cost_map,
            "DeathLink": self.options.death_link.value,
            "DeathLink_Amnesty": self.options.death_link_amnesty.value
        }
