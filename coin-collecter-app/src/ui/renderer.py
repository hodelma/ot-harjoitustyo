import pygame


def draw_button(display, text, font, rect, color=(80, 80, 80), text_color=(255, 255, 255), hover=False):
    background_color = tuple(min(c + 40, 255) for c in color) if hover else color
    pygame.draw.rect(display, background_color, rect, border_radius=8)
    pygame.draw.rect(display, (200, 200, 200), rect, 2, border_radius=8)
    label = font.render(text, True, text_color)
    display.blit(label, label.get_rect(center=rect.center))


class Renderer:
    """handles rendering of sprites to the display"""
    def __init__(self, display, all_sprites, game, score_repository):
        self._display = display
        self._all_sprites = all_sprites
        self._game = game
        self._score_repository = score_repository
        self.button_rects = {}

    def render(self):
        """draws all sprites and update display"""
        self._display.fill((0, 0, 0))
        self.button_rects = {}
        mouse_position = pygame.mouse.get_pos()

        if self._game.state == "menu":
            self._draw_menu(mouse_position)
        elif self._game.state == "scoreboard":
            self._draw_scoreboard(mouse_position)
        else:
            self._all_sprites.draw(self._display)
            self._render_ui(mouse_position)

        pygame.display.update()

    def _render_ui(self, mouse_position):
        """draws ui elements like score"""
        self._draw_score()

        if self._game.state == "paused":
            self._draw_pause_menu(mouse_position)

        if self._game.is_over:
            self._draw_game_over(mouse_position)

    def _draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = f"Score: {self._game.score}"
        score_image = font.render(score_text, True, (255, 255, 255))
        self._display.blit(score_image, (10, 10))

        lives_text = f"Lives left: {self._game.lives}"
        lives_image = font.render(lives_text, True, (255, 100, 100))
        self._display.blit(lives_image, (10, 45))

    def _draw_menu(self, mouse_position):
        self._draw_menu_texts()
        self._draw_menu_buttons(mouse_position)

    def _draw_menu_texts(self):
        font_title = pygame.font.Font(None, 100)
        font_title.set_bold(True)
        font_info = pygame.font.Font(None, 40)
        title = font_title.render("COIN GAME", True, (255, 255, 0))
        info = font_info.render("Welcome to the Coin Game. Watch out for the monsters!", True, (255, 150, 0))
        self._display.blit(title, title.get_rect(center=(625, 150)))
        self._display.blit(info, info.get_rect(center=(625, 210)))

    def _draw_menu_buttons(self, mouse_position):
        btn_font = pygame.font.Font(None, 42)
        start_rect = pygame.Rect(0, 0, 260, 54)
        start_rect.center = (625, 300)
        score_rect = pygame.Rect(0, 0, 260, 54)
        score_rect.center = (625, 380)
        quit_rect = pygame.Rect(0, 0, 260, 54)
        quit_rect.center = (625, 460)

        draw_button(self._display, "Start", btn_font, start_rect,
                    color=(0, 100, 0), text_color=(0, 255, 0),
                    hover=start_rect.collidepoint(mouse_position))

        draw_button(self._display, "Scoreboard", btn_font, score_rect,
                    hover=score_rect.collidepoint(mouse_position))

        draw_button(self._display, "Quit", btn_font, quit_rect,
                    color=(100, 0, 0), text_color=(255, 80, 80),
                    hover=quit_rect.collidepoint(mouse_position))

        self.button_rects["start"] = start_rect
        self.button_rects["scoreboard"] = score_rect
        self.button_rects["quit"] = quit_rect

    def _draw_pause_menu(self, mouse_position):
        btn_font = pygame.font.Font(None, 42)
        resume_rect = pygame.Rect(0, 0, 240, 54)
        resume_rect.center = (625, 260)
        menu_rect = pygame.Rect(0, 0, 240, 54)
        menu_rect.center = (625, 330)

        draw_button(self._display, "Resume", btn_font, resume_rect,
                    color=(0, 80, 0), hover=resume_rect.collidepoint(mouse_position))

        draw_button(self._display, "Back to menu", btn_font, menu_rect,
                    color=(80, 0, 0), hover=menu_rect.collidepoint(mouse_position))

        self.button_rects["resume"] = resume_rect
        self.button_rects["menu"] = menu_rect

    def _draw_game_over(self, mouse_position):
        self._draw_game_over_result()
        self._draw_game_over_buttons(mouse_position)

    def _draw_game_over_result(self):
        font = pygame.font.Font(None, 50)
        btn_font = pygame.font.Font(None, 36)

        if self._game.won:
            result_text = "YOU WIN!"
            bright_color = (0, 255, 0)
            dark_color = (0, 100, 0)

        else:
            result_text = "GAME OVER!"
            bright_color = (255, 0, 0)
            dark_color = (100, 0, 0)

        current_time = pygame.time.get_ticks()
        blink_color = bright_color if (current_time // 500) % 2 == 0 else dark_color
        result_image = font.render(result_text, True, blink_color)
        self._display.blit(result_image, result_image.get_rect(center=(600, 200)))

        score_image = btn_font.render(f"Final score: {self._game.score}", True, (255, 255, 255))
        self._display.blit(score_image, score_image.get_rect(center=(600, 260)))

    def _draw_game_over_buttons(self, mouse_position):
        btn_font = pygame.font.Font(None, 36)
        r_rect = pygame.Rect(0, 0, 220, 48)
        r_rect.center = (600, 320)
        m_rect = pygame.Rect(0, 0, 280, 48)
        m_rect.center = (600, 385)

        draw_button(self._display, "Play again", btn_font, r_rect,
                    hover=r_rect.collidepoint(mouse_position))

        draw_button(self._display, "Main menu", btn_font, m_rect,
                    hover=m_rect.collidepoint(mouse_position))

        self.button_rects["restart"] = r_rect
        self.button_rects["menu"] = m_rect

    def _draw_scoreboard(self, mouse_position):
        self._draw_scoreboard_content()
        self._draw_scoreboard_buttons(mouse_position)

    def _draw_scoreboard_content(self):
        font_title = pygame.font.Font(None, 56)
        font = pygame.font.Font(None, 36)
        title = font_title.render("SCOREBOARD", True, (255, 255, 0))
        self._display.blit(title, title.get_rect(center=(625, 80)))

        high_score = self._score_repository.get_high_score()
        high_score_text = font.render(f"High Score: {high_score}", True, (0, 255, 0))
        self._display.blit(high_score_text, (520, 160))

        recent_games_text = font.render("Recent games:", True, (200, 200, 200))
        self._display.blit(recent_games_text, (520, 210))

        scores = self._score_repository.get_recent_scores(10)
        for i, score_row in enumerate(scores):
            line = font.render(f"{i + 1}.  {score_row['score']} points", True, (255, 255, 255))
            self._display.blit(line, (520, 250 + i * 36))

    def _draw_scoreboard_buttons(self, mouse_position):
        btn_font = pygame.font.Font(None, 36)
        back_rect = pygame.Rect(0, 0, 180, 48)
        back_rect.center = (625, 630)

        draw_button(self._display, "Back", btn_font, back_rect,
                    hover=back_rect.collidepoint(mouse_position))
        self.button_rects["back"] = back_rect
