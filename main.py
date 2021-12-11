import pygame #importing pygame module
#defining some colours
import time
import os
GREEN = (20, 255, 140)
GREEN2 = (0,255,0)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)

weaponfired = 0
moveleft = 0
moveleft2 = 0
        
 #person class, the class for the player object
class Person(pygame.sprite.Sprite):  #inherits from pygame sprites
  def __init__(self, color, width, height):
    super().__init__() 
    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
  
  def moveright(self, pixels):
    self.rect.x += pixels

  def moveleft(self, pixels):
    self.rect.x -= pixels

  def moveup(self,pixels):
    self.rect.y -= pixels
  
  def movedown(self,pixels):
    self.rect.y += pixels


class Collsiions(pygame.sprite.Sprite):
  def __init__(self,color,width,height,friendly):
    super().__init__() 
    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
    self.friendly = friendly
  
  def moveright(self,pixels):
    self.rect.x += pixels

  def moveleft(self,pixels):
    self.rect.x -= pixels

class Bullet(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__() 
    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()

  def bulletmoveup(self,pixels):
    self.rect.y -= pixels
  
  def bulletmovedown(self,pixels):
    self.rect.y += pixels
  
  def bulletmoveleft(self,pixels):
    self.rect.x -= pixels
  
  def bulletmoveright(self,pixels):
    self.rect.x += pixels



#collisionstuff
allothersprites = pygame.sprite.Group()
#initialise pygame screen
pygame.init()
SCREENWIDTH=400
SCREENHEIGHT=500
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Marlo") #"mario" lol
friendlysprites = pygame.sprite.Group()
clear = lambda: os.system('clear')
#clear()
#a list of all the sprites
all_sprites_list = pygame.sprite.Group()
#creating the player object
player = Person(PURPLE, 20, 20)
#defining it's coordinates
player.rect.x = 50
player.rect.y = 400
#bullet
bullet = Bullet(GREY,2,10)
#for the thing you need to collect
collectable = Collsiions(GREEN,20,20,1)
collectable.rect.x = 250
collectable.rect.y = 50

weapon = Collsiions(BLUE,20,20,1)
weapon.rect.x = 350
weapon.rect.y = 450
giveweapon = pygame.sprite.Group()
giveweapon.add(weapon)

movedetect = pygame.sprite.Group()
detect1 = Collsiions(BLACK,5,500,0)
detect2 = Collsiions(BLACK,5,500,0)
detect2.rect.x = 400
movedetect.add(detect1)
movedetect.add(detect2)

#the things you need to avoid
badguy1 = Collsiions(RED,50,50,0)
badguy1.rect.y = 200
badguy1.rect.x = 10 
collision_list = pygame.sprite.spritecollide(player,allothersprites,False)
badguy2 = Collsiions(RED,20,20,0)
badguy2.rect.y = 100
badguy2.rect.x = 200
allothersprites.add(badguy1)
friendlysprites.add(collectable)
secondbadguy = pygame.sprite.Group()
secondbadguy.add(badguy2)
#for the Bullet
bulletshot = pygame.sprite.Group()

#for the walls so that the player doesn't go outside of the game barriers:
hleft = Collsiions(RED,1,500,0)
hright = Collsiions(RED,1,500,0)
hright.rect.x = 399

vtop = Collsiions(RED,400,1,0)
vbottom = Collsiions(RED,400,1,0)
vbottom.rect.y = 499

wall1 = Collsiions(RED,1,220,0)
wall1.rect.y = 280
wall1.rect.x = 200
wall2 = Collsiions(RED,1,180,0)
wall2.rect.y = 0
wall2.rect.x = 200
wall3 = Collsiions(RED,140,1,0)
wall3.rect.x = 200
wall3.rect.y = 180
walls = pygame.sprite.Group()
walls.add(hleft)
walls.add(hright)
walls.add(vtop)
walls.add(vbottom)
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
carryOn = True #setting some things for the game logic
clock=pygame.time.Clock()
all_sprites_list.add(player)
all_sprites_list.add(collectable)
all_sprites_list.add(badguy1)
all_sprites_list.add(badguy2)
all_sprites_list.add(weapon)
all_sprites_list.add(detect1)
all_sprites_list.add(detect2)
all_sprites_list.add(hleft)
all_sprites_list.add(hright)
all_sprites_list.add(vtop)
all_sprites_list.add(vbottom)
all_sprites_list.add(wall1)
all_sprites_list.add(wall2)
all_sprites_list.add(wall3)

#preparing some textual stuff right here
font = pygame.font.Font("freesansbold.ttf",32)

while carryOn: 
  for event in pygame.event.get(): #allowing the game to be closed
    if event.type==pygame.QUIT:
      carryOn=False
    elif event.type==pygame.KEYDOWN:
      if event.key==pygame.K_p:
        carryOn=False
  
  if moveleft == 0:
    badguy1.moveright(2)
  else:
    badguy1.moveleft(2)
  
  if moveleft2==0:
    badguy2.moveright(4)
  else:
    badguy2.moveleft(4)

  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    player.moveleft(5)
  if keys[pygame.K_d]:
    player.moveright(5)
  if keys[pygame.K_w]:
    player.moveup(5)
  if keys[pygame.K_s]:
    player.movedown(5)
  
  if keys[pygame.K_UP] or keys[pygame.K_i] :
    if weapon == 1:
      print("bang!")
      bullet.rect.x = player.rect.x
      bullet.rect.y = player.rect.y
      all_sprites_list.add(bullet)
      weaponfired = 1
      weapon = 0

  if keys[pygame.K_DOWN] or keys[pygame.K_k]:
    if weapon == 1:
      print("bang!")
      bullet.rect.x = player.rect.x
      bullet.rect.y = player.rect.y
      all_sprites_list.add(bullet)
      weaponfired = 2
      weapon = 0
  
  if keys[pygame.K_LEFT] or keys[pygame.K_j]:
    if weapon == 1:
      print("bang!")
      bullet.rect.x = player.rect.x
      bullet.rect.y = player.rect.y
      all_sprites_list.add(bullet)
      weaponfired = 3
      weapon = 0
  
  if keys[pygame.K_RIGHT] or keys[pygame.K_l]:
    if weapon == 1:
      print("bang!")
      bullet.rect.x = player.rect.x
      bullet.rect.y = player.rect.y
      all_sprites_list.add(bullet)
      weaponfired = 4
      weapon = 0
  

  badcollisionlist = pygame.sprite.spritecollide(player,allothersprites,False)
  for i in (badcollisionlist):
      text = font.render("game over :(",True,WHITE,RED)
      textRect = text.get_rect()
      textRect.center = (200,250)
      screen.blit(text,textRect)
      pygame.display.update()
      time.sleep(2)
      print("Game over")
      carryOn = False

  badcollide2 = pygame.sprite.spritecollide(player,secondbadguy,False)
  for i in(badcollide2):
    print("game over")
    text = font.render("game over :(",True,WHITE,RED)
    textRect = text.get_rect()
    textRect.center = (200,250)
    screen.blit(text,textRect)
    pygame.display.update()
    time.sleep(2)
    carryOn = False
  
  goodcollisionlist = pygame.sprite.spritecollide(player,friendlysprites,False)
  for i in (goodcollisionlist):
    print("WE WOOOOOOOOOOOOOOOOOOOOOOOOOOON")
    text = font.render("WEEEEE WOOOOOON :)",True,WHITE,GREEN)
    textRect = text.get_rect()
    textRect.center = (200,250)
    screen.blit(text,textRect)
    pygame.display.update()
    time.sleep(2)
    carryOn = False 

  
  weaponadd = pygame.sprite.spritecollide(player,giveweapon,False)
  for i in (weaponadd):
    print("1 bullet added")
    weapon.kill()
    weapon = 1
    all_sprites_list.remove(weapon)
  
  bullethit = pygame.sprite.spritecollide(bullet,allothersprites,False)
  for i in (bullethit):
    print("bullet hit")
    badguy1.kill()
  
  bullethit2 = pygame.sprite.spritecollide(bullet,secondbadguy,False)
  for i in (bullethit2):
    print("bullet hit")
    badguy2.kill()
  
  endofpath = pygame.sprite.spritecollide(badguy1,walls,False)
  for i in (endofpath):
    if moveleft == 0:
      moveleft =1
    else:
      moveleft = 0
  
  endofpath2 = pygame.sprite.spritecollide(badguy2,walls,False)
  for i in (endofpath2):
    if moveleft2 == 0:
      moveleft2 = 1
    else:
      moveleft2 = 0
  
  wallcollision =pygame.sprite.spritecollide(player,walls,False)
  for i in(wallcollision):
    print("game over")
    text = font.render("game over :(",True,WHITE,RED)
    textRect = text.get_rect()
    textRect.center = (200,250)
    screen.blit(text,textRect)
    pygame.display.update()
    time.sleep(2)
    print("don't go here again >:( game over!!")
    carryOn = False 

  if weaponfired == 1:
    bullet.bulletmoveup(15)
  if weaponfired == 2:
    bullet.bulletmovedown(15)
  if weaponfired == 3:
    bullet.bulletmoveleft(15)
  if weaponfired == 4:
    bullet.bulletmoveright(15)
                              
  all_sprites_list.update()
  screen.fill(BLACK) #make the screen green
  all_sprites_list.draw(screen) #draw the sprites
  pygame.display.flip() 
  clock.tick(60)
  pygame.key.start_text_input()
 
pygame.quit()
#hey you reading this i think you're really cool and i appreciate you :)