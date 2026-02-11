CELL_SIZE = 20
SIZE = (1280, 700)
WORLD_X, WORLD_Y = SIZE
ROWS = int(SIZE[0] // CELL_SIZE)
COLS = int(SIZE[1] // CELL_SIZE)
TERRAIN_VALUES = {
    "water": -0.1,
    "plains": 0.1,
    "hill": 0.7,
    "mountain": 0.83,
}
TROOP_R = 7
THRESHOLD = 0.5
PLAYERS = 2
COLORS = [(255, 0, 0), (0, 0, 255), (255, 150, 0), (175, 0, 175), (0, 175, 0), (0, 255, 255)]

TABLE = {
    1: [["v0", "p_top", "p_left"]],
    2: [["v1", "p_right", "p_top"]],
    3: [["p_left", "v0", "v1", "p_right"]],
    4: [["v2", "p_bottom", "p_right"]],
    5: [["v0", "p_top", "p_left"], ["v2", "p_right", "p_bottom"]],
    6: [["p_top", "v1", "v2", "p_bottom"]],
    7: [["p_left", "v0", "v1", "v2", "p_bottom"]],
    8: [["v3", "p_left", "p_bottom"]],
    9: [["p_top", "v0", "v3", "p_bottom"]],
    10: [["p_top", "v1", "p_right"], ["p_bottom", "v3", "p_left"]],
    11: [["v0", "v1", "p_right", "p_bottom", "v3"]],
    12: [["p_right", "v2", "v3", "p_left"]],
    13: [["v0", "p_top", "p_right", "v2", "v3"]],
    14: [["v1", "v2", "v3", "p_left", "p_top"]],
}
PORTS = [i for i in range(1200, 1300)]
