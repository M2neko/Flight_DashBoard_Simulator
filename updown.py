import pygame
import sys

move_speed = 1.0
now_angle = 0
set_angle = 0
WIDTH = 200
HEIGHT = 200

pygame.init()
window = pygame.display.set_mode((WIDTH + 100, HEIGHT))
pygame.display.set_caption("Cessna 172")


WHITE = (255, 255, 255)
RED = (255, 0, 0)

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
        self.rotation = 0

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


class InputButton:

    def __init__(self, x, y, w, h, text='UP'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.text == 'UP':
                    self.text = 'DN'
                else:
                    self.text = 'UP'
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.txt_surface = FONT.render(self.text, True, self.color)


    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))



        
pp = pygame.image.load("tenpoi.png")
ppRect = pp.get_rect()
ppRect = ppRect.move((WIDTH - ppRect.width) / 2, (HEIGHT - ppRect.height) / 2)
pygame.display.update()

input_box = InputBox(220, 90, 32, 32)
input_button = InputButton(215, 45, 32, 32)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input_box.handle_event(event)
        input_button.handle_event(event)

    if now_angle > set_angle:
        now_angle -= move_speed
        if now_angle < set_angle:
            now_angle = set_angle
    if now_angle < set_angle:
        now_angle += move_speed
        if now_angle > set_angle:
            now_angle = set_angle
    
    newpp = pygame.transform.rotate(pp, now_angle)

    newRect = newpp.get_rect(center = ppRect.center)

    if input_box.INPUT >= 0 and input_box.INPUT <= 500:
        if input_button.text == 'UP':
            set_angle = -input_box.INPUT / 100.0 * 360 / 50.0
        if input_button.text == 'DN':
            set_angle = input_box.INPUT / 100.0 * 360 / 50.0
            
    elif input_box.INPUT >= 0 and input_box.INPUT <= 1000:
        if input_button.text == 'UP':
            set_angle = - (36 + (input_box.INPUT - 500) / 100.0 * 360 / 42.0)
        if input_button.text == 'DN':
            set_angle = 36 + (input_box.INPUT - 500) / 100.0 * 360 / 42.0
            
    elif input_box.INPUT >= 0 and input_box.INPUT <= 2000:
        if input_button.text == 'UP':
            set_angle = - (78.86 + (input_box.INPUT - 1000) / 100.0 * 360 / 38.0)
        if input_button.text == 'DN':
            set_angle = 78.86 + (input_box.INPUT - 1000) / 100.0 * 360 / 38.0

    window.fill((111,111,111))
    

    img = pygame.image.load("ten.png")
    window.blit(img, (0, 0))
    window.blit(newpp, newRect)
    
    input_box.update()
    input_box.draw(window)

    input_button.draw(window)

    
    
    pygame.display.flip()
    pygame.display.update()
