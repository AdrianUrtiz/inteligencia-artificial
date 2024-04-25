import pygame
import random
import math


class TicTacToe:
    def __init__(self):
        self.board = ["-" for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.humanPlayer = "X"
            self.botPlayer = "O"
        else:
            self.humanPlayer = "O"
            self.botPlayer = "X"

        pygame.init()

        self.window_size = (500, 500)
        self.screen = pygame.display.set_mode(self.window_size)

        pygame.display.set_caption("Juego del Gato")

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(i * 167, j * 167, 166, 166))

        for i, spot in enumerate(self.board):
            if spot == "X":
                pygame.draw.line(self.screen, (255, 0, 0), (i % 3 * 167 + 10, i // 3 * 167 + 10),
                                 ((i % 3 + 1) * 167 - 10, (i // 3 + 1) * 167 - 10), 5)
                pygame.draw.line(self.screen, (255, 0, 0), ((i % 3 + 1) * 167 - 10, i // 3 * 167 + 10),
                                 (i % 3 * 167 + 10, (i // 3 + 1) * 167 - 10), 5)
            elif spot == "O":
                pygame.draw.circle(self.screen, (0, 0, 255), (i % 3 * 167 + 83, i // 3 * 167 + 83), 75, 5)

    def check_winner(self, board):
        def is_player_win(state, player):
            if state[0] == state[1] == state[2] == player: return True
            if state[3] == state[4] == state[5] == player: return True
            if state[6] == state[7] == state[8] == player: return True
            if state[0] == state[3] == state[6] == player: return True
            if state[1] == state[4] == state[7] == player: return True
            if state[2] == state[5] == state[8] == player: return True
            if state[0] == state[4] == state[8] == player: return True
            if state[2] == state[4] == state[6] == player: return True
            return False

        if is_player_win(board, self.humanPlayer):
            return f"Jugador {self.humanPlayer} gana!"
        elif is_player_win(board, self.botPlayer):
            return f"Jugador {self.botPlayer} gana!"
        elif "-" not in board:
            return "Empate!"
        else:
            return None

    def minimax(self, state, player):
        def is_player_win(state, player):
            if state[0] == state[1] == state[2] == player: return True
            if state[3] == state[4] == state[5] == player: return True
            if state[6] == state[7] == state[8] == player: return True
            if state[0] == state[3] == state[6] == player: return True
            if state[1] == state[4] == state[7] == player: return True
            if state[2] == state[5] == state[8] == player: return True
            if state[0] == state[4] == state[8] == player: return True
            if state[2] == state[4] == state[6] == player: return True
            return False

        if is_player_win(state, self.botPlayer):
            return 1
        elif is_player_win(state, self.humanPlayer):
            return -1
        elif "-" not in state:
            return 0

        if player == self.botPlayer:
            best_score = -math.inf
            for i in range(9):
                if state[i] == "-":
                    state[i] = player
                    score = self.minimax(state, self.humanPlayer)
                    state[i] = "-"
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if state[i] == "-":
                    state[i] = player
                    score = self.minimax(state, self.botPlayer)
                    state[i] = "-"
                    best_score = min(score, best_score)
            return best_score

    def find_best_move(self, state):
        best_move = -1
        best_score = -math.inf
        for i in range(9):
            if state[i] == "-":
                state[i] = self.botPlayer
                score = self.minimax(state, self.humanPlayer)
                state[i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def game_loop(self):
        clock = pygame.time.Clock()
        human_turn = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and human_turn:
                    pos = pygame.mouse.get_pos()
                    x = pos[0] // 167
                    y = pos[1] // 167
                    index = x + y * 3
                    if self.board[index] == "-":
                        self.board[index] = self.humanPlayer
                        human_turn = False

            winner = self.check_winner(self.board)
            if winner:
                print(winner)
                return

            if not human_turn:
                # Bot move (minimax)
                bot_move = self.find_best_move(self.board)
                self.board[bot_move] = self.botPlayer
                human_turn = True

            self.screen.fill((0, 0, 0))
            self.draw_board()
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    game = TicTacToe()
    game.game_loop()
