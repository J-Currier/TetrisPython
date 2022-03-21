import pygame
import random
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
 
 
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
 
def create_grid(locked_positions={}):
    #(0, 0, 0,) black create a list of ten (width) for each row (20)
    #columns = j, rows = i 
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid
 
def convert_shape_format(shape):
    #tell what shape looks like and where in grid it exists
    positions = []
    # gives orientation of shape change! format might be a key word
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            #line ex. '..00.' shape position is equivilent to top left "corner" of list of lists, so adding the j (column) to x to get proper square that is occupied by a brick in the shape, and like-wise adding i (row) of the brick to the shape location
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
        
        #offsetting occupied space makes up for leading ... in the shape location lists of lists change! you're saving the position and then changing. Is it better to change and then save? (see the append function 2 lines up)
        for i, pos, in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions




 # checking gris to see if you are moving into a valid space
def valid_space(shape, grid):
    #creating a list of accepted positions in a 10x20 grid LU! error? if statement checking if space is already occupied by anoht
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    #flatens list in accepted_pos to a one dimensional list ex. [[(o,1)], [(2, 3)]] -> [(0, 1), (2, 3)] list comprehension (used for regular lists) 
    accepted_pos = [item for sublist in accepted_pos for item in sublist]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        #check if shape positon exists in valid position list
        if pos not in accepted_pos:
            #checking if a positve value b/c shapes will spawn above screen (-y values) and the starting position will return an invalid position 
            if pos[1] > -1:
                return False
    return True


 
def check_lost(positions):
    #checks if any positions are above the play area
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False
 
def get_shape():
    # change! consider making y value negative so that the piece materializes above visable grid and falls down
    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid(surface, grid):
    # draws lines on grid
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        #change! check formula. Drawing Vertical lines
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size ))
        for j in range(len(grid[i])):
            #drawing horizontal lines
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))


    
 
def clear_rows(grid, locked):
    pass
 
 
def draw_next_shape(shape, surface):
    pass
 
 
def draw_window(surface, grid):
    #fill with black
    surface.fill((0, 0, 0))

    #set up font, (font name, size) change! font
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)

    label = font.render("Tetris", 1, (255, 255, 255))
    
    #label placement (x, y) change! clean up formula
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))

    for i in range(len(grid)):
        #pygame.draw.rect(surface, colour, coordinates-start at 0,0 (top left x/y) and move 30 to the right or down based on which square (j/i) we are on, width, height, fill)
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    #draw border rectangle (surface, colour, (coordinatesx, y, width, height), border size)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)
    draw_grid(surface, grid)

    #update screen
    pygame.display.update()
 
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27 #how long until a shape starts falling

    #running the game:
    while run:
        fall_speed = 0.27

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime() #clock.get_rawtime gets how long since clock.tick in ms 47:30 LU!
        clock.tick() #pygame checks how ling it took for while loop to run. clock.tick(40) means that for every second st most 40 frames should pass and clock.tick will slow down the speed to match the frame rate

        if fall_time/1000 > fall_speed:
            #checking if elapsed time since last fall move is greater than set game speed
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True #locksw piece and generates next piece


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                # move piece left
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    #check if piece will be in a valid position on the game board
                    if not valid_space(current_piece, grid):
                        current_piece.x +=1

                # move piece right
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                            current_piece.x -=1

                # move piece down
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -=1

                # rotate piece
                if event.key == pygame.K_UP:
                    #error? 
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -=1


        #check and update grid as piece is moving down
        shape_pos = convert_shape_format(current_piece)

        for i in range (len(shape_pos)):
            #error? check x
                x, y = shape_pos[i]
                if y > -1:
                    #error? y, x  vs x, y
                    grid[y][x] = current_piece.color
        
        if change_piece: 
            #stores locked position piece coordinates as key in locked_pos dictionary with value of fill colour of square
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
                current_piece = next_piece
                next_piece = get_shape()
                change_piece = False


        draw_window(win, grid)

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()



 
def main_menu():
    main(win)
    


 # returns a pygame.Surface represnting the window on the screen
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
main_menu()  # start game