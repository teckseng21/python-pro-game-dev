import pygame
import random
import sys

pygame.init()

WIDTH=500
HEIGHT=750

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wordle")

clock=pygame.time.Clock()
FPS=60
BG=(18,18,19)
EMPTY=(58,58,60)
GREEN=(83,141,78)
YELLOW=(181,159,59)
GRAY=(120,124,126)
DARK_GRAY=(80,80,80)
WHITE=(255,255,255)
BUTTON=(70,130,180)
BLACK=(0,0,0)

ROWS=6
COLS=5
TILE_SIZE=60
GAP=8

title_font=pygame.font.SysFont("arial", 50,bold=True)
start_title_font=pygame.font.SysFont("arial", 60,bold=True)
letter_font=pygame.font.SysFont("arial", 35,bold=True)
keyboard_font=pygame.font.SysFont("arial", 18,bold=True)
message_font=pygame.font.SysFont("arial", 25,bold=True)
button_font=pygame.font.SysFont("arial", 25,bold=True)
small_font=pygame.font.SysFont("arial", 20)

def load_words():
    try:
        with open("words.txt", "r") as file:
            loaded_words=[]

            for line in file:
                word=line.strip().upper()

            if len(word)==5 and word.isalpha():
                loaded_words.append(word)

        if len(loaded_words)==0:
            raise ValueError("No valid five-letter words found.")
        return loaded_words

    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        print("Place words.txt in the same folder as wordle.py")
        pygame.quit()
        sys.exit()

    except ValueError as error:
        print("Error",error)
        pygame.quit()
        sys.exit()
words=load_words()
game_state="start"

start_button=pygame.Rect(150,300,200,60)
play_again_button=pygame.Rect(150,680,200,50)

grid=[]
colors=[]
current_row=0
current_col=0
secret_word=""
message=""
key_colors={}
keylayout=[
        list("QWERTYUIOP"),
        list("ASDFGHJKL"),
        ["ENTER"]+list("ZXCVBNM")+["BACK"],
    ]

key_rects=[]

def create_keyboard():
    key_rects.clear()

    y_start=500

    for row_index,row in enumerate(keylayout):
        key_widths=[]

        for key in row:
            if key=="ENTER" or key=="BACK":
                key_widths.append(65)
            else:
                key_widths.append(40)

        total_width=sum(key_widths)+(len(row)-1)*5
        x_start=(WIDTH-total_width)//2

        x=x_start

        for key, width in zip(row,key_widths):
            rect=pygame.Rect(x,y_start+row_index*55,width,45)

            key_rects.append((rect,key))
            x +=width+5

def init_game():
    global grid,colors
    global current_row,current_col
    global secret_word,message,key_colors

    grid=[["" for _ in range(COLS)]for _ in range(ROWS)]

    colors=[[EMPTY for _ in range(COLS)]for _ in range(ROWS)]

    current_row=0
    current_col=0

    secret_word=random.choice(words)
    message=""
    key_colors={}

def draw_text(text,font,color,center):
    image=font.render(str(text),True,color)
    rect=image.get_rect(center=center)
    screen.blit(image,rect)

def draw_button(rect,text,font):
    pygame.draw.rect(screen,BUTTON,rect, border_radius=8)
    pygame.draw.rect(screen,WHITE,rect,2,border_radius=8)

    draw_text(text,font,WHITE,rect.center)

def draw_start_screen():
    screen.fill(BG)
    
    draw_text("WORDLE",start_title_font,WHITE,(WIDTH//2,200))

    draw_text("Guess the wordle in 6 tries",small_font,WHITE,(WIDTH//2,250))
    
    draw_button(start_button,"START",button_font)

def draw_grid():
    grid_width=COLS*TILE_SIZE+(COLS-1)*GAP
    x_start=(WIDTH-grid_width)//2

    for r in range(ROWS):
        for c in range(COLS):

            x=x_start+c*(TILE_SIZE+GAP)
            y=80+r*(TILE_SIZE+GAP)

            rect=pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
            pygame.draw.rect(screen,colors[r][c],rect,border_radius=4)

            if grid[r][c]!="":
                pygame.draw.rect(screen,GRAY,rect,2,border_radius=4)

            if grid[r][c]!="":
                draw_text(grid[r][c],letter_font,WHITE,rect.center)

def draw_keyboard():
    for rect,key in key_rects:
        color=key_colors.get(key,GRAY)

        pygame.draw.rect(screen,color,rect,border_radius=5)
        pygame.draw.rect(screen,WHITE,rect,2,border_radius=5)

        draw_text(key,keyboard_font,WHITE,rect.center)

def draw_game_screen():
    screen.fill(BG)
    draw_text("WORDLE",title_font,WHITE,(WIDTH//2,30))
    draw_grid()
    draw_text("WORDLE",message_font,WHITE,(WIDTH//2,460))
    draw_keyboard()
    if game_state=="game_over":
        draw_button(play_again_button,"PLAY AGAIN",button_font)

def update_key_color(letter,color):
    current=key_colors.get(letter,)

    if current==GREEN:
        return

    if current==YELLOW and color==DARK_GRAY:
        return

    key_colors[letter]=color

def check_word():
    global current_row,current_col,game_state, message

    guess="".join(grid[current_row])
    secret_list=list(secret_word)

    for i in range(COLS):
        if guess[i]==secret_word[i]:
            colors[current_row][i]=GREEN
            secret_list[i]=None
            update_key_color(guess[i],GREEN)

    for i in range(COLS):
        if colors[current_row][i]==GREEN:
            continue

        if guess[i] in secret_list:
            colors[current_row][i]=YELLOW

            index=secret_list.index(guess[i])
            secret_list[index]=None
            update_key_color(guess[i],YELLOW)

        else:
            colors[current_row][i]=DARK_GRAY
            update_key_color(guess[i],DARK_GRAY)

    if guess==secret_word:
        message="Congratulations!"
        game_state="gameover"
        return

    current_row +=1
    current_col=0

    if current_row==ROWS:
        message="The word was: {secret_word}"
        game_state="gameover"

    else:
        message=""

def handle_key(key):
    global current_col,message

    if game_state!="playing":
        return

    if key=="ENTER":

        if current_col==COLS:
            check_word()
        else:
            message="Not enough letters"

    elif key=="BACK":

        if current_col>0:
            current_col -=1
            grid[current_row][current_col]=""

        message=""

    else:
        if current_col<COLS:
            grid[current_row][current_col]=key
            current_col +=1
            message=""

create_keyboard()
init_game() 

running=True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pos=event.pos

                if game_state =="start":
                    if start_button.collidepoint(pos):
                        game_state="playing"

                elif game_state=="playing":
                    for rect,key in key_rects:
                        if rect.collidepoint(pos):
                            handle_key(key)
                            break

                elif game_state=="gameover":
                    if play_again_button.collidepoint(pos):
                        init_game()
                        game_state="playing"

        elif event.type==pygame.KEYDOWN:
            if game_state=="playing":
                if event.key==pygame.K_RETURN:
                    handle_key("ENTER")

                elif event.key==pygame.K_BACKSPACE:
                    handle_key("BACK")

                elif pygame.K_a <= event.key <= pygame.K_z:
                    letter=event.unicode.upper()

                    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        handle_key(letter)

    if game_state=="start":
        draw_start_screen()

    else:
        draw_game_screen()

    pygame.display.flip()

pygame.quit()
sys.exit()
                    
