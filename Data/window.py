import pygame as py
from pygame.locals import *

py.init()

# Class for the Window and working with the overall properties of the Window
# Helps alot to Display BackGround ,Platform ,Icon and Title for the Game


class Window:
    # Initilizing the properties for the window

    def __init__(self) -> None:
        self.SizeX = 600
        self.SizeY = 500
        self.Icon = py.image.load("images/background/Icon.png")
        self.IconGod = py.image.load("images/background/ForGod.png")
        self.Platform = py.image.load(
            "images/background/BackGround02.png"
        )
        self.BackGround = py.image.load(
            "images/background/BackGround03.png"
        )
        self.BlackLayer = py.image.load("images/background/Darkner.png")
        self.ExitButton = py.image.load("images/background/Exit.png")
        self.StartButton = py.image.load("images/background/Start.png")
        self.ScoreBoard = py.image.load(
            "images/background/ScoreBoard.png"
        )
        self.BoostBoard = py.image.load(
            "images/background/BoostBoard.png"
        )
        self.ControlsBox = py.image.load("images/background/Controls.png")
        self.Title = "Aruson"
        self.Running = True
        self.MainScreen = py.display.set_mode((self.SizeX, self.SizeY))
        self.FPS = 120
        self.ExitButtonRect = py.Rect(245, 225, 120, 26)
        self.Start = True
        self.RectStart = py.Rect(245, 225, 120, 26)
        self.MainMouse = py.mouse.get_pos()
        self.MainMouseRect = py.Rect(self.MainMouse[0], self.MainMouse[1], 20, 20)
        self.ShowIntro = True
        self.IntroBoard = py.image.load(
            "images/background/Introduction.png"
        )
        self.IntroRect = py.Rect(0, 0, 600, 500)

    def Display(self):
        # Displaying the Main Window with the use of the properties from Above!

        self.MainScreen.blit(self.BackGround, (0, 0))
        self.MainScreen.blit(self.Platform, (0, 432))
        self.MainScreen.blit(self.ScoreBoard, (0, 0))
        # self.MainScreen.blit(self.BoostBoard, (0, 26))
        py.display.set_caption(self.Title)

    def Clock(self):
        # The Fps limiter helps to Keep Fps constant!

        MyClock = py.time.Clock()
        MyClock.tick(self.FPS)

    def Starmenu(self):

        self.MainMouse = py.mouse.get_pos()
        self.MainMouseRect = py.Rect(self.MainMouse[0], self.MainMouse[1], 20, 20)

        if self.Start == True:
            self.MainScreen.blit(self.BlackLayer, (0, 0))
            self.MainScreen.blit(self.StartButton, (self.RectStart.x, self.RectStart.y))
            self.MainScreen.blit(self.ControlsBox,(0,0))

            if (
                self.MainMouseRect.colliderect(self.RectStart)
                and py.mouse.get_pressed()[0]
            ):
                self.Start = False


Screen = Window()
