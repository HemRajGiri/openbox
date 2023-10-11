import pygame as py
import random
from pygame import display
from pygame.locals import *
from Data.window import *
from Data.player import *
from pygame import mixer
py.init()


class Shards(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Image = [
            py.image.load("images/objects/Shards/Shards.png"),
            py.image.load("images/objects/Shards/ShardsMove1.png"),
            py.image.load("images/objects/Shards/ShardsMove2.png"),
            py.image.load("images/objects/Shards/ShardsMove3.png"),
            py.image.load("images/objects/Shards/ShardsMove3.png"),
            py.image.load("images/objects/Shards/ShardsMove2.png"),
            py.image.load("images/objects/Shards/ShardsMove1.png"),
            py.image.load("images/objects/Shards/Shards.png"),
        ]
        self.XAxix = 200
        self.YAxix = -32
        self.MainRect = py.Rect(self.XAxix, self.YAxix, 32, 32)
        self.Velocity = 3
        self.Grouping = py.sprite.Group()
        self.Damage = 10
        self.Change = 0

    def Display(self):
        if self.YAxix < 400:
            Screen.MainScreen.blit(self.Image[self.Change], (self.XAxix, self.YAxix))
            self.YAxix += self.Velocity
            self.Change += 1
            if self.Change > 7:
                self.Change = 0

        else:
            self.XAxix = random.randint(0, 545)
            self.YAxix = -32

        self.MainRect = py.Rect(self.XAxix, self.YAxix, 32, 32)


MrShards = Shards()


class Coins(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Image = [
            py.image.load("images/objects/Coins/Coin.png"),
            py.image.load("images/objects/Coins/Coin1.png"),
            py.image.load("images/objects/Coins/Coin2.png"),
            py.image.load("images/objects/Coins/Coin3.png"),
            py.image.load("images/objects/Coins/Coin4.png"),
            py.image.load("images/objects/Coins/Coin5.png"),
            py.image.load("images/objects/Coins/Coin.png"),
        ]
        self.XAxix = 350
        self.YAxix = -32
        self.MainRect = py.Rect(self.XAxix, self.YAxix, 16, 16)
        self.Velocity = 3
        self.Amount = 10
        self.Change = 0
        self.Sound = py.mixer.Sound("audio/Coin.mp3")

    def Display(self):
        if self.YAxix < 400 and not self.MainRect.colliderect(MrShards.MainRect): 
            Screen.MainScreen.blit(
                self.Image[int(self.Change)], (self.XAxix, self.YAxix)
            )
            self.YAxix += self.Velocity
            self.Change += 1
            if self.Change > 6:
                self.Change = 0

        else:
            self.XAxix = random.randint(0, 545)
            self.YAxix = -3
            if Screen.Start == False and self.Velocity < 13 and MrRock0.Score >= 100:
                self.Velocity += 1

        self.MainRect = py.Rect(self.XAxix, self.YAxix, 32, 32)


# class Cursor(py.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.Image = py.image.load("images/buttons/Cursor.png")
#         self.MousePos = py.mouse.get_pos()
#         self.MainRect = py.Rect(self.MousePos[0], self.MousePos[1], 32, 32)

#     def Display(self):
#         py.mouse.set_visible(False)
#         self.MousePos = py.mouse.get_pos()
#         self.MainRect = py.Rect(self.MousePos[0], self.MousePos[1], 16, 16)
#         if (
#             self.MainRect.x > 0
#             and self.MainRect.y > 0
#             and self.MainRect.x < 598
#             and self.MainRect.y < 496
#         ):
#             self.MousePos = py.mouse.get_pos()
#             self.MainRect = py.Rect(self.MousePos[0], self.MousePos[1], 16, 16)
#             Screen.MainScreen.blit(
#                 self.Image, (self.MainRect.x - 7, self.MainRect.y - 5)
#             )
