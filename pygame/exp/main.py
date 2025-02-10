import pygame
from game_object import GameObject
from position import Position
from user_input import UserInput

pygame.init()
pygame.display.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Fl")

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
position1 = Position(100, 100)
tile_size = 32
user = UserInput()

objects = [
    GameObject(position1, 50, 50, (255, 0, 0), 1)
    #To add more, add a comma after this ^ object then follow the format.
]
running = True
loop=0
while running:
    loop+=1
    print(f"LOOP: {loop}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,100))
    for x in range(0, screen_width, tile_size):
        pygame.draw.line(screen, white, (x, 0), (x, screen_height))
    for y in range(0, screen_height, tile_size):
        pygame.draw.line(screen, white, (0, y), (screen_width, y))
    user.check()
    action=0
    if user.keys[pygame.K_ESCAPE]:
        print("Exiting...")
        running = False
        
    if user.keys[pygame.K_LSHIFT]:
        #ad-hoc ugly solution1
        objects[0].speed = 2 #Horrific isn't it?
    if user.keys[pygame.K_w]:
        action = (0, -1)
    elif user.keys[pygame.K_s]:
        action = (0, 1)
    elif user.keys[pygame.K_a]:
        action = (-1, 0)
    elif user.keys[pygame.K_d]:
        action = (1, 0)
    else:
        pass
    
    for obj in objects:
        obj.update(action)
        obj.draw(screen)
        obj.speed = 1

    grid_x = (user.mouse_pos[0] // tile_size) * tile_size
    grid_y = (user.mouse_pos[1] // tile_size) * tile_size
    pygame.draw.rect(screen, (0, 255, 0), (grid_x, grid_y, tile_size, tile_size), 2)
    pygame.event.pump()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
