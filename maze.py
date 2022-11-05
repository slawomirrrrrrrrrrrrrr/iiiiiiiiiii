
class GameSprite(sprite.Sprite) :
    def init(self, player_image, player_x, player_y, player_speed) :
        super().init() 
        
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed   
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
class player(GameSprite)
    def update(self):
        keys = key.get.pressed()
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 395:
class wall ():
    def __init__(self,color_1,.. wall_x,... wall_width )
    super().__init__()
    self.








    
       
  
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
  
 
win_width = 700 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
display.set_caption("Maze") 
background = transform.scale(image.load("background.jpg"), (win_width, win_height)) 
  
 
player = player('hero.png', 5, win_height - 80, 4) 
monster = GameSprite('cyborg.png', win_width - 80, 280, 2) 
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0) 
  
game = True 
clock = time.Clock() 
FPS = 60 
  
 
mixer.init() 
mixer.music.load('jungles.ogg') 
mixer.music.play() 
  
while game: 
    
    for e in event.get() :
        if e.type == QUIT: 
            game = False 
   
    window.blit(background,(0, 0)) 
    player.reset() 
    monster.reset() 
  
    display.update() 
    clock.tick(FPS)