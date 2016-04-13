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
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot

###
# User inputs
###
size_x = 30
size_y = 40



class cell:
    ' the building block of the CA'
    
    def __init__(self, x, y):
        # the location
        x = int() 
        y = int()
        # the size
        w = int()
        # the states
        self.state = np.random.randint(0,2)
        self.previous_state = self.state        
       
    def save_previous(self):
        self.previous = self.state
        
    def change_state(self, new_state):
        # the states
        self.state = new_state
    
    
    def display(self):
        if ((self.previous_state == 0) and (self.state == 1)):
            # a cell is born
            value = 2
        elif (self.state == 1):
            # no change - cell is alive
            value = 1
        elif (self.previous_state == 1 and self.state == 0):
            # a cell dies
            value = 3
        else:
            # no change - cell is dead
            value = 0
           
    return(value)
            

class GOL():
    '''
    The 2D grid 
    '''
    
    w = 8
    columns = 0
    rows = 0
    
    board = np.empty(shape=(size_x, size_y), dtype=object)
    

    def __init__(self, size_x, size_y):
        '''
        Sets a size, but you still need to populate qualities before use
        '''
        for x in range(0,size_x):
            for y in range(0,size_y):
                board[i,j] = cell(i,j)
    
    def generate():
        '''
        save the old generation
        '''
        for x in range(0,size_x):
            for y in range(0,size_y):        
                board[i,j].save_previous()
    
    
    # loop through the cells in the board
    for x in range(0,size_x):
        for y in range(0,size_y):
            
            # count neighbors
            neighbors = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    neighbors += board[x+i,y+i].previous_state
                    
            neighbors -= board[x,y].previous_state # subtract the state itself
            
            # Rules of Life
            if ((board[x,y].state == 1) and (neighbors <= 1)):
                # Loneliness
                board[x,y].change_state(0)
            elif ((board[x,y].state == 1) and (neighbors >= 4)):
                # Overpopulation
                board[x,y].change_state(0)
            elif ((board[x,y].state == 0) and (neighbors == 3)):
                # Reproduction
                board[x,y].change_state(1)     

    def display():
        zvals = np.zeros(size_x,size_y)
        for x in range(0,size_x):
                for y in range(0,size_y):      
                    zvals[i,j] = board[i,j].display()
        
        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['white','black','blue','red'])
        bounds=[0,1,2,3,4]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        
        # tell imshow about color map so that only set colors are used
        img = pyplot.imshow(zvals,interpolation='nearest',
                            cmap = cmap,norm=norm)
        
        # make a color bar
        cbar = pyplot.colorbar(img,cmap=cmap,
                        norm=norm,boundaries=bounds,ticks=[0,1,2,3])
        cbar.ax.set_yticklabels(['dead', 'alive','born','dying'])
        
        pyplot.show()    


# initialise the board
board = grid(size_x, size_y)
 

