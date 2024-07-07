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
    "Courtyard Gate Activation": ("Courtyard", [])
}

start = 100

location_name_to_id = {n: x + start for n, x in enumerate(location_table.keys())}