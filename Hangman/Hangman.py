import random
import pygame
import math

pygame.init()
WIDTH , HEIGHT = 800,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman")

#btn variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS*2 + GAP)*13)/2)
start_y = 400
A = 65

for i in range(26):
    x = start_x + GAP*2 + (RADIUS*2 + GAP)*(i%13)
    y = start_y + ((i//13)*(GAP + RADIUS*2))
    letters.append([x,y,chr(A + i),True])

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#images
images = []
for i in range(7):
    img = pygame.image.load("hangman" + str(i)+ ".png")
    images.append(img)

#image game variables
hangman_status = 0
words = ["SURI","VAHINI","ASEESH","MANOHAR"]
guess = []
word = random.choice(words)

#fonts
LETTER_FONT = pygame.font.SysFont("sans-serif", 40)
WORD_FONT = pygame.font.SysFont("sans-serif", 60)
TITLE_FONT = pygame.font.SysFont("sans-serif", 70)

FPS = 1
clock = pygame.time.Clock()
run = True

def draw():
    WIN.fill((WHITE))

    #draw title
    text = TITLE_FONT.render("Hangman Game",1,BLACK)
    WIN.blit(text,(WIDTH//2 - text.get_width()//2,20))

    #draw word
    display_word = ""
    
    for letter in word:
        if letter in guess:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    WIN.blit(text,(400,200))
    
    #draw btns
    for letter in letters:
        x,y,LTR,visible = letter
        if visible:
            pygame.draw.circle(WIN,BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(LTR, 1,BLACK)
            WIN.blit(text,(x-text.get_width()//2,y-text.get_height()//2))

    WIN.blit(images[hangman_status],(150,100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    WIN.fill(WHITE)
    text = WORD_FONT.render(message,1,BLACK)
    WIN.blit(text,(WIDTH//2 - text.get_width()//2,HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x , y , ltr , visible = letter
                if visible:
                    dis = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guess.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()
    won = True
    for letter in word:
        if letter not in guess:
            won = False
            break       
    if won:
        display_message("Great guess...You Won!")
        break
        
    if hangman_status == 6:
        display_message("Opps...You Lost!")
        break
             
pygame.quit()