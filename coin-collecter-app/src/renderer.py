import pygame


class Renderer:
    """handles rendering of sprites to the display"""
    def __init__(self, display, all_sprites, game):
        self._display = display
        self._all_sprites = all_sprites
        self._game = game


    def render(self):
        """draws all sprites and update display"""
        self._display.fill((0, 0, 0))

        if self._game.state == "menu":
            self._draw_menu()

        elif self._game.state == "scoreboard":
            self._draw_scoreboard()

        else:
            self._all_sprites.draw(self._display)
            self._render_ui()

        pygame.display.update()

