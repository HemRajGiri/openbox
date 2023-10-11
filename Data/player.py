import pygame as py
from pygame.locals import *
from Data.window import *
from Data.objects import *

py.init()
# imported all the files required

# This is the modules that controls all the properties and controls of the Rock(Main player)
# This also controls Properties of the Rock too!


class Rock:
    def __init__(self):
        # Initizing the values for the rock Object and Obstacle

        self.image = [
            py.image.load("images/player/InitialRock.png"),
            py.image.load("images/player/Moving.png"),
            py.image.load("images/player/Moving2.png"),
            py.image.load("images/player/Moving3.png"),
        ]
        self.Myfont = py.font.Font("prompt/Prompt-Light.ttf", 11)

        self.power_icons = [
            py.image.load("images/player/jump.png"),
            py.image.load("images/player/boost.png")
        ]


        self.FallSound = py.mixer.Sound("audio/FallingRock.mp3")
        self.X = 285
        self.Y = 402
        self.Velocity = 4
        self.RunningRock = True
        self.Change = 1
        self.JumpCount = 6
        self.DoJump = False
        self.FontColour = (255, 255, 255)
        self.Score = 0
        self.Health = 10
        self.RectRock = py.Rect(self.X, self.Y, 32, 32)
        self.Running = True
        self.Angle = 0
        self.initialScore = 20
        self.BoostDetect = " "

    def Display(self):
        # Displaying the Rock and the obstacle
        Screen.MainScreen.blit(self.image[int(self.Change)], (self.X, self.Y))

    def Moving(self):
        # Defines the Controls and movement of the rock
        if self.RunningRock == True:
            if py.key.get_pressed()[K_d] and self.X <= 600 - 32:
                self.X += self.Velocity
                self.Change += self.Velocity // 4
                if self.Change > 3:
                    self.Change = 0

            elif py.key.get_pressed()[K_a] and self.X >= 0:
                self.X -= self.Velocity
                self.Change -= self.Velocity // 4
                if self.Change < 0:
                    self.Change = 3

    def Jumping(self):
        # Defining the Jumping function for the Rock
        if self.RunningRock == True:
            if py.key.get_pressed()[K_SPACE] and self.Score >= 100:
                self.DoJump = True
            if self.Score >= 100 and self.Score < 2000:
                small_icon = py.transform.scale(self.power_icons[0],(24,24))
                Screen.MainScreen.blit(small_icon, (13, 460))
                if self.Score == 120:
                    self.ShowSpaceBar = False

            if self.DoJump == True:

                if self.JumpCount >= -6:
                    Negative = 1

                    if self.JumpCount < 0:
                        Negative = -1

                    self.Y -= (self.JumpCount ** 2) * Negative
                    self.Velocity = 5
                    self.JumpCount -= 1
    
                else:
                    self.DoJump = False
                    self.JumpCount = 6
                    self.Velocity = 5

    def Boosting(self):
        if py.key.get_pressed()[K_LSHIFT] and self.Score >= 220:
            self.BoostDetect = "Boosted!"
            self.Velocity = 13

        else:
            self.Velocity = 4

    def Coordinates(self):
        # Rendering Position of Rock

        self.RectRock = py.Rect(self.X, self.Y, 32, 32)
        self.Myfont = py.font.Font("prompt/Prompt-Bold.ttf", 20)
        # PosText = self.Myfont.render(f"Pos : {self.X,self.Y}", True, self.FontColour)
        # Screen.MainScreen.blit(PosText, (0, 0))

        # Render the score Board
        Screen.MainScreen.blit(Screen.ScoreBoard, (0, 0))
        ScoreText = self.Myfont.render(f"{self.Score:}", True, self.FontColour)
        Screen.MainScreen.blit(ScoreText, (100, 1))

        # HealthText = self.Myfont.render(
        #     f"Health : {self.Health}", True, self.FontColour
        # )
        # Screen.MainScreen.blit(HealthText, (0, 26))

        # ScoreText = self.Myfont.render(
        #     f"Velocity : {self.Velocity:}", True, self.FontColour
        # )
        # Screen.MainScreen.blit(ScoreText, (0, 26))

        # ScoreText = self.Myfont.render(f"{self.BoostDetect:}", True, self.FontColour)
        # Screen.MainScreen.blit(ScoreText, (64, 32))
        if self.Score >= 220 and self.Health >= 10  and self.Score < 2000:
            small_icon = py.transform.scale(self.power_icons[1],(24,24))
            Screen.MainScreen.blit(small_icon, (46, 460))
            if self.Score == 240:
                self.ShowShiftBar = False

    def ScoreDealing(self):
        # Securing score if the mouse collides with the Rock

        if py.mouse.get_pos() == (self.X, self.Y):
            self.Score += 1


MrRock0 = Rock()
