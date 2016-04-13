'''
The Game of Life
Python 3
Object-oriented
Cellular Automata

Tom Logan

The game of life code is as described in
http://natureofcode.com/book/chapter-7-cellular-automata/
by Daniel Shiffman
'''


class cell:
    ' the building block of the CA'
    
    def __init__(self, x, y, size):
        # the location
        x = int() 
        y = int()
        # the size
        w = int()
        
    def change_state(self, new_state):
        # the states
        self.state = int()
        self.previous_state = self.state
        self.state = new_state
    
    
    def display(self):
        if ((self.previous_state == 0) and (self.state == 1)):
            # a cell is born
            print('blue')
        elif (self.state == 1):
            # a cell 
            print('black')
        elif (self.previous_state == 1 and self.state == 0):
            # a cell dies
            print('red')
        else:
            print('white')
           
        # something else here
            
            
    
