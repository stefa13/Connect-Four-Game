from Board import Board
from Game import Game
from Computer import Computer
from ui import UI
from GUI import GUI
from Settings import Settings

def get_ui_from_properties(settings, game):
    if settings['ui'] == 'gui':
        window_width = int(settings['window_width'])
        window_height = int(settings['window_height'])
        window_title = settings['window_title']
        return GUI(game, window_width, window_height, window_title)
    elif settings['ui'] == 'console':
        return UI(game)

if __name__ == '__main__':
    settings = Settings("application.properties")

    board = Board(6, 7)
    computer = Computer()
    game = Game(board, computer)

    ui = get_ui_from_properties(settings, game)
    ui.run()