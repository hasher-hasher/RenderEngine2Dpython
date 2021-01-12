class Sprite:
    def __init__(self):
        self.vertices = (
            (-1, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
        )

        self.edges = (
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
        )

        # texture data
        T0, T1, T2, T3 = [0, 0], [0, 1], [1, 1], [1, 0]
        uv_data = [T0, T1, T2, T3]
