class Position:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def add_movement(self):
        pass
    
    def update(self):
        self.x_pos += movement[0]
        self.y_pos += movement[1]

