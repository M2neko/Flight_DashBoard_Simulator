import pygame
import sys

artif_now_angle = 0
artif_set_angle = 0
artif_now_height = 0
artif_set_height = 0

updown_move_speed = 1.0
updown_now_angle = 0
updown_set_angle = 0

MAX_WIDTH = 1200
MAX_HEIGHT = 700

WIDTH = 200
HEIGHT = 200

INDEX = 100

BOX = 32

pygame.init()
window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pygame.display.set_caption("Cessna 172")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BACK = (111,111,111)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)



# ARTIF CLASSES
class ArtifInputButton:
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


class ArtifInputBox:
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







# UPDOWN CLASSES
class UpDownInputBox:
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


class UpDownInputButton:
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


# ARTIF INIT
pp_dash = pygame.image.load("sevdash.png")
ppRect_dash = pp_dash.get_rect()
dash_center = ppRect_dash.center

pp_updown = pygame.image.load("sevupdown.png")
ppRect_updown = pp_updown.get_rect()
updown_center = ppRect_updown.center

pp_turn = pygame.image.load("sevturn.png")
ppRect_turn = pp_turn.get_rect()
turn_center = ppRect_turn.center

artif_input_button = ArtifInputButton(WIDTH + 20 + 2.5 * INDEX + WIDTH, 30 + INDEX, 32, 32)
artif_input_box_rot = ArtifInputBox(WIDTH + 20 + 2.5 * INDEX + WIDTH, 70 + INDEX, 32, 32)
artif_input_box_hei = ArtifInputBox(WIDTH + 20 + 2.5 * INDEX + WIDTH, 130 + INDEX, 32, 32)


# UPDOWN INIT
ten = pygame.image.load("tenpoi.png")
tenRect = ten.get_rect()
tencenter = tenRect.center

updown_input_box = UpDownInputBox(WIDTH + 20 + INDEX, 90 + INDEX, BOX, BOX)
updown_input_button = UpDownInputButton(WIDTH + 15 + INDEX, 45 + INDEX, BOX, BOX)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        artif_input_box_rot.handle_event(event)
        artif_input_box_hei.handle_event(event)
        artif_input_button.handle_event(event)
        
        updown_input_box.handle_event(event)
        updown_input_button.handle_event(event)
        

    # ARTIF UPDATE
    if artif_now_angle > artif_set_angle:
        artif_now_angle -= 2
        if artif_now_angle < artif_set_angle:
            artif_now_angle = artif_set_angle
    if artif_now_angle < artif_set_angle:
        artif_now_angle += 2
        if artif_now_angle > artif_set_angle:
            artif_now_angle = artif_set_angle

    if artif_now_height > artif_set_height:
        artif_now_height -= 0.5
        if artif_now_height < artif_set_height:
            artif_now_height = artif_set_height
    if artif_now_height < artif_set_height:
        artif_now_height += 0.5
        if artif_now_height > artif_set_height:
            artif_now_height = artif_set_height
    
    newpp_dash = pygame.transform.rotate(pp_dash, artif_now_angle)
    newRect_dash = newpp_dash.get_rect(center = dash_center + pygame.math.Vector2(2.5 * INDEX + WIDTH, INDEX))

    newpp_updown = pygame.transform.rotate(pp_updown, artif_now_angle)
    newRect_updown = newpp_updown.get_rect(center = updown_center + pygame.math.Vector2(2.5 * INDEX + WIDTH, INDEX) + pygame.math.Vector2(0, artif_now_height).rotate(-artif_now_angle))

    newpp_turn = pygame.transform.rotate(pp_turn, artif_now_angle)
    newRect_turn = newpp_turn.get_rect(center = turn_center + pygame.math.Vector2(2.5 * INDEX + WIDTH, INDEX))

    if artif_input_box_rot.letRot:
        if artif_input_box_rot.INPUT >= 0 and artif_input_box_rot.INPUT <= 90:
            if artif_input_button.text == 'L':
                artif_set_angle = artif_input_box_rot.INPUT
                artif_input_box_rot.letRot = False
            else:
                artif_set_angle = -artif_input_box_rot.INPUT
                artif_input_box_rot.letRot = False

    if artif_input_box_hei.INPUT >= 0 and artif_input_box_hei.INPUT <= 20:
        artif_set_height = artif_input_box_hei.INPUT
    elif artif_input_box_hei.INPUT >= -20 and artif_input_box_hei.INPUT < 0:
        artif_set_height = artif_input_box_hei.INPUT / 15 * 20




    # UPDOWN UPDATE
    if updown_now_angle > updown_set_angle:
        updown_now_angle -= updown_move_speed
        if updown_now_angle < updown_set_angle:
            updown_now_angle = updown_set_angle
    if updown_now_angle < updown_set_angle:
        updown_now_angle += updown_move_speed
        if updown_now_angle > updown_set_angle:
            updown_now_angle = updown_set_angle
    
    tenPP = pygame.transform.rotate(ten, updown_now_angle)

    tenRect = tenPP.get_rect(center = tencenter + pygame.math.Vector2(INDEX, INDEX))

    if updown_input_box.INPUT >= 0 and updown_input_box.INPUT <= 500:
        if updown_input_button.text == 'UP':
            updown_set_angle = -updown_input_box.INPUT / 100.0 * 360 / 50.0
        if updown_input_button.text == 'DN':
            updown_set_angle = updown_input_box.INPUT / 100.0 * 360 / 50.0
            
    elif updown_input_box.INPUT >= 0 and updown_input_box.INPUT <= 1000:
        if updown_input_button.text == 'UP':
            updown_set_angle = - (36 + (updown_input_box.INPUT - 500) / 100.0 * 360 / 42.0)
        if updown_input_button.text == 'DN':
            updown_set_angle = 36 + (updown_input_box.INPUT - 500) / 100.0 * 360 / 42.0
            
    elif updown_input_box.INPUT >= 0 and updown_input_box.INPUT <= 2000:
        if updown_input_button.text == 'UP':
            updown_set_angle = - (78.86 + (updown_input_box.INPUT - 1000) / 100.0 * 360 / 38.0)
        if updown_input_button.text == 'DN':
            updown_set_angle = 78.86 + (updown_input_box.INPUT - 1000) / 100.0 * 360 / 38.0






    window.fill(BACK)
    but = pygame.image.load("button.png")
    
    # --ARTIF DRAW--
    window.blit(newpp_dash, newRect_dash)
    window.blit(newpp_updown, newRect_updown)
    window.blit(newpp_turn, newRect_turn)
    
    background_img = pygame.image.load("sevback.png")
    window.blit(background_img, (2.5 * INDEX + WIDTH, INDEX))
    window.blit(but, (2.5 * INDEX + WIDTH, INDEX))
    
    artif_input_box_rot.update()
    artif_input_box_hei.update()
    artif_input_box_rot.draw(window)
    artif_input_box_hei.draw(window)
    artif_input_button.draw(window)
    # ---------------


    # --UPDOWN DRAW--
    img = pygame.image.load("ten.png")
    window.blit(img, (INDEX, INDEX))
    window.blit(but, (INDEX, INDEX))
    window.blit(tenPP, tenRect)
    
    updown_input_box.update()
    updown_input_box.draw(window)

    updown_input_button.draw(window)
    # ---------------

    

    
    
    pygame.display.flip()
    pygame.display.update()
