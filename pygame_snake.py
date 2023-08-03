import pygame
import random

# initialise pygame 
pygame.init()

# set up variables for the game
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 400
dis_height = 400 

# Set up drawing window/display
dis = pygame.display.set_mode((dis_width, dis_height))

# Create clock object (to regulate speed of game loop)
clock = pygame.time.Clock()

# Start game
def run():
    # co-ords of snake
    x1 = dis_width / 2
    y1 = dis_height / 2 

    # direction of movement
    dir = [0, 0]

    # keep track of co-ords of each part of snake's body
    snake_list = []

    snake_length = 1
    food_x = 30
    food_y = 30

    # main game loop
    # Python handles main event messaging through event queue
    # change co-ords depending on key 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir = [-10, 0]
                elif event.key == pygame.K_RIGHT:
                    dir = [10, 0]
                elif event.key == pygame.K_UP:
                    dir = [0, -10]
                elif event.key == pygame.K_DOWN:
                    dir = [0, 10]

        # add updated direction to snake co-ords
        x1 += dir[0]
        y1 += dir[1]
        # fill background with blue 
        dis.fill(blue)
        # draw rectangle
        pygame.draw.rect(dis, green, [food_x, food_y, 10, 10])

        # add head of snake to body & remove last body piece if it is longer than the length
        snake_list.append([x1, y1])
        if len(snake_list) > snake_length:
            del snake_list[0]

        # if snakes hits itself, restart game
        if ([x1, y1] in snake_list[:-1]):
            run()

        # if snakes hits edges, restart game
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            run()

        # draw rectangle for each body element of the snake
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], 10, 10])

        # if snake's head touches food, move food to random spot and make the snake longer
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - 10) / 10) * 10
            food_y = round(random.randrange(0, dis_height - 10) / 10) * 10
            snake_length += 1

        # use pygame to update display 
        pygame.display.update()
        # prevent game from running at more than 10 frames/sec
        clock.tick(10)

run()
    