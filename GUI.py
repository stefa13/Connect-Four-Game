from exceptions import GameWonException, NoWinningException
import pygame
from Game import Game

BACKGROUND_BLUE = (0, 136, 172)
YELLOW = (255, 204, 0)
RED = (255, 100, 72)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class GUI:
    def __init__(self, game, width, height, title, fps = 150):
        self._game = game
        self._init_pygame(width, height, title)
        self._setup(width,height, fps)

    def _init_pygame(self, width, height, title): 
        pygame.init()
        pygame.display.set_caption(title)
        self._screen = pygame.display.set_mode([width, height])
        self._clock = pygame.time.Clock()

    def _setup(self, width, height, fps):
        self._width = width
        self._height = height
        self._fps = fps
        self._mouseX = 0
        self._mouseY = 0
        self._mousePressed = False
        self._mouseWasPressed = False
        self._game_over = False
        self._game_over_msg = ''
        self._PlayerMove = False

        self._circle_radius = int((min(self._width / self._game.Board.Columns, self._height / self._game.Board.Rows) / 2) * 0.9)
        self._x_step = self._width / self._game.Board.Columns
        self._y_step = self._height / self._game.Board.Rows

    def render_text_centered(self, screen, text, x, y, size, color, font_type = None):
        try:
            text = str(text)
            font = pygame.font.Font(font_type, size)
            text = font.render(text, True, color)
            screen.blit(text, (x - text.get_rect().width // 2, y - text.get_rect().height // 2))
        except Exception as ex:
            print('Font Error, saw it coming')
            raise ex

    def run(self):
        finished = False

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEMOTION:
                    self._mouseX, self._mouseY = pygame.mouse.get_pos()
                    hovered_column = int(pygame.mouse.get_pos()[0] / self._x_step)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._mousePressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self._mousePressed = False
            
            if self._mousePressed:
                if not self._mouseWasPressed:
                    self._PlayerMove = True
                self._mouseWasPressed = True
            elif not self._mousePressed:
                self._mouseWasPressed = False
                self._PlayerMove = False
            
            if self._game_over:
                self.render_text_centered(self._screen, self._game_over_msg, self._width // 2, int(self._height * 0.4), 64, BLACK)
            else:
                try:
                    if self._game.Current_Player == 1 and self._PlayerMove:
                        self._game.make_player_move(hovered_column)
                        self._PlayerMove = False
                    elif self._game.Current_Player==2:
                        self._game.make_computer_move()
                except GameWonException as exc:
                    print(exc)
                    self._game_over = True
                    self._game_over_msg = str(exc)
                except NoWinningException as exc2:
                    print(exc2)
                    self._game_over = True
                    self._game_over_msg = str(exc2)
                except Exception as e:
                    print(e)

                if not self._game_over:
                    try:
                        hovered_row = self.Board.last_free_row(hovered_column)
                    except:
                        hovered_row = None
                
                self._screen.fill(BACKGROUND_BLUE)

                for row in range(self._game.Board.Rows):
                    for column in range(self._game.Board.Columns):
                        cell_value = self._game.Board.get_value(row, column)
                        if cell_value == 0:
                            pygame.draw.circle(self._screen, (YELLOW if self._game.Current_Player == 1 else RED) if (hovered_row != None and row == hovered_row and column == hovered_column) else WHITE, [int(column * self._x_step + self._x_step / 2), int(row * self._y_step + self._y_step / 2)], self._circle_radius, 2)
                        else:
                            pygame.draw.circle(self._screen, YELLOW if cell_value == 1 else RED, [int(column * self._x_step + self._x_step / 2), int(row * self._y_step + self._y_step / 2)], self._circle_radius)

            self._clock.tick(self._fps)
            pygame.display.flip()
        pygame.quit()



