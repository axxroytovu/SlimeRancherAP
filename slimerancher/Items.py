from BaseClasses import Item, ItemClassification

class SlimeItem(Item):
    game: str = "Slime rancher"

item_table = {
    # Door Keys
    "Indigo Quarry Entry Door": ItemClassification.progression,
    "Moss Blanket Entry Door": ItemClassification.progression,
    "The Beach Door": ItemClassification.progression,
    "Courtyard from Moss Blanket Door": ItemClassification.progression,
    "Courtyard from Indigo Quarry Door": ItemClassification.progression,
    "Ancient Ruins Entry Door": ItemClassification.progression,
    "Warp Area Entry Door": ItemClassification.progression,
    "Glass Desert Eastern Door": ItemClassification.progression,
    "Glass Desert Western Door": ItemClassification.progression,
    "Ring Island Vault Door": ItemClassification.progression,
    "Feral Path Vault Door": ItemClassification.progression,
    "Ash Isle Vault Door": ItemClassification.progression,
    # Ranch Upgrades
    "Grotto Expansion": ItemClassification.progression,
    "Overgrowth Expansion": ItemClassification.progression,
    "Lab Expansion": ItemClassification.progression,
    "Docks Expansion": ItemClassification.progression,
    # Teleporter Activations
    "Glass Desert Teleporter": ItemClassification.progression,
    "Dry Reef Teleporter": ItemClassification.progression,
    "Ring Island Teleporter": ItemClassification.progression,
    "Indigo Quarry Teleporter": ItemClassification.progression,
    "Moustache Island Teleporter": ItemClassification.progression,
    "Ash Isle Teleporter": ItemClassification.progression,
    # Everything Else
    "Garbage": ItemClassification.filler
}