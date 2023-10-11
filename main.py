from random import Random
import pygame as py
import sys
from pygame import mouse
from pygame.locals import *
from Data.objects import *
from Data.window import *
from Data.player import *
from pygame import mixer

py.init()
# Imported all the required modules


# The main Hub that controls over all program
# It controls from Running the game to Exiting It !
# Helps to Keep Window , players and objects in good condition and Displaying them

if __name__ == "__main__":
    # The above Lines check if the code if run from main.py or not
    # If not then code doesn't run but if yes the codes Below will run!

    MrRock = Rock()
    MrShards = Shards()
    MrCoin = Coins()
    # MrCursor = Cursor()

    def MrRockControls():
        # Defining and Controling all the function from other modules related to player here
        if MrRock.Score < 2000:
            py.display.set_icon(Screen.Icon)
        MrRock.Display()
        MrRock.Coordinates()
        MrRock.ScoreDealing()
        MrRock.Jumping()
        MrRock.Moving()
        MrRock.Boosting()

    # def ForGodplayer():
    #     if MrRock.Score >= 2000:

    #         GodLevel = MrRock.Myfont.render(
    #             "Your are a god !", True, (255, 10, 10))
    #         Screen.MainScreen.blit(GodLevel, (450, 0))
    #         Screen.Title = "Your are god Level!"
    #         py.display.set_icon(Screen.IconGod)
    #         MrCoin.Amount = 1000

    def ShardsControls():
        MrShards.Display()
        if MrRock.Health >= 0:
            if MrRock.RectRock.colliderect(MrShards.MainRect):
                MrShards.XAxix = random.randint(0, 545)
                MrShards.YAxix = -3
                if Screen.Start == False:
                    MrRock.Health -= MrShards.Damage

        elif MrRock.Health <= 0 and Screen.Start == False:
            MrShards.Velocity = 0
            MrRock.RunningRock = False

    def CoinControls():
        MrCoin.Display()
        if MrRock.Health >= 0:
            if MrRock.RectRock.colliderect(MrCoin.MainRect):
                MrCoin.Sound.play()
                MrCoin.XAxix = random.randint(0, 545)
                MrCoin.YAxix = -3
                if Screen.Start == False:
                    MrRock.Score += MrCoin.Amount
                    if MrRock.Score == 100:
                        MrShards.Damage = 20
                        MrCoin.Amount = 20
                        MrShards.Velocity += 3
                    elif MrRock.Score == 500:
                        MrShards.Damage = 30
                        MrCoin.Amount = 50
                        MrShards.Velocity += 5
                    elif MrRock.Score == 1000:
                        MrShards.Damage = 45
                        MrShards.Velocity += 8
                        MrCoin.Amount = 100

        elif MrRock.Health <= 0 and Screen.Start == False:
            MrCoin.Velocity = 0
            MrRock.RunningRock = False

    # def CursorControls():
    #     MrCursor.Display()

    def Exit():
        if MrRock.Health <= 0:
            MrRock.RunningRock = False
            MrCoin.Velocity = 0
            MrShards.Velocity = 0
            MrRock.Velocity = 0
            Screen.MainScreen.blit(Screen.BlackLayer, (0, 0))
            MrRock.Coordinates()
            Screen.MainScreen.blit(Screen.ExitButton, (245, 225))
            MainMouse = py.mouse.get_pos()
            MainMouseRect = py.Rect(MainMouse[0], MainMouse[1], 20, 20)

            if (
                MainMouseRect.colliderect(Screen.ExitButtonRect)
                and py.mouse.get_pressed()[0]
            ):

                Screen.Running = False

    def Mainloop():
        # The main loop helping to run and exit the Game!

        while Screen.Running:
            for Event in py.event.get():
                if Event.type == py.QUIT:
                    Screen.Running = False

            Screen.Display()
            Screen.Clock()


            ShardsControls()
            MrRockControls()
            CoinControls()

            Screen.Starmenu()
            # CursorControls()
            # ForGodplayer()
            Exit()
            py.display.update()

        py.quit()
        # The program has been Exited : Terminal!

    Mainloop()
