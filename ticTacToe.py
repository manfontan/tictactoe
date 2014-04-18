import pygame,sys,random,time
from pygame.locals import *
from pygame.pixelarray import PixelArray


class Gameboard:

    def __init__(self,surface):
        self.box = ["","","","","","","","",""]
        self.surface = surface

    def draw(self):
        x = y = 0
        self.surface.fill((255,255,255))
        for i in range(0,3):
            for j in range(0,3):
                pygame.draw.rect(self.surface,(0,0,0),Rect((x,y),(50,50)),1)
                x += 50
            x = 0
            y += 50
            
    def insert(self):
        width = {0:25,1:75,2:125,3:25,4:75,5:125,6:25,7:75,8:125}
        height = {0:25,1:25,2:25,3:75,4:75,5:75,6:125,7:125,8:125}
        for i in range(0,9):
            if self.box[i] == "X":
                pygame.draw.aaline (self.surface, (0, 0, 0), (width[i]-10,height[i]-10), (width[i]+10,height[i]+10), 1)
                pygame.draw.aaline (self.surface, (0, 0, 0), (width[i]-10,height[i]+10), (width[i]+10,height[i]-10), 1)
            if self.box[i] == "O":
                pygame.draw.circle(self.surface,(0,0,0),(width[i],height[i]),10)
                pygame.draw.circle(self.surface,(255,255,255),(width[i],height[i]),9)

    def move(self,x,y):
        if x > 0 and x < 50:
            if y > 0 and y < 50:
                if self.box[0] == "":
                    self.box[0] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[3] == "":
                    self.box[3] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[6] == "":
                    self.box[6] = "O"
                    return True
            return False

        elif x > 50 and x < 100:
            if y > 0 and y < 50:
                if self.box[1] == "":
                    self.box[1] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[4] == "":
                    self.box[4] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[7] == "":
                    self.box[7] = "O"
                    return True
            return False

        elif x > 100 and x < 150:
            if y > 0 and y < 50:
                if self.box[2] == "":
                    self.box[2] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[5] == "":
                    self.box[5] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[8] == "":
                    self.box[8] = "O"
                    return True
            return False
        
        return False
            
    def check(self):
        if self.box[0] == "X" and self.box[1] == "X" and self.box[2] == "X": return True,"C"
        elif self.box[3] == "X" and self.box[4] == "X" and self.box[5] == "X": return True,"C"
        elif self.box[6] == "X" and self.box[7] == "X" and self.box[8] == "X": return True,"C"

        elif self.box[0] == "X" and self.box[3] == "X" and self.box[6] == "X": return True,"C"
        elif self.box[1] == "X" and self.box[4] == "X" and self.box[7] == "X": return True,"C"
        elif self.box[2] == "X" and self.box[5] == "X" and self.box[8] == "X": return True,"C"

        elif self.box[0] == "X" and self.box[4] == "X" and self.box[8] == "X": return True,"C"
        elif self.box[6] == "X" and self.box[4] == "X" and self.box[2] == "X": return True,"C"


        if self.box[0] == "O" and self.box[1] == "O" and self.box[2] == "O": return True,"P"
        elif self.box[3] == "O" and self.box[4] == "O" and self.box[5] == "O": return True,"P"
        elif self.box[6] == "O" and self.box[7] == "O" and self.box[8] == "O": return True,"P"

        elif self.box[0] == "O" and self.box[3] == "O" and self.box[6] == "O": return True,"P"
        elif self.box[1] == "O" and self.box[4] == "O" and self.box[7] == "O": return True,"P"
        elif self.box[2] == "O" and self.box[5] == "O" and self.box[8] == "O": return True,"P"
        
        elif self.box[0] == "O" and self.box[4] == "O" and self.box[8] == "O": return True,"P"
        elif self.box[6] == "O" and self.box[4] == "O" and self.box[2] == "O": return True,"P"

        return False,"N"

