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

    all_coins = [Coins() , Coins() , Coins() , Coins()]
    all_shards = [Shards() , Shards() , Shards() , Shards()]

    MrShards = Shards()
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
    def Exit():

        for shards in all_shards :
            for coins in all_coins:
        
                if MrRock.Health <= 0:
                    MrRock.RunningRock = False
                    coins.Velocity = 0
                    shards.Velocity = 0
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

    def ShardsControls():

        for shards in all_shards:
            shards.Display()
        

            if MrRock.Health >= 0:
                if MrRock.RectRock.colliderect(shards.MainRect):
                    shards.XAxix = random.randint(0, random.randint(0,545))
                    shards.YAxix = random.randint(-64, random.randint(-32,-1))
                    if Screen.Start == False:
                        MrRock.Health -= shards.Damage
                
                Exit()

            elif MrRock.Health <= 0 and Screen.Start == False:
                shards.Velocity = 0
                MrRock.RunningRock = False

    def CoinControls():

        for coins in all_coins:
            coins.Display()

            if MrRock.Health >= 0:
                if MrRock.RectRock.colliderect(coins.MainRect):
                    coins.Sound.play()
                    coins.XAxix = random.randint(0, random.randint(0,545))
                    coins.YAxix = random.randint(-64, random.randint(-32,-1))
                    
                    if Screen.Start == False:
                        MrRock.Score += coins.Amount

                        if MrRock.Score == 100:
                            coins.Amount = 20
                            
                        elif MrRock.Score == 500:
                            coins.Amount = 50    

                        elif MrRock.Score == 1000:
                            coins.Amount = 100

            elif MrRock.Health <= 0 and Screen.Start == False:
                coins.Velocity = 0
                MrRock.RunningRock = False

    # def CursorControls():
    #     MrCursor.Display()


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
