import pygame


class GameLoop:
    """manages the main game loop with event handling, updates and rendering"""
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        """ starts the game loop"""
        running = True

        while running:
            if not self._handle_events():
                running = False

            keys_pressed = pygame.key.get_pressed()

            self._level.update(keys_pressed)
            self._renderer.render()

            self._clock.tick(60)

    def _handle_events(self):
        """handles pygame events"""
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self._level.game.state == "menu":
                    if event.key == pygame.K_RETURN:
                        self._level.reset()

                    if event.key == pygame.K_q:
                        return False

            if event.type == pygame.KEYDOWN:
                if self._level.game.state == "paused":
                    if event.key == pygame.K_q:
                        self._level.game.state = "menu"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self._level.game.state == "playing":
                        self._level.game.state = "paused"
                    elif self._level.game.state == "paused":
                        self._level.game.state = "playing"

                if event.key == pygame.K_SPACE:
                    if self._level.game.is_over:
                        self._level.reset()
        return True
