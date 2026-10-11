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