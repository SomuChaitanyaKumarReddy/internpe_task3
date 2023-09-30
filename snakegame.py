import tkinter as tk
import random
import time

# Constants
GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15

# Colors
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Snake Game")
        
        self.canvas = tk.Canvas(window, width=GRID_WIDTH * GRID_SIZE, height=GRID_HEIGHT * GRID_SIZE, bg=BG_COLOR)
        self.canvas.pack()

        self.snake = [(4, 4), (4, 3), (4, 2)]
        self.direction = RIGHT
        self.food = self.spawn_food()
        self.score = 0

        self.window.bind("<KeyPress>", self.change_direction)
        self.update()

    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != DOWN:
            self.direction = UP
        elif key == "Down" and self.direction != UP:
            self.direction = DOWN
        elif key == "Left" and self.direction != RIGHT:
            self.direction = LEFT
        elif key == "Right" and self.direction != LEFT:
            self.direction = RIGHT
            
    def change_direction(self, event):
        key = event.keysym
        if key == "w" and self.direction != DOWN:
            self.direction = UP
        elif key == "s" and self.direction != UP:
            self.direction = DOWN
        elif key == "a" and self.direction != RIGHT:
            self.direction = LEFT
        elif key == "d" and self.direction != LEFT:
            self.direction = RIGHT


    def update(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in self.snake[1:]
        ):
            self.game_over()
            return

        self.draw_board()
        self.window.after(100, self.update)  # Update every 100 milliseconds

    def draw_board(self):
        self.canvas.delete("all")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * GRID_SIZE,
                y * GRID_SIZE,
                (x + 1) * GRID_SIZE,
                (y + 1) * GRID_SIZE,
                fill=SNAKE_COLOR,
            )

        x, y = self.food
        self.canvas.create_oval(
            x * GRID_SIZE,
            y * GRID_SIZE,
            (x + 1) * GRID_SIZE,
            (y + 1) * GRID_SIZE,
            fill=FOOD_COLOR,
        )

        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE - 30, 10, text=f"Score: {self.score}", fill="white"
        )

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE // 2,
            GRID_HEIGHT * GRID_SIZE // 2,
            text="Game Over",
            fill="white",
            font=("Helvetica", 24),
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
