"""
ROBOT CLASS | TOY ROBOT TECHNICAL ASSESSMENT
"""
TABLE_WIDTH = 5
TABLE_HEIGHT = 5
DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']


class Robot():
    def __init__(self):
        self.direction = None
        self.pos_x = None
        self.pos_y = None
        self.table = {
            row: {
                col: '-' for col in range(TABLE_WIDTH)
            } for row in reversed(range(TABLE_HEIGHT))
        }
    
    def is_move_valid(self, new_pos_x, new_pos_y):
        return new_pos_y in self.table and new_pos_x in self.table[new_pos_y]
    
    def is_pos_taken(self, pos_x, pos_y):
        if not self.is_move_valid(pos_y, pos_x):
            print('Error: Position is not valid.')
            return True
        
        if self.table[pos_y][pos_x] != '-':
            print('Error: Position is already taken.')
            return True
        return False
    
    def get_facing_direction(self, direction):
        if direction == DIRECTIONS[0]:
            return '↑'
        elif direction == DIRECTIONS[1]:
            return '→'
        elif direction == DIRECTIONS[2]:
            return '↓'
        elif direction == DIRECTIONS[3]:
            return '←'
    
    def place_robot(self, position):
        self.pos_x, self.pos_y, self.direction = position.split(',')
        self.pos_x = int(self.pos_x)
        self.pos_y = int(self.pos_y)
        
        if self.is_pos_taken(self.pos_x, self.pos_y):
            return
        
        self.table[int(self.pos_y)][int(self.pos_x)] = self.get_facing_direction(self.direction)

    def move_robot(self):
        new_pos_x = self.pos_x
        new_pos_y = self.pos_y
    
        if self.direction == DIRECTIONS[0] and self.pos_y < 4:
            new_pos_y = self.pos_y + 1
        elif self.direction == DIRECTIONS[1] and self.pos_x < 4:
            new_pos_x = self.pos_x + 1
        elif self.direction == DIRECTIONS[2] and self.pos_y > 0:
            new_pos_y = self.pos_y - 1
        elif self.direction == DIRECTIONS[3] and self.pos_x > 0:
            new_pos_x = self.pos_x - 1
            
        
        self.table[self.pos_y][self.pos_x] = '-'
        
        if self.is_pos_taken(new_pos_x, new_pos_y):
            self.table[self.pos_y][self.pos_x] = self.get_facing_direction(self.direction)
            return
        
        self.table[new_pos_y][new_pos_x] = self.get_facing_direction(self.direction)
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y
    
    def rotate_robot(self, new_direction):
        idx = DIRECTIONS.index(self.direction) - 1 if new_direction == 'LEFT' else DIRECTIONS.index(self.direction) + 1
        self.direction = DIRECTIONS[idx % 4]
        
        self.table[int(self.pos_y)][int(self.pos_x)] = self.get_facing_direction(self.direction)
        
    def report(self):
        print(f'Output: {self.pos_y},{self.pos_x},{self.direction}')
        
    def show_table(self): 
        for row in reversed(range(TABLE_HEIGHT)):
            print(' '.join(str(self.table[row][col]) for col in range(TABLE_WIDTH)))