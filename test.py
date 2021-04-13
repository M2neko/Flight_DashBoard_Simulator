import pygame
import sys

angle = 1
WIDTH = 200
HEIGHT = 200

pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Cessna 172")

pp = pygame.image.load("points.png")
ppRect = pp.get_rect()
ppRect = ppRect.move((WIDTH - ppRect.width) / 2, (HEIGHT - ppRect.height) / 2)

#window.blit(point, (100 - 5.5, 100 - 49))
pygame.display.update()


flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    newpp = pygame.transform.rotate(pp, angle)
    
    newRect = newpp.get_rect(center = ppRect.center)
    angle -= 1

    window.fill((111,111,111))	
    img = pygame.image.load("fou.png")
    window.blit(img, (0, 0))
    window.blit(newpp, newRect)
    pygame.display.update()
