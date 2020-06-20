from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
BACKGROUND_COLOR = "#FFFFFF"
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30
PLATFORM_COLOR = "#654321"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
Rect = bg.get_rect()


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color("#654321"))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


level = [
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"---0000000000000000000000000-00000000000000000000000000000000---",
"---0000000000000000000000000000000000000000000000000000000000---",
"---0---------------000000000000000-00000000000--0000000000------",
"---00000000-0000000--000000000-000-0-000000000000-------00000---",
"---00000000-0000000000--000000-0-0-0-0000000-0000000000000000---",
"----0000000-000000000000000------------000000-000000000000000---",
"---00000000-----------00--00000000000000-0000-0000000-----00----",
"---0------00000000000000-000000000000000000000-00-00000000000---",
"---000000000000000000000-00000000000000-00000000000-0000000-----",
"---000000000000000000000000-------------00000000-000000000000---",
"---0------------------000-000000000000000000000-0000000000------",
"---0000000000000000000000-00000000000000000000-0000000--00000---",
"---0000000000000000000000-----------------000-000000000000000---",
"-------------------------0000000000000000000-00000000000-0000---",
"---000000000000000000000000000000000000000-----------------00---",
"---000000000000000000000000000000000000000000000000000000000----",
"---0000000000000000000000000000000000000000000000000000000000---",
"---00000000000000000000-000000000000---00-----------------------",
"---000------------00000000----------0000000000000000000000000---",
"----0000000000000-0-0000-000000000000000000000000000000000000---",
"-----000000000000-0000000000000000000000000000000000000000000---",
"------00000000000-0000000-0000000000000-0---00000000000000000---",
"---00000000000000-000-000000000--------0000-00000000000000000---",
"---000----0000000-00000000-0000000000000000-----0-0--0-----00---",
"---000--------000-000000000000000000000000000000000000000000----",
"---000000000000---0-0000000-0000-0-0000--00000000000000000000---",
"---000000000000---0000000000---00000--000000000000000000000-----",
"---0000000--------000000000000000000--000-0000000000000000------",
"---0000000--------000-00--000000------0000000----------00-------",
"---000------------00000000000000------0000-000000000000000000---",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------"]


