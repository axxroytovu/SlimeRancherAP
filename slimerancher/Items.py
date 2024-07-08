from BaseClasses import Item, ItemClassification

class SlimeItem(Item):
    game: str = "Slime rancher"

item_table = {
    # Door Keys
    "Indigo Quarry Entry Door": (ItemClassification.progression, 1),
    "Moss Blanket Entry Door": (ItemClassification.progression, 1),
    "The Beach Door": (ItemClassification.progression, 1),
    "Courtyard from Moss Blanket Door": (ItemClassification.progression, 1),
    "Courtyard from Indigo Quarry Door": (ItemClassification.progression, 1),
    "Ancient Ruins Entry Door": (ItemClassification.progression, 1),
    "Warp Area Entry Door": (ItemClassification.progression, 1),
    "Glass Desert Eastern Door": (ItemClassification.progression, 1),
    "Glass Desert Western Door": (ItemClassification.progression, 1),
    "Ring Island Vault Door": (ItemClassification.progression, 1),
    "Feral Path Vault Door": (ItemClassification.progression, 1),
    "Ash Isle Vault Door": (ItemClassification.progression, 1),
    # Ranch Upgrades
    "Grotto Expansion": (ItemClassification.progression, 1),
    "Overgrowth Expansion": (ItemClassification.progression, 1),
    "Lab Expansion": (ItemClassification.progression, 1),
    "Docks Expansion": (ItemClassification.progression, 1),
    # Teleporter Activations
    "Glass Desert Teleporter": (ItemClassification.progression, 1),
    "Dry Reef Teleporter": (ItemClassification.progression, 1),
    "Ring Island Teleporter": (ItemClassification.progression, 1),
    "Indigo Quarry Teleporter": (ItemClassification.progression, 1),
    "Moustache Island Teleporter": (ItemClassification.progression, 1),
    "Ash Isle Teleporter": (ItemClassification.progression, 1),
    "Water Tank Upgrade": (ItemClassification.useful, 1),
    "Progressive Jetpack Upgrade": (ItemClassification.progression, 2),
    "Progressive Dash Upgrade": (ItemClassification.useful, 2),
    "Pulse Wave Upgrade": (ItemClassification.useful, 1),
    "Progressive Heart Module": (ItemClassification.useful, 4),
    "Progressive Power Core": (ItemClassification.useful, 3),
    "Progressive Tank Booster": (ItemClassification.useful, 4),
    "Progressive Treasure Cracker": (ItemClassification.progression, 3),
    # Everything Else
    "Garbage": (ItemClassification.filler, 0)
}

offset = int.from_bytes("slime".encode('utf-8'))

item_name_to_id = {itm: idx + offset for idx, itm in enumerate(item_table.keys())}