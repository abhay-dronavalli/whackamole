import pygame
import random
#black = (0, 0, 0)

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_image = pygame.image.load("mole.png")
        mole_position = (0,0) #mole_position is the specfic square of the grid in which the mole is, 0,0 being the top left corner square

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    #places the mole in the top left of the square it is in such that it doesnt interfere with gridlines
                    mole_rect = mole_image.get_rect(center = (mole_position[0]*32,mole_position[1]*32))
                    if mole_rect.collidepoint(mouse_x,mouse_y):
                        #randomizing the square in the grid that the mole gets moved to
                        mole_position = (random.randrange(0,20), random.randrange(0,16))
            screen.fill("light green")
            for i in range (1,21):
                pygame.draw.line(screen, 'black' , (32*i, 0), (32*i, 512))
            for i in range(1,17):
                pygame.draw.line(screen, 'black', (0, 32*i), (640, 32*i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position[0]*32, mole_position[1]*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
