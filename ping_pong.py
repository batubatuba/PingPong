from pygame import*
class GameSprite(sprite.Sprite)
  def __init__(self,player_image.player__x,player_y,player_speed,width,heigth):
    super().__init__()
    self.image = transform.scale( image.load(player_image) , (width,heigth))
    self.speed = player_speed
    self.rect.x = player_x
    self.rect_y = player_y
  def reset(self):
    window.blit(self.image,(self.rect.x,self.rect.y))
    class Player(GameSprite):
      def update_r(self)
      keys = key.get_pressed()
      if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heigth -80:
          self.rect.y += self.speed
          def update_r(self)
      keys = key.get_pressed()
      if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_heigth -80:
          self.rect.y += self.speed

#Oyun Sahnesi
back = (200,255,255) #Arka Plan Renk Kodu
win_width = 600
win_heigth = 500
window = display.set_mode((win_width,win_heigth))
window.fill(back)

#Bayrak Değişkenler
game = True 
finish = False
clock = time.Clock()
FPS = 60
