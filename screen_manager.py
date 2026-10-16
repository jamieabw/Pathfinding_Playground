import pygame

class Screen_Manager:
    def __init__(self, initial_scene, **other_scenes):
        self.display = pygame.display.set_mode((800, 800))
        self.current_scene = initial_scene(self.display)


    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.current_scene.handle_event(event)
            self.current_scene.run()
            pygame.display.flip()
            clock.tick(60)