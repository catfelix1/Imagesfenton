import pygame
import os

x = 30
y = 30
_image_library = {}
lives = int(4)
z = int(input("What speed do you want to use? "))
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
        screen.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        screen.blit(get_image('greyball.png'), (x, y))
                
        if lives != 0:
                
                if x >= 360 or x <= 0 or y >= 260 or y <= 0:
                        x = 180
                        y = 120
                        lives = (lives-1)
                        print (lives)
                if pressed[pygame.K_UP]: y -= z
                if pressed[pygame.K_DOWN]: y += z
                if pressed[pygame.K_LEFT]: x -= z
                if pressed[pygame.K_RIGHT]: x += z
        else :
                print ("You're out of lives!")
                done = True
       
        pygame.display.flip()
        clock.tick(60)
