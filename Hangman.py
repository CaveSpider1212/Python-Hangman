import turtle as t
import random

def drawPart(shape, size, angle, distance): # Draw part, then go to new positiion
    t.pendown()
    if shape == "circle":
        t.circle(size)
    if shape == "line":
        t.forward(size)
    t.penup()
    t.right(angle)
    t.forward(distance)

# Turtle settings
t.pensize(width = 5)
t.speed(10)

# Drawing the gallows
t.penup() # Setup
t.goto(-250, -90)
t.pendown() # Base
t.forward(125)
t.penup()
t.left(180)
t.forward(62.5)
t.right(90)
t.pendown() # Height
t.forward(250)
t.right(90)
t.forward(175) # Top part
t.right(90)
t.forward(25) # Hook
t.right(90)
t.penup()

# Word list
fourlw = ["book", "pure", "team", "foot", "hand", "lamp", "horn", "ball", "card", "cube", "food"]
fivelw = ["sport", "drive", "robot", "award", "stand", "water", "spray", "piano", "clock", "phone", "light"]
sixlw = ["closet", "trophy", "bottle", "guitar", "pillow", "school", "member", "window", "python", "jacket", "basket"]
sevenlw = ["monitor", "blanket", "stapler", "history", "science", "algebra", "trumpet", "chicken", "curtain", "library", "grocery"]

wordlist = random.randint(4, 7) # update this and add another if statement if another set is added
if wordlist == 4: # Choose random four-letter word
    word = fourlw[random.randint(0, 10)] # Update if more words are added
    clue = list("????")
    print(clue)
if wordlist == 5: # Choose random five-letter word
    word = fivelw[random.randint(0, 10)] # Update if more words are added
    clue = list("?????")
    print(clue)
if wordlist == 6: # Choose random six-letter word
    word = sixlw[random.randint(0, 10)] # Update if more words are added
    clue = list("??????")
    print(clue)
if wordlist == 7: # Choose random seven-letter word
    word = sevenlw[random.randint(0, 10)] # Update if more words are added
    clue = list("???????")
    print(clue)

lives = 6
while lives != 0:
    guess = input("Guess a letter, or the whole word: ")
    if guess == word: # Done if guessed word is correct
        print("Correct!")
        break
    elif guess in word: # Update clue if guessed letter is in the word
        space = 0
        while space < len(word):
            if guess == word[space]:
                clue[space] = guess
            space += 1
        if clue == list(word):
            print("Correct!")
            break
        else:
            print(clue)        
    else: # Done if guessed letter or word is incorrect
        if lives == 6: # Head
            drawPart("circle", 35, 270, 70)
        elif lives == 5: # Body
            drawPart("line", 100, 180, 62.5)
            t.left(90)
        elif lives == 4: # Left Arm
            drawPart("line", 62.5, 180, 62.5)
        elif lives == 3: # Right Arm
            drawPart("line", 62.5, 180, 62.5)
            t.left(90)
            t.forward(62.5)
            t.right(45)
        elif lives == 2: # Left Leg
            drawPart("line", 62.5, 180, 62.5)
            t.right(90)
        else: # Right Leg
            drawPart("line", 62.5, 0, 0)
            print(f"Game over! The word was {word}")
            break
        lives -= 1