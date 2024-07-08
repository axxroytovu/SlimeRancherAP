from BaseClasses import Location

class SlimeLocation(Location):
    game: str = "Slime Rancher"

location_table = {
    # Gordos
    "Reef Pink Gordo": ("DryDryReef", []),
    "Phosphor Gordo": ("DryDryReef", []),
    "Reef Tabby Gordo": ("DryDryReef", []),
    "Beach Tabby Gordo": ("TheBeach", []),
    "Island Pink Gordo": ("RingIsland", []),
    "Cave Rock Gordo": ("IndigoQuarry", []),
    "Rad Gordo": ("IndigoQuarry", []),
    "Island Rock Gordo": ("IndigoQuarry", []),
    "Crystal Gordo": ("AshIsle", []),
    "Honey Gordo": ("MossBlanket", []),
    "Hunter Gordo": ("MossBlanket", []),
    "Boom Gordo": ("AncientRuins", []),
    "Quantum Gordo": ("AncientRuins", []),
    "Dervish Gordo": ("GlassDesert", []),
    "Tangle Gordo": ("GlassDesert", []),
    "Mosaic Gordo": ("GlassDesert4", []),
    # Plort Achievements
    "Ancient Ruins Warp Activation": ("WarpArea", []),
    "Courtyard Gate Activation": ("Courtyard", []),
    # VacPack Upgrades
    "Water Tank Upgrade": ("TheRanch", []),
    "Jetpack Upgrade": ("TheRanch", []),
    "Air Drive Upgrade": ("TheRanch", []),
    "Dash Boots Upgrade": ("TheRanch", []),
    "Ultra Dash Boots Upgrade": ("TheRanch", []),
    "Pulse Wave Upgrade": ("TheRanch", []),
    "Heart Module Upgrade": ("TheRanch", []),
    "Heart Module Mk2 Upgrade": ("TheRanch", []),
    "Heart Module Mk3 Upgrade": ("TheRanch", []),
    "Heart Module Ultra Upgrade": ("TheRanch", []),
    "Power Core Upgrade": ("TheRanch", []),
    "Power Core Mk2 Upgrade": ("TheRanch", []),
    "Power Core Mk3 Upgrade": ("TheRanch", []),
    "Tank Booster Upgrade": ("TheRanch", []),
    "Tank Booster Mk2 Upgrade": ("TheRanch", []),
    "Tank Booster Mk3 Upgrade": ("TheRanch", []),
    "Tank Booster Ultra Upgrade": ("TheRanch", []),
    "Treasure Cracker Upgrade": ("TheLab", []),
    "Treasure Cracker Mk2 Upgrade": ("TheLab", []),
    "Treasure Cracker Mk3 Upgrade": ("TheLab", []),
    "Golden Sureshot": ("TheRanch", []),
    # Ranch Expansions
    "The Grotto": ("TheRanch", []),
    "The Lab": ("TheRanch", []),
    "The Docks": ("TheOvergrowth", []),
    "The Overgrowth": ("TheRanch", [])
}

events_table = {
    "Hobson Final": ("GlassDesert2", [])
}

offset = int.from_bytes("slime".encode('utf-8'))

location_name_to_id = {loc: idx + offset for idx, loc in enumerate(location_table.keys())}
