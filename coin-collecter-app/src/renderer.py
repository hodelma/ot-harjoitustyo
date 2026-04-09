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

            instruction_text = "Press SPACE to return to menu"
            instruction_surface = font.render(instruction_text, True, (255, 255, 255))
            instruction_rect = instruction_surface.get_rect(center=(600, 250))
            self._display.blit(instruction_surface, instruction_rect)


    def _draw_menu(self):
        font = pygame.font.Font(None, 48)
        title = font.render("COIN GAME", True, (255, 255, 0))
        start = font.render("Start (ENTER)", True, (255, 255, 255))
        score = font.render("Scoreboard (S)", True, (255, 255, 255))
        quit_text = font.render("Quit (Q)", True, (255, 255, 255))

        self._display.blit(title, (500, 150))
        self._display.blit(start, (500, 250))
        self._display.blit(score, (500, 320))
        self._display.blit(quit_text, (500, 390))


    def _draw_pause_menu(self):
        font = pygame.font.Font(None, 48)
        resume = font.render("Resume (ESC)", True, (255, 255, 255))
        quit_text = font.render("Quit (Q)", True, (255, 255, 255))

        self._display.blit(resume, (500, 250))
        self._display.blit(quit_text, (500, 320))


    def _draw_scoreboard(self):
        font = pygame.font.Font(None, 48)
        text = font.render(f"High Score: {self._game.high_score}", True, (255, 255, 255))
        self._display.blit(text, (500, 300))
