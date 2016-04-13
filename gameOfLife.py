'''
The Game of Life
Python 3
Object-oriented program
Cellular Automata

Tom Logan

The game of life code is as described in
http://natureofcode.com/book/chapter-7-cellular-automata/
by Daniel Shiffman
'''
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot
from time import sleep

def main():
    '''
    Runs a home range simulation.
    '''
    
    # the size of the board
    size_x = 45
    size_y = 80
    
    # create the board
    gol = GOL(size_x,size_y)
    
    # simulate the game of life
    gol.first_display()
    i = 0
    while (i < 1000):
        i += 1
        gol.generate()
        gol.display()


class cell:
    ' the building block of the CA'
    
    def __init__(self, x, y):
        # the location
        x = int() 
        y = int()
        
        # the states
        self.state = np.random.randint(0,2)
        self.previous_state = self.state        
       
    def save_previous(self):
        self.previous_state = self.state
        
    def change_state(self, new_state):
        # the states
        self.state = new_state
    
    
    def transition(self):
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
    The game of life
    '''    

    def __init__(self, size_x, size_y):
        '''
        Creates a 2D grid of cells. Randomly seeds dead/alive.
        '''
        self.size_x = size_x
        self.size_y = size_y       
        
        # create an empty array for objects
        self.board = np.empty(shape=(size_x, size_y), dtype=object)        
        
        for i in range(0,size_x):
            for j in range(0,size_y):
                self.board[i,j] = cell(i,j)
    
    
    def generate(self):
        '''
        save the old generation
        '''
        for i in range(0,self.size_x):
            for j in range(0,self.size_y):        
                self.board[i,j].save_previous()
        
        '''
        create the new generation
        '''
        
        
        for x in range(0,self.size_x):
            for y in range(0,self.size_y):
                
                # count neighbors
                neighbors = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        x_indx = np.mod(x+i,self.size_x)
                        y_indx = np.mod(y+j,self.size_y)
                        neighbors += self.board[x_indx,y_indx].previous_state
                        
                neighbors -= self.board[x,y].previous_state # subtract the state itself
                
                # Rules of Life
                if ((self.board[x,y].state == 1) and (neighbors <= 1)):
                    # Loneliness
                    self.board[x,y].change_state(0)
                elif ((self.board[x,y].state == 1) and (neighbors >= 4)):
                    # Overpopulation
                    self.board[x,y].change_state(0)
                elif ((self.board[x,y].state == 0) and (neighbors == 3)):
                    # Reproduction
                    self.board[x,y].change_state(1) 
                
        

    def plot_data(self):
        self.gol_state = np.zeros(shape=(self.size_x,self.size_y))
        for i in range(0,self.size_x):
                for j in range(0,self.size_y):      
                    self.gol_state[i,j] = self.board[i,j].transition()
    
    def first_display(self):
        '''
        initialise plotting framework
        '''
        self.plot_data()
        pyplot.ion()
        self.fig, ax =pyplot.subplots(1,1)
        pyplot.cla()
        
        # color map of fixed colors
        cmap = mpl.colors.ListedColormap(['white','black','blue','red'])
        bounds=[0,1,2,3,4]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        self.img = pyplot.imshow(self.gol_state,interpolation='nearest',cmap = cmap,norm=norm)
        
        # grid
        ax.grid(True, which='minor', axis='both', linestyle='-', color='k')
        ax.set_xticks(range(0,self.size_y), minor=True)
        ax.set_yticks(range(0,self.size_x), minor=True)        

        # color bar
        cbar = pyplot.colorbar(self.img,cmap=cmap,
                        norm=norm,boundaries=bounds,ticks=[0,1,2,3])
        cbar.ax.set_yticklabels(['dead', 'alive','born','dying'])        
        
        # title
        ax.set_title('The Game of Life')
        
        pyplot.show() 
    
    def update_plot(self):
        self.plot_data()       
        self.img.set_data(self.gol_state) 
        self.fig.canvas.draw()        
        sleep(0.001)
    
if __name__ == '__main__':
    main() # initialise the board

 

