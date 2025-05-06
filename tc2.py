import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x330")
root.resizable(False, False)

# Global variables
current_player = "X"
board = [" " for _ in range(9)]
buttons = []

# Function to check for a win
def check_winner():
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# Handle button clicks
def on_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index]["text"] = current_player
        buttons[index]["state"] = "disabled"
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")

# Create the 3x3 grid of buttons
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Run the application
root.mainloop()
