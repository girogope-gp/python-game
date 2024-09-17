import pygame
from game import Game
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Shooter")

    game = Game(screen)
    menu = Menu(screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        if menu.is_active:
            menu.run()
        else:
            game.run()

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()