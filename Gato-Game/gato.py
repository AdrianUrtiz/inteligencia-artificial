import tkinter as tk
from tkinter import messagebox
import sys
import time
import math

class TicTacToe:
    def __init__(self):            
        self.board = ["-" for _ in range(9)]
        self.humanPlayer = "X"
        self.computerPlayer = "O"
        self.turn = "X"

    def print_board(self):
        print()
        for i in range(3):
            print(self.board[i * 3], self.board[i * 3 + 1], self.board[i * 3 + 2])
        print()

    def is_player_win(self, state, player):
        for i in range(3):
            if state[i * 3] == player and state[i * 3 + 1] == player and state[i * 3 + 2] == player:
                return True
            if state[i] == player and state[i + 3] == player and state[i + 6] == player:
                return True
        if state[0] == player and state[4] == player and state[8] == player:
            return True
        if state[2] == player and state[4] == player and state[6] == player:
            return True
        return False

    def is_board_filled(self, state):
        for i in range(9):
            if state[i] == "-":
                return False
        return True

    def minimax(self, state, player):
        max_player = "O"  # yourself
        other_player = "X" if player == "O" else "O"

        # first we want to check if the previous move is a winner
        if self.is_player_win(state, "X"):
            return {"position": None, "score": -1 * (len(self.actions(state)) + 1)}
        elif self.is_player_win(state, "O"):
            return {"position": None, "score": 1 * (len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # each score should maximize
        else:
            best = {"position": None, "score": math.inf}  # each score should minimize
        for possible_move in self.actions(state):
            newState = self.result(state, possible_move)
            sim_score = self.minimax(newState, other_player)
            sim_score["position"] = possible_move

            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best
    
    def players(self, state):
        n = len(state)
        x = 0
        o = 0
        for i in range(9):
            if (state[i] == "X"):
                x = x + 1
            if (state[i] == "O"):
                o = o + 1

        if (self.humanPlayer == "X"):
            return "X" if x == o else "O"
        if (self.humanPlayer == "O"):
            return "O" if x == o else "X"
        
    def actions(self, state):
        return [i for i, x in enumerate(state) if x == "-"]
    
    def result(self, state, action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState
    
    def terminal(self, state):
        if (self.is_player_win(state, "X")):
            return True
        if (self.is_player_win(state, "O")):
            return True
        return False
    
    def play(self):
        self.humanPlayer = "X"
        self.computerPlayer = "O"
        self.turn = "X"
        self.board = ["-" for _ in range(9)]
        self.print_board()
        while not self.terminal(self.board):
            if self.turn == self.humanPlayer:
                self.human_move()
            else:
                self.computer_move()
            self.print_board()
            self.turn = "X" if self.turn == "O" else "O"
        if self.is_player_win(self.board, self.humanPlayer):
            print("You win!")
        elif self.is_player_win(self.board, self.computerPlayer):
            print("You lose!")
        else:
            print("It's a tie!")

    def human_move(self):
        while True:
            square = int(input("Enter a square (0-8): "))
            print()
            if self.board[square] == "-":
                break
        self.board[square] = self.humanPlayer

    def computer_move(self):
        start = time.time()
        move = self.minimax(self.board, self.computerPlayer)
        print("Evaluation time: {}s".format(round(time.time() - start, 7)))
        print("Recommended move: {}".format(move["position"]))
        self.board[move["position"]] = self.computerPlayer

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("450x450")
        self.master.resizable(0, 0)
        self.ttt = TicTacToe()
        self.buttons = []
        for i in range(9):
            self.buttons.append(tk.Button(self.master, text=" ", font=("Helvetica", 20), height=3, width=6,
                                          command=lambda i=i: self.human_move(i)))
            self.buttons[i].grid(row=i // 3, column=i % 3)
        self.turn = "X"
        self.humanPlayer = "X"
        self.computerPlayer = "O"
        self.computer_move()

    def human_move(self, i):
        if self.ttt.board[i] == "-" and self.turn == self.humanPlayer:
            self.ttt.board[i] = self.humanPlayer
            self.buttons[i].config(text=self.humanPlayer)
            if not self.ttt.terminal(self.ttt.board):
                self.turn = "O"
                self.computer_move()

    def computer_move(self):
        move = self.ttt.minimax(self.ttt.board, self.computerPlayer)
        self.ttt.board[move["position"]] = self.computerPlayer
        self.buttons[move["position"]].config(text=self.computerPlayer)
        if self.ttt.terminal(self.ttt.board):
            if self.ttt.is_player_win(self.ttt.board, self.humanPlayer):
                messagebox.showinfo("Game Over", "You win!")
                self.master.destroy()
            elif self.ttt.is_player_win(self.ttt.board, self.computerPlayer):
                messagebox.showinfo("Game Over", "You lose!")
                self.master.destroy()
            else:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.master.destroy()
        else:
            self.turn = "X"

if __name__ == "__main__":
    if len(sys.argv) == 1:
        root = tk.Tk()
        game = Game(root)
        root.mainloop()
    else:
        ttt = TicTacToe()
        ttt.play()