import pygame
import sys

from core.input import Input


class Base:
    def __init__(self):

        # initialize all pygame modules
        pygame.init()

        screen_size = (512, 512)

        display_flags = pygame.DOUBLEBUF | pygame.OPENGL

        # setting additional attributes for OpenGL
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_COMPATIBILITY)
        # pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)

        # create and display window
        self.screen = pygame.display.set_mode(
            screen_size,
            display_flags
        )

        # screen upper bar title
        pygame.display.set_caption("Computer Graphics Course")

        # is the game running?
        self.running = True

        # manage time related data and operations
        self.clock = pygame.time.Clock()

        # input class
        self.input = Input()

    # implemented by extending class
    def initialize(self):
        pass

    # implemented by extending class
    def update(self):
        pass

    def run(self):
        # startup
        self.initialize()

        # main loop
        while self.running:
            # process input #
            self.input.update()

            if self.input.quit:
                self.running = False

            # update #
            self.update()

            # render #

            # display image in screen
            pygame.display.flip()

            # pause if necessary to achieve 60 fps
            self.clock.tick(60)

        # shutdown #
        pygame.quit()
        sys.exit()
