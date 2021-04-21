import pygame
import sys

WIDTH = 200
HEIGHT = 200

set_meter = 0
now_meter = 0

hun_angle = 0
tho_angle = 0
tent_angle = 0

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
        self.INPUT = 0
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    
                    # Update INPUT
                    self.INPUT = float(self.text)

                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(35, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)





pp_eighun = pygame.image.load("eighun.png")
ppRect_eighun = pp_eighun.get_rect()
ppRect_eighun = ppRect_eighun.move((WIDTH - ppRect_eighun.width) / 2, (HEIGHT - ppRect_eighun.height) / 2)
pygame.display.update()

pp_eigtho = pygame.image.load("eigtho.png")
ppRect_eigtho = pp_eigtho.get_rect()
ppRect_eigtho = ppRect_eigtho.move((WIDTH - ppRect_eigtho.width) / 2, (HEIGHT - ppRect_eigtho.height) / 2)
pygame.display.update()

pp_eigtent = pygame.image.load("eigtent.png")
ppRect_eigtent = pp_eigtent.get_rect()
ppRect_eigtent = ppRect_eigtent.move((WIDTH - ppRect_eigtent.width) / 2, (HEIGHT - ppRect_eigtent.height) / 2)
pygame.display.update()

input_box = InputBox(220, 90, 32, 32)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input_box.handle_event(event)


    if now_meter < set_meter:
        hun_angle -= 36
        tho_angle -= 3.6
        tent_angle -= 0.36
        now_meter += 1
        if now_meter > set_meter:
            now_meter = set_meter
    if now_meter > set_meter:
        hun_angle += 36
        tho_angle += 3.6
        tent_angle += 0.36
        now_meter -= 1
        if now_meter < set_meter:
            now_meter = set_meter
        
    
    newpp_eighun = pygame.transform.rotate(pp_eighun, hun_angle)
    newRect_eighun = newpp_eighun.get_rect(center = ppRect_eighun.center)

    newpp_eigtho = pygame.transform.rotate(pp_eigtho, tho_angle)
    newRect_eigtho = newpp_eigtho.get_rect(center = ppRect_eigtho.center)

    newpp_eigtent = pygame.transform.rotate(pp_eigtent, tent_angle)
    newRect_eigtent = newpp_eigtent.get_rect(center = ppRect_eigtent.center)


    if input_box.INPUT >= 0 and input_box.INPUT <= 100000:
        set_meter = input_box.INPUT / 100

    window.fill((111,111,111))	
    img = pygame.image.load("eigback.png")
    window.blit(img, (0, 0))
    window.blit(newpp_eigtent, newRect_eigtent)
    window.blit(newpp_eigtho, newRect_eigtho)
    window.blit(newpp_eighun, newRect_eighun)
    
    input_box.update()
    input_box.draw(window)
    
    pygame.display.flip()
    pygame.display.update()
