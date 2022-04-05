# by da winston
import time
import sys, pygame
pygame.init() #setup variables

size = width, height = 1920 , 1080     #window size

background_color = 135,206,235
def snap(x, base=300):
    return base * round(x/base)

screen = pygame.display.set_mode(size) # makes window
''' list for the blocks '''
blocks = [pygame.image.load(r"C:\Users\Winston\Pictures\trueiso\acacia_planks.png"),pygame.image.load(r"C:\Users\Winston\Pictures\trueiso\cobblestone.png"), pygame.image.load(r"C:\Users\Winston\Pictures\trueiso\basalt.png")]

blocks_rect = []
index = 0
pygame.display.set_caption('THE epic geme thing')

for bloc in blocks: # make list for all block rects
    blocks_rect.append(blocks[index].get_rect())
    index+=1
previous_press = None
press = None
block = None
block_index = 0

display_blocks = [] # these will be blitted in order
background = pygame.image.load(r"C:\Users\Winston\Pictures\trueiso\background.png")
background_rect = background.get_rect()




def block(blockindex):
    return [blocks[block_index], blockscopy()]
screen.blit(background, background_rect)
framecount = 0
max_fps = 60
fps_split = max_fps
fps = 0
while True:
    tic = time.perf_counter()
    
    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            screen.blit(background, background_rect)

            
    
    mouse = pygame.mouse.get_pos() # get mouse position
    block = blocks_rect[block_index]
    if snap(mouse[0],150)%300 == 0:  
        block.center = [snap(mouse[0],300), snap(mouse[1], 173)] # go to mouse
    elif snap(mouse[0],150)%300 != 0:
        block.center = [snap(mouse[0],150), snap(mouse[1], 173)+347/4] # go to mouse
    if not pygame.mouse.get_pressed() == previous_press: # new click
        press = pygame.mouse.get_pressed()
        if press[0]: # leftclick
            
            screen.blit(blocks[block_index], block.copy()) # copy block
            
            
        elif press[2]: # rightclick
            
            if block_index+1 != len(blocks):
                block_index+=1
            elif block_index+1 == len(blocks):
                
                block_index = 0
                
            
        previous_press = press


    block_image = blocks[block_index]
    framecount+=1
    

    pygame.display.flip() # updates screen

    time.sleep(1/fps_split)
    toc = time.perf_counter()
    
    print(f"fps: ", round(1/(toc-tic)),'         fps split = ', fps_split)
    
    fps = 1/(toc-tic)
    if fps < max_fps:
        fps_split +=1
    elif fps > max_fps:
        fps_split -=1
    else:
        pass
    