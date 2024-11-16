import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates to improve performance

# Snake head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"  # Initial direction

# Snake body segments
segments = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score
score = 0
high_score = 0

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.color("white")
score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Functions for controlling the snake
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

# Function to move the snake
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# Function to check for collisions with the wall
def check_wall_collision():
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        return True
    return False

# Function to check for collisions with the body
def check_body_collision():
    for segment in segments:
        if segment.distance(snake_head) < 20:
            return True
    return False

# Function to update the score
def update_score():
    global score, high_score
    if score > high_score:
        high_score = score
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Main game loop
def game_loop():
    global score

    # Move the snake
    move()

    # Check for collision with the wall
    if check_wall_collision():
        game_over()
        return

    # Check for collision with the body
    if check_body_collision():
        game_over()
        return

    # Check if the snake eats the food
    if snake_head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))  # Move food to a new random position
        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        score += 10  # Increase score
        update_score()

    # Move the body segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first body segment to the head's position
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    # Keep updating the screen
    screen.update()

    # Repeat the game loop after a small delay
    time.sleep(0.1)

    # Continue the game loop
    game_loop()

# Game over function
def game_over():
    global score
    score = 0
    segments.clear()
    snake_head.goto(0, 0)
    snake_head.direction = "stop"
    update_score()
    print("Game Over! Press 'r' to restart.")

# Restart the game
def restart():
    global score
    score = 0
    segments.clear()
    snake_head.goto(0, 0)
    snake_head.direction = "stop"
    update_score()
    game_loop()

# Set up the keyboard controls
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")
screen.onkey(restart, "r")  # Press 'r' to restart the game

# Start the game loop
game_loop()

# Keep the window open
screen.mainloop()
