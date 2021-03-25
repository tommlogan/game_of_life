'''
The Game of Life
Python 3
Object-oriented program
Cellular Automata

Tom M Logan
www.tomlogan.co.nz

Amaraj Judge
www.amarajjudge.com/

The game of life code is as described in
http://natureofcode.com/book/chapter-7-cellular-automata/
by Daniel Shiffman
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import sleep
from scipy import signal
from mpl_toolkits.axes_grid1 import make_axes_locatable
# import cProfile
# import pstats

def main(showPlot=True):
    '''
    Runs a home range simulation.
    '''
    
    # the size of the board
    size_x = 45
    size_y = 80
    
    # create the board
    gol = GOL(size_x,size_y)
    
    # create kernel for convolution
    kernel = np.ones((3, 3), dtype='uint8')
    kernel[1,1] = 0

    # simulate the game of life
    if showPlot:
        gol.first_display()
    # update each time    
    i = 0
    while (i < 200):
        i += 1
        gol.generate(kernel)
        if showPlot:
            gol.update_plot()


class GOL:
    '''
    The game of life
    '''    

    def __init__(self, size_x, size_y):
        '''
        Creates a 2D grid of cells. Randomly seeds dead/alive.
        '''
        self.size_x = size_x
        self.size_y = size_y       
        
        # initialise a random board of dead and alive cells
        self.board = np.random.randint(0,2,size = (size_x, size_y), dtype='uint8')        

        # initialise the board for saving the previous state
        self.previous_board = np.copy(self.board)
    

    def save_previous_board(self):
        '''
        save the old generation
        '''
        self.previous_board = np.copy(self.board)


    def generate(self, kernel):
        '''
        save the old generation
        '''
        self.save_previous_board()
        
        '''
        create the new generation
        '''
        
        # count neighbors of each cell
        neighbors_count = signal.convolve2d(self.previous_board, kernel, mode='same')        
        
        for x in range(0,self.size_x):
            for y in range(0,self.size_y):
                # Rules of Life
                if ((self.board[x,y] == 1) and (neighbors_count[x,y] <= 1)):
                    # Loneliness
                    self.board[x,y] = 0
                elif ((self.board[x,y] == 1) and (neighbors_count[x,y] >= 4)):
                    # Overpopulation
                    self.board[x,y] = 0
                elif ((self.board[x,y] == 0) and (neighbors_count[x,y] == 3)):
                    # Reproduction
                    self.board[x,y] = 1
                

    def plot_data(self):
        '''
        assigns plotting colors based on change in state
        '''
        self.gol_state = np.zeros(shape=(self.size_x,self.size_y), dtype='uint8')
        for i in range(0,self.size_x):
                for j in range(0,self.size_y):      
                    if ((self.previous_board[i,j] == 0) and (self.board[i,j] == 1)):
                        # a cell is born
                        self.gol_state[i,j] = 2
                    elif (self.board[i,j] == 1):
                        # no change - cell is alive
                        self.gol_state[i,j] = 1
                    elif (self.previous_board[i,j] == 1 and self.board[i,j] == 0):
                        # a cell dies
                        self.gol_state[i,j] = 3
                    else:
                        # no change - cell is dead
                        self.gol_state[i,j] = 0
    

    def first_display(self):
        '''
        initialise plotting framework
        '''
        self.plot_data()
        plt.ion()
        self.fig, ax =plt.subplots(1,1)
        plt.cla()
        
        # color map of fixed colors
        cmap = mpl.colors.ListedColormap(['white','black','blue','red'])
        bounds=[0,1,2,3,4]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        self.img = plt.imshow(self.gol_state,interpolation='nearest',cmap = cmap,norm=norm)
                
        # grid  
        # ax.grid(False, which='minor', axis='both', linestyle='-', color='k')
        # ax.set_xticks(range(0,self.size_y), minor=True)
        # ax.set_yticks(range(0,self.size_x), minor=True)       
        plt.axis('off')
        
        # color bar
        # divider = make_axes_locatable(ax)
        # cax = divider.append_axes("right", size="1%")
        cbar = plt.colorbar(self.img,cmap=cmap, norm=norm,boundaries=bounds,ticks=[0,1,2,3])
        cbar.ax.set_yticklabels(['dead', 'alive','born','dying'])        
        
        # title
        ax.set_title('The Game of Life')
        
        plt.show() 
    

    def update_plot(self):
        self.plot_data()       
        # import code
        # code.interact(local=locals())
        self.img.set_data(self.gol_state) 
        self.fig.canvas.draw()
        plt.pause(0.0001)
        # sleep(0.1)
    

# def profile():
#     cProfile.run('main(showPlot=False)', 'stats')
#     p = pstats.Stats('stats')
#     p.sort_stats('time').print_stats(20)    

    
if __name__ == '__main__':
    # profile() # initialise the board
    main(showPlot=True)
