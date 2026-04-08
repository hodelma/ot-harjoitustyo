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


    def _render_ui(self):
        """draws ui elements like score"""
        font = pygame.font.Font(None, 36)
        score_text = f"Score: {self._game.score}"
        score_surface = font.render(score_text, True, (255, 255, 255))
        self._display.blit(score_surface, (10, 10))

        if self._game.state == "paused":
            self._draw_pause_menu()

        if self._game.is_over:
            if self._game.won:
                result_text = "YOU WIN!"
                color = (0, 255, 0)
            else:
                result_text = "GAME OVER!"
                color = (255, 0, 0)

            result_surface = font.render(result_text, True, color)
            text_rect = result_surface.get_rect(center=(600, 200))
            self._display.blit(result_surface, text_rect)

