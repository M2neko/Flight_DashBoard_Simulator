import pygame
import sys

now_angle = 0
set_angle = 0
now_height = 0
set_height = 0
WIDTH = 200
HEIGHT = 200

pygame.init()
window = pygame.display.set_mode((WIDTH + 100, HEIGHT))
pygame.display.set_caption("Cessna 172")

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputButton:

    def __init__(self, x, y, w, h, text='L'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.text == 'R':
                    self.text = 'L'
                else:
                    self.text = 'R'
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.txt_surface = FONT.render(self.text, True, self.color)


    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.INPUT = 0
        self.active = False
        self.letRot = False

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

                    self.letRot = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(35, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


pp_dash = pygame.image.load("sevdash.png")
ppRect_dash = pp_dash.get_rect()
ppRect_dash = ppRect_dash.move((WIDTH - ppRect_dash.width) / 2, (HEIGHT - ppRect_dash.height) / 2)
pygame.display.update()

pp_updown = pygame.image.load("sevupdown.png")
ppRect_updown = pp_updown.get_rect()
ppRect_updown = ppRect_updown.move((WIDTH - ppRect_updown.width) / 2, (HEIGHT - ppRect_updown.height) / 2)
pygame.display.update()

pp_turn = pygame.image.load("sevturn.png")
ppRect_turn = pp_turn.get_rect()
ppRect_turn = ppRect_turn.move((WIDTH - ppRect_turn.width) / 2, (HEIGHT - ppRect_turn.height) / 2)
pygame.display.update()

input_button = InputButton(220, 30, 32, 32)
input_box_rot = InputBox(220, 70, 32, 32)
input_box_hei = InputBox(220, 130, 32, 32)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input_box_rot.handle_event(event)
        input_box_hei.handle_event(event)
        input_button.handle_event(event)

    if now_angle > set_angle:
        now_angle -= 2
        if now_angle < set_angle:
            now_angle = set_angle
    if now_angle < set_angle:
        now_angle += 2
        if now_angle > set_angle:
            now_angle = set_angle

    if now_height > set_height:
        now_height -= 0.5
        if now_height < set_height:
            now_height = set_height
    if now_height < set_height:
        now_height += 0.5
        if now_height > set_height:
            now_height = set_height
    
    newpp_dash = pygame.transform.rotate(pp_dash, now_angle)
    newRect_dash = newpp_dash.get_rect(center = ppRect_dash.center)

    newpp_updown = pygame.transform.rotate(pp_updown, now_angle)
    newRect_updown = newpp_updown.get_rect(center = ppRect_updown.center + pygame.math.Vector2(0, now_height).rotate(-now_angle))

    newpp_turn = pygame.transform.rotate(pp_turn, now_angle)
    newRect_turn = newpp_turn.get_rect(center = ppRect_turn.center)

    if input_box_rot.letRot:
        if input_box_rot.INPUT >= 0 and input_box_rot.INPUT <= 90:
            if input_button.text == 'L':
                set_angle = input_box_rot.INPUT
                input_box_rot.letRot = False
            else:
                set_angle = -input_box_rot.INPUT
                input_box_rot.letRot = False

    if input_box_hei.INPUT >= 0 and input_box_hei.INPUT <= 20:
        set_height = input_box_hei.INPUT
    elif input_box_hei.INPUT >= -20 and input_box_hei.INPUT < 0:
        set_height = input_box_hei.INPUT / 15 * 20

    window.fill((111,111,111))	
    window.blit(newpp_dash, newRect_dash)
    window.blit(newpp_updown, newRect_updown)
    window.blit(newpp_turn, newRect_turn)
    
    background_img = pygame.image.load("sevback.png")
    window.blit(background_img, (0, 0))
    
    input_box_rot.update()
    input_box_hei.update()
    input_box_rot.draw(window)
    input_box_hei.draw(window)
    input_button.draw(window)
    
    pygame.display.flip()
    pygame.display.update()
