import pygame
import sys

angle = 0
WIDTH = 200
HEIGHT = 200
INPUT = 10

pygame.init()
window = pygame.display.set_mode((WIDTH + 100, HEIGHT))
pygame.display.set_caption("Cessna 172")



COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)





pp = pygame.image.load("points.png")
ppRect = pp.get_rect()
ppRect = ppRect.move((WIDTH - ppRect.width) / 2, (HEIGHT - ppRect.height) / 2)
pygame.display.update()

input_box = InputBox(220, 90, 32, 32)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    newpp = pygame.transform.rotate(pp, angle)
    
    newRect = newpp.get_rect(center = ppRect.center)
    angle = -INPUT * 360 / 12
    angle %= 360

    window.fill((111,111,111))	
    img = pygame.image.load("fou.png")
    window.blit(img, (0, 0))
    window.blit(newpp, newRect)

    input_box.draw(window)
    pygame.display.flip()
    pygame.display.update()
