import pygame


class GameLoop:
    """manages the main game loop with event handling, updates and rendering"""
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        """starts the game loop"""
        game_is_running = True

        while game_is_running:
            if not self._handle_events():
                game_is_running = False

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
                self._handle_keydown(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self._handle_click(pygame.mouse.get_pos()):
                    return False
        return True

    def _handle_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            if self._level.game.state == "playing":
                self._level.game.state = "paused"

            elif self._level.game.state == "paused":
                self._level.game.state = "playing"

    def _handle_click(self, pos):
        state = self._level.game.state
        buttons = self._renderer.button_rects

        if state == "menu":
            if buttons.get("start") and buttons["start"].collidepoint(pos):
                self._level.reset()

            elif buttons.get("scoreboard") and buttons["scoreboard"].collidepoint(pos):
                self._level.game.state = "scoreboard"

            elif buttons.get("quit") and buttons["quit"].collidepoint(pos):
                return False

        elif state == "scoreboard":
            if buttons.get("back") and buttons["back"].collidepoint(pos):
                self._level.game.state = "menu"

        elif state == "paused":
            if buttons.get("resume") and buttons["resume"].collidepoint(pos):
                self._level.game.state = "playing"

            elif buttons.get("menu") and buttons["menu"].collidepoint(pos):
                self._level.game.state = "menu"

        elif state == "game_over":
            if buttons.get("restart") and buttons["restart"].collidepoint(pos):
                self._level.reset()

            elif buttons.get("menu") and buttons["menu"].collidepoint(pos):
                self._level.game.state = "menu"

        return True
