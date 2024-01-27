import pygame


class UI:
    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((640, 480))
        self._window.fill((0, 0, 0))
        pygame.display.flip()
        pygame.display.set_caption("Connect Four")

        self.main_loop()

    def main_loop(self):
        while True:
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


ui = UI()
