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
                return self._handle_keydown(event)

        return True

    def _handle_keydown(self, event):
        state = self._level.game.state

        if state == "menu":
            return self._menu_keydown(event)

        if state == "paused":
            return self._paused_keydown(event)

        if state == "playing":
            return self._playing_keydown(event)

        return True

    def _menu_keydown(self, event):
        if event.key == pygame.K_RETURN:
            self._level.reset()
            return True

        if event.key == pygame.K_q:
            return False

        return True

    def _paused_keydown(self, event):
        if event.key == pygame.K_q:
            self._level.game.state = "menu"
            return True

        if event.key == pygame.K_ESCAPE:
            self._level.game.state = "playing"
            return True

        return True

    def _playing_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            self._level.game.state = "paused"
            return True

        if event.key == pygame.K_SPACE and self._level.game.is_over:
            self._level.reset()

        return True
