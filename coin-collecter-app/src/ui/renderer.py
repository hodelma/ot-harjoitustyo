import pygame


class Renderer:
    """handles rendering of sprites to the display"""
    def __init__(self, display, all_sprites, game, score_repository):
        self._display = display
        self._all_sprites = all_sprites
        self._game = game
        self._score_repository = score_repository


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
        self._draw_score()

        if self._game.state == "paused":
            self._draw_pause_menu()

        if self._game.is_over:
            self._draw_game_over()


    def _draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = f"Score: {self._game.score}"
        score_image = font.render(score_text, True, (255, 255, 255))
        self._display.blit(score_image, (10, 10))

        lives_text = f"Lives left: {self._game.lives}"
        lives_image = font.render(lives_text, True, (255, 100, 100))
        self._display.blit(lives_image, (10, 45))


    def _draw_game_over(self):
        font = pygame.font.Font(None, 50)
        small_font = pygame.font.Font(None, 36)

        if self._game.won:
            result_text = "YOU WIN!"
            color = (0, 255, 0)
        else:
            result_text = "GAME OVER!"
            color = (255, 0, 0)

        result_image = font.render(result_text, True, color)
        self._display.blit(result_image, result_image.get_rect(center=(600, 200)))

        score_image = small_font.render(f"Final score: {self._game.score}", True, (255, 255, 255))
        self._display.blit(score_image, score_image.get_rect(center=(600, 260)))

        restart_game = small_font.render("Play again (R)", True, (255, 255, 255))
        menu_text = small_font.render("Go back to main menu (SPACE)", True, (255, 255, 255))
        self._display.blit(restart_game, restart_game.get_rect(center=(600, 320)))
        self._display.blit(menu_text, menu_text.get_rect(center=(600, 370)))


    def _draw_menu(self):
        font = pygame.font.Font(None, 48)
        title = font.render("COIN GAME", True, (255, 255, 0))
        start = font.render("Start (ENTER)", True, (255, 255, 255))
        score = font.render("Scoreboard (S) (Coming soon!)", True, (255, 255, 255))
        quit_text = font.render("Quit game (Q)", True, (255, 255, 255))

        self._display.blit(title, (500, 150))
        self._display.blit(start, (500, 250))
        self._display.blit(score, (500, 320))
        self._display.blit(quit_text, (500, 390))


    def _draw_pause_menu(self):
        font = pygame.font.Font(None, 48)
        resume = font.render("Resume (ESC)", True, (255, 255, 255))
        quit_text = font.render("Back to menu (Q)", True, (255, 255, 255))

        self._display.blit(resume, (500, 250))
        self._display.blit(quit_text, (500, 320))


    def _draw_scoreboard(self):
        font_title = pygame.font.Font(None, 56)
        font = pygame.font.Font(None, 36)

        title = font_title.render("SCOREBOARD", True, (255, 255, 0))
        self._display.blit(title, (480, 80))

        high_score = self._score_repository.get_high_score()
        high_score_text = font.render(f"High Score: {high_score}", True, (0, 255, 0))
        self._display.blit(high_score_text, (520, 160))

        recent_games_text = font.render("Recent games:", True, (200, 200, 200))
        self._display.blit(recent_games_text, (520, 210))

        scores = self._score_repository.get_recent_scores(10)
        for i, score_row in enumerate(scores):
            line = font.render(f"{i + 1}.  {score_row["score"]} points", True, (255, 255, 255))
            self._display.blit(line, (520, 250 + i * 36))

        back = font.render("Back (ESC)", True, (180, 180, 180))
        self._display.blit(back, (520, 620))
