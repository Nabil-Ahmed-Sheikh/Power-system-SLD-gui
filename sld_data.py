source_data = [
    {"name": "Gen1 Solar", "voltage": 1.0, "x": 299, "y": 538},
    {"name": "Gen2 Wind", "voltage": 1.0, "x": 125, "y": 187},
    {"name": "Gen3 Thermal", "voltage": 1.0, "x": 437, "y": 379},
    {"name": "Gen4 Thermal", "voltage": 1.0, "x": 122, "y": 424},
    {"name": "Intertie", "voltage": 1.0, "x": 714, "y": 390},
]

bus_data = [
    {"name": "bus1", "voltage": 1.0, "x": 189, "y": 421, "angle": 0, "width": 10, "height": 60},
    {"name": "bus2", "voltage": 1.0, "x": 299, "y": 496, "angle": 0, "width": 60, "height": 10},
    {"name": "bus3", "voltage": 1.0, "x": 404, "y": 391, "angle": 0, "width": 10, "height": 60},
    {"name": "bus4", "voltage": 1.0, "x": 404, "y": 261, "angle": 0, "width": 10, "height": 60},
    {"name": "bus5", "voltage": 1.0, "x": 276, "y": 283, "angle": 0, "width": 60, "height": 10},
    {"name": "bus6", "voltage": 1.0, "x": 182, "y": 187, "angle": 0, "width": 10, "height": 60},
    {"name": "bus7", "voltage": 1.0, "x": 582, "y": 411, "angle": 0, "width": 60, "height": 10},
    {"name": "bus8", "voltage": 1.0, "x": 669, "y": 390, "angle": 0, "width": 10, "height": 60},
    {"name": "bus9", "voltage": 1.0, "x": 624, "y": 225, "angle": 0, "width": 10, "height": 60},
    {"name": "bus10", "voltage": 1.0, "x": 443, "y": 186, "angle": 0, "width": 60, "height": 10},
    {"name": "bus11", "voltage": 1.0, "x": 331, "y": 186, "angle": 0, "width": 60, "height": 10},
    {"name": "bus12", "voltage": 1.0, "x": 125, "y": 80, "angle": 0, "width": 10, "height": 60},
    {"name": "bus13", "voltage": 1.0, "x": 412, "y": 66, "angle": 0, "width": 60, "height": 10},
    {"name": "bus14", "voltage": 1.0, "x": 618, "y": 66, "angle": 0, "width": 60, "height": 10},
]

load_data = [
    {"name": "load2", "power": 100, "x": 263, "y": 536},
    {"name": "load3", "power": 100, "x": 437, "y": 438},
    {"name": "load4", "power": 100, "x": 442, "y": 295},
    {"name": "load5", "power": 100, "x": 275, "y": 234},
    {"name": "load6", "power": 100, "x": 126, "y": 252},
    {"name": "load9", "power": 100, "x": 692, "y": 225},
    {"name": "load10", "power": 100, "x": 446, "y": 139},
    {"name": "load11", "power": 100, "x": 330, "y": 139},
    {"name": "load12", "power": 100, "x": 80, "y": 80},
    {"name": "load13", "power": 100, "x": 412, "y": 25},
    {"name": "load14", "power": 100, "x": 615, "y": 25}
]

line_data = [
    {"name": "line0", "item1": "bus7", "item2": "bus8", "impedance": 0.1, "is_directed": True},
    {"name": "line1", "item1": "bus1", "item2": "bus2", "impedance": 0.1, "is_directed": True},
    {"name": "line2", "item1": "bus1", "item2": "bus5", "impedance": 0.1, "is_directed": True},
    {"name": "line3", "item1": "bus2", "item2": "bus3", "impedance": 0.1, "is_directed": True},
    {"name": "line4", "item1": "bus2", "item2": "bus4", "impedance": 0.1, "is_directed": True},
    {"name": "line5", "item1": "bus2", "item2": "bus5", "impedance": 0.1, "is_directed": True},
    {"name": "line6", "item1": "bus3", "item2": "bus4", "impedance": 0.1, "is_directed": True},
    {"name": "line7", "item1": "bus4", "item2": "bus7", "impedance": 0.1, "is_directed": True},
    {"name": "line8", "item1": "bus5", "item2": "bus4", "impedance": 0.1, "is_directed": True},
    {"name": "line9", "item1": "bus4", "item2": "bus9", "impedance": 0.1, "is_directed": True},
    {"name": "line10", "item1": "bus5", "item2": "bus6", "impedance": 0.1, "is_directed": True},
    {"name": "line11", "item1": "bus6", "item2": "bus11", "impedance": 0.1, "is_directed": True},
    {"name": "line12", "item1": "bus6", "item2": "bus12", "impedance": 0.1, "is_directed": True},
    {"name": "line13", "item1": "bus6", "item2": "bus13", "impedance": 0.1, "is_directed": True},
    {"name": "line14", "item1": "bus12", "item2": "bus13", "impedance": 0.1, "is_directed": True},
    {"name": "line15", "item1": "bus13", "item2": "bus14", "impedance": 0.1, "is_directed": True},
    {"name": "line16", "item1": "bus10", "item2": "bus11", "impedance": 0.1, "is_directed": True},
    {"name": "line17", "item1": "bus10", "item2": "bus9", "impedance": 0.1, "is_directed": True},
    {"name": "line18", "item1": "bus14", "item2": "bus9", "impedance": 0.1, "is_directed": True},
    {"name": "line19", "item1": "bus9", "item2": "bus7", "impedance": 0.1, "is_directed": True},
    # Load connections
    {"name": "", "item1": "bus2", "item2": "load2", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus3", "item2": "load3", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus4", "item2": "load4", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus5", "item2": "load5", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus6", "item2": "load6", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus9", "item2": "load9", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus10", "item2": "load10", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus11", "item2": "load11", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus12", "item2": "load12", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus13", "item2": "load13", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "bus14", "item2": "load14", "impedance": 0.1, "is_directed": True},
    # Source connections
    {"name": "", "item1": "Gen1 Solar", "item2": "bus2", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "Gen2 Wind", "item2": "bus6", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "Gen3 Thermal", "item2": "bus3", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "Gen4 Thermal", "item2": "bus1", "impedance": 0.1, "is_directed": True},
    {"name": "", "item1": "Intertie", "item2": "bus8", "impedance": 0.1, "is_directed": True},
]
