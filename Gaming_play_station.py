import tkinter as tk
from tkinter import messagebox

class GamingStation:
    def __init__(self, master):
        self.master = master
        master.title("Gaming Station")
        self.current_game = None

        self.tic_tac_toe_button = tk.Button(master, text="Tic Tac Toe", command=self.play_tic_tac_toe)
        self.tic_tac_toe_button.grid(row=0, column=0)

        self.quiz_game_button = tk.Button(master, text="Quiz Game", command=self.play_quiz_game)
        self.quiz_game_button.grid(row=1, column=0)

    def play_tic_tac_toe(self):
        if self.current_game:
            self.current_game.destroy()

        self.current_game = TicTacToe(self.master)

    def play_quiz_game(self):
        if self.current_game:
            self.current_game.destroy()

        self.current_game = QuizGame(self.master)

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text='', font=('Helvetica', 24), width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.destroy()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.destroy()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def update_button(self, row, col):
        button = tk.Button(self.master, text=self.current_player, font=('Helvetica', 24), width=5, height=2, state=tk.DISABLED)
        button.grid(row=row, column=col)

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Paris', 'Berlin', 'London', 'Madrid'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the largest mammal?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Gorilla'],
                'correct_answer': 'Blue Whale'
            }
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text='')
        self.question_label.grid(row=0, column=0, columnspan=4)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text='', command=lambda i=i: self.check_answer(i))
            button.grid(row=1, column=i)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])
            for i in range(4):
                self.option_buttons[i].config(text=question_data['options'][i])

            self.current_question_index += 1
        else:
            messagebox.showinfo("Quiz Game", f"Quiz completed! Your score: {self.score}")
            self.destroy()

    def check_answer(self, option_index):
        selected_option = self.questions[self.current_question_index - 1]['options'][option_index]
        correct_answer = self.questions[self.current_question_index - 1]['correct_answer']

        if selected_option == correct_answer:
            self.score += 1

        self.next_question()

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

# Create the main Tkinter window
root = tk.Tk()

# Instantiate the GamingStation class
gaming_station = GamingStation(root)

# Run the Tkinter event loop
root.mainloop()
