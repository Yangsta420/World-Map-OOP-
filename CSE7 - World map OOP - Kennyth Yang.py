class Room():
    def __init__(self, the_name, N, S, E, W, U, D, the_description):
        self.name = the_name
        self.description= the_description
        self.north = N
        self.south = S
        self.east = E
        self.west = W
        self.up = U
        self.down = D
    def move(self, direction):
        '''This function allows movement to a different node.
        '''
        global node
        node = globals()[getattr(self,direction)]
        
r19a = Room('Wiebe\'s room', ' parking_lot', None, None, None, None, None, "This is your computer science classroom")

parking_lot = Room('Parking_lot', None, 'r19a', None, None, None, None, "It its filled with cars.")

node = r19a