class Machine:

    def __init__(self,gameboard):
        self.gameboard = gameboard
        self.move = None

    def attack(self):
        self.aimove("X")

    def defend(self):
        self.aimove("O")

    def do(self):
        if self.move == None: self.randomove()
        elif self.gameboard.box[self.move] != "": self.randomove()
        else: self.gameboard.box[self.move] = "X"
        self.move = None

    def randomove(self):
        while 1:
            move = random.randint(0,8)
            if self.gameboard.box[move] == "":
                self.gameboard.box[move] = "X"
                break        

    def aimove(self,simbol):
        if self.gameboard.box[0] == simbol and self.gameboard.box[1] == simbol and self.gameboard.box[2] == "": self.move = 2
        elif self.gameboard.box[0] == simbol and self.gameboard.box[1] == "" and self.gameboard.box[2] == simbol: self.move = 1
        elif self.gameboard.box[0] == "" and self.gameboard.box[1] == simbol and self.gameboard.box[2] == simbol: self.move = 0

        if self.gameboard.box[3] == simbol and self.gameboard.box[4] == simbol and self.gameboard.box[5] == "": self.move = 5
        elif self.gameboard.box[3] == simbol and self.gameboard.box[4] == "" and self.gameboard.box[5] == simbol: self.move = 4
        elif self.gameboard.box[3] == "" and self.gameboard.box[4] == simbol and self.gameboard.box[5] == simbol: self.move = 3

        if self.gameboard.box[6] == simbol and self.gameboard.box[7] == simbol and self.gameboard.box[8] == "": self.move = 8
        elif self.gameboard.box[6] == simbol and self.gameboard.box[7] == "" and self.gameboard.box[8] == simbol: self.move = 7
        elif self.gameboard.box[6] == "" and self.gameboard.box[7] == simbol and self.gameboard.box[8] == simbol: self.move = 6
        
        if self.gameboard.box[0] == simbol and self.gameboard.box[3] == simbol and self.gameboard.box[6] == "": self.move = 6
        elif self.gameboard.box[0] == simbol and self.gameboard.box[3] == "" and self.gameboard.box[6] == simbol: self.move = 3
        elif self.gameboard.box[0] == "" and self.gameboard.box[3] == simbol and self.gameboard.box[6] == simbol: self.move = 0

        if self.gameboard.box[1] == simbol and self.gameboard.box[4] == simbol and self.gameboard.box[7] == "": self.move = 7
        elif self.gameboard.box[1] == simbol and self.gameboard.box[4] == "" and self.gameboard.box[7] == simbol: self.move = 4
        elif self.gameboard.box[1] == "" and self.gameboard.box[4] == simbol and self.gameboard.box[7] == simbol: self.move = 1

        if self.gameboard.box[2] == simbol and self.gameboard.box[5] == simbol and self.gameboard.box[8] == "": self.move = 8
        elif self.gameboard.box[2] == simbol and self.gameboard.box[5] == "" and self.gameboard.box[8] == simbol: self.move = 5
        elif self.gameboard.box[2] == "" and self.gameboard.box[5] == simbol and self.gameboard.box[8] == simbol: self.move = 2

        if self.gameboard.box[0] == simbol and self.gameboard.box[4] == simbol and self.gameboard.box[8] == "": self.move = 8
        elif self.gameboard.box[0] == simbol and self.gameboard.box[4] == "" and self.gameboard.box[8] == simbol: self.move = 4
        elif self.gameboard.box[0] == "" and self.gameboard.box[4] == simbol and self.gameboard.box[8] == simbol: self.move = 0

        if self.gameboard.box[2] == simbol and self.gameboard.box[4] == simbol and self.gameboard.box[6] == "": self.move = 6
        elif self.gameboard.box[2] == simbol and self.gameboard.box[4] == "" and self.gameboard.box[6] == simbol: self.move = 4
        elif self.gameboard.box[2] == "" and self.gameboard.box[4] == simbol and self.gameboard.box[6] == simbol: self.move = 2
    
def run(ai,gameboard,screen):
    win = False
    player = True
    winner = ""

    while win is not True:

        ok = False

        screen.fill((0,0,0))
        gameboard.draw()
        gameboard.insert()

        if player is not True:
            ai.attack()
            if ai.move == None:
                ai.defend()
                ai.do()
            else: ai.do()        
            player = True
    
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player:
                        if gameboard.move(event.pos[0],event.pos[1]):
                            player = False
        
        for i in gameboard.box: 
            if  i == "":
                ok = True
                break 
          
        win,winner = gameboard.check()

        if ok == False: 
            win = True
            winner = "N"
    
        pygame.display.update()
    return winner    


pygame.init()
screen = pygame.display.set_mode((150,150))
pygame.display.set_caption("TicTacToe")
font = pygame.font.SysFont("arial",20)

while 1:
    gameboard = Gameboard(screen)
    ai = Machine(gameboard)
    Winner = run(ai,gameboard,screen)

    if Winner == "C":
        screen.fill((255,255,255))
        text = font.render("You Lose!!!",True,(0,0,0))
        screen.blit(text,(37,37+font.get_linesize()))
        pygame.display.update()
    elif Winner == "P":
        screen.fill((255,255,255))
        text = font.render("You Win!!!",True,(0,0,0))
        screen.blit(text,(37,37+font.get_linesize()))
        pygame.display.update()
    elif Winner == "N":
        screen.fill((255,255,255))
        text = font.render("Tie...",True,(0,0,0))
        screen.blit(text,(37,37+font.get_linesize()))
        pygame.display.update()

    time.sleep(3)