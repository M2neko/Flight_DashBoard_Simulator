import pygame
import sys

now_angle = 0
set_angle = 0
WIDTH = 200
HEIGHT = 200

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
        input_box.handle_event(event)

    if now_angle > set_angle:
        now_angle -= 2
        if now_angle < set_angle:
            now_angle = set_angle
    if now_angle < set_angle:
        now_angle += 2
        if now_angle > set_angle:
            now_angle = set_angle
    
    newpp = pygame.transform.rotate(pp, now_angle)

    newRect = newpp.get_rect(center = ppRect.center)


    if input_box.INPUT >= 40 and input_box.INPUT <= 160:
        set_angle = - ((input_box.INPUT - 20) * 360 / 190)
    elif input_box.INPUT > 160 and input_box.INPUT <= 200:
        temp_input = (input_box.INPUT - 160) / 40 * 25 + 160
        set_angle = - ((temp_input - 20) * 360 / 190)

    

    window.fill((111,111,111))	
    img = pygame.image.load("six.png")
    window.blit(img, (0, 0))
    window.blit(newpp, newRect)
    
    input_box.update()
    input_box.draw(window)
    
    pygame.display.flip()
    pygame.display.update()
