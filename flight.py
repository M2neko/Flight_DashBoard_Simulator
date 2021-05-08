import pygame
import sys

# SPEED SET
speed_now_angle = 0
speed_set_angle = 0

# ARTIF SET
artif_now_angle = 0
artif_set_angle = 0
artif_now_height = 0
artif_set_height = 0

# ALTI SET
alti_set_meter = 0
alti_now_meter = 0

alti_hun_angle = 0
alti_tho_angle = 0
alti_tent_angle = 0

# SLIP SET
slip_now_angle = 0
slip_set_angle = 0

slip_RIGHT_X = 45
slip_LEFT_X = -45

slip_set_x = 0
slip_now_x = 0
slip_now_y = 0

# HEAD SET
head_move_speed = 2
head_now_angle = 0

# UPDOWN SET
updown_move_speed = 1.0
updown_now_angle = 0
updown_set_angle = 0

# GENERAL SET
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


# SPEED CLASSES
class SpeedInputBox:
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


# ALTI CLASSES
class AltiInputBox:
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

# SLIP CLASSES
class SlipInputBox:
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
                    self.INPUT = self.text

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

# HEAD CLASSES
class HeadInputBox:
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

                    if head_input_button.text == 'L':
                        if self.INPUT >= 0 and self.INPUT <= 360:
                            self.rotation -= self.INPUT / 10 * 360 / 36
                            self.rotation %= 360
                    if head_input_button.text == 'R':
                        if self.INPUT >= 0 and self.INPUT <= 360:
                            self.rotation += self.INPUT / 10 * 360 / 36
                            self.rotation %= 360

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


class HeadInputButton:
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


# SPEED INIT
six = pygame.image.load("points.png")
sixRect = six.get_rect()
sixRect = sixRect.move((WIDTH - sixRect.width) / 2, (HEIGHT - sixRect.height) / 2)
sixcenter = sixRect.center

speed_input_box = SpeedInputBox(WIDTH + 20 + INDEX, 90 + INDEX, 32, 32)

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
artif_input_box_rot = ArtifInputBox(WIDTH + 20 + 2.5 * INDEX + WIDTH, 80 + INDEX, 32, 32)
artif_input_box_hei = ArtifInputBox(WIDTH + 20 + 2.5 * INDEX + WIDTH, 130 + INDEX, 32, 32)

# ALTI INIT
pp_eighun = pygame.image.load("eighun.png")
ppRect_eighun = pp_eighun.get_rect()
eighun_center = ppRect_eighun.center

pp_eigtho = pygame.image.load("eigtho.png")
ppRect_eigtho = pp_eigtho.get_rect()
eigtho_center = ppRect_eigtho.center

pp_eigtent = pygame.image.load("eigtent.png")
ppRect_eigtent = pp_eigtent.get_rect()
eigtent_center = ppRect_eigtent.center

alti_input_box = AltiInputBox(WIDTH + 20 + 4 * INDEX + 2 * WIDTH, 90 + INDEX, 32, 32)

# SLIP INIT
nin = pygame.image.load("ninfly.png")
ninRect = nin.get_rect()
nincenter = ninRect.center

slip_input_box = SlipInputBox(WIDTH + 20 + INDEX, 90 + 2 * INDEX + HEIGHT, 32, 32)

# HEAD INIT
fif = pygame.image.load("fifback.png")
fifRect = fif.get_rect()
fifcenter = fifRect.center

head_input_box = HeadInputBox(WIDTH + 20 + 2.5 * INDEX + WIDTH, 90 + 2 * INDEX + HEIGHT, 32, 32)
head_input_button = HeadInputButton(WIDTH + 20 + 2.5 * INDEX + WIDTH, 45 + 2 * INDEX + HEIGHT, 32, 32)

# UPDOWN INIT
ten = pygame.image.load("tenpoi.png")
tenRect = ten.get_rect()
tencenter = tenRect.center

updown_input_box = UpDownInputBox(WIDTH + 20 + 4 * INDEX + 2 * WIDTH, 90 + 2 * INDEX + HEIGHT, BOX, BOX)
updown_input_button = UpDownInputButton(WIDTH + 15 + 4 * INDEX + 2 * WIDTH, 45 + 2 * INDEX + HEIGHT, BOX, BOX)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        speed_input_box.handle_event(event)

        alti_input_box.handle_event(event)
            
        artif_input_box_rot.handle_event(event)
        artif_input_box_hei.handle_event(event)
        artif_input_button.handle_event(event)

        slip_input_box.handle_event(event)

        head_input_box.handle_event(event)
        head_input_button.handle_event(event)
        
        updown_input_box.handle_event(event)
        updown_input_button.handle_event(event)

    # SPEED UPDATE
    if speed_now_angle > speed_set_angle:
        speed_now_angle -= 2
        if speed_now_angle < speed_set_angle:
            speed_now_angle = speed_set_angle
    if speed_now_angle < speed_set_angle:
        speed_now_angle += 2
        if speed_now_angle > speed_set_angle:
            speed_now_angle = speed_set_angle
    
    sixPP = pygame.transform.rotate(six, speed_now_angle)

    pointRect = sixPP.get_rect(center = sixcenter + pygame.math.Vector2(INDEX, INDEX))

    if speed_input_box.INPUT >= 40 and speed_input_box.INPUT <= 160:
        speed_set_angle = - ((speed_input_box.INPUT - 20) * 360 / 190)
    elif speed_input_box.INPUT > 160 and speed_input_box.INPUT <= 200:
        speed_temp_input = (speed_input_box.INPUT - 160) / 40 * 25 + 160
        speed_set_angle = - ((speed_temp_input - 20) * 360 / 190)

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

    # ALTI UPDATE
    if alti_now_meter < alti_set_meter:
        alti_hun_angle -= 36
        alti_tho_angle -= 3.6
        alti_tent_angle -= 0.36
        alti_now_meter += 1
        if alti_now_meter > alti_set_meter:
            alti_now_meter = alti_set_meter
    if alti_now_meter > alti_set_meter:
        alti_hun_angle += 36
        alti_tho_angle += 3.6
        alti_tent_angle += 0.36
        alti_now_meter -= 1
        if alti_now_meter < alti_set_meter:
            alti_now_meter = alti_set_meter
        
    
    newpp_eighun = pygame.transform.rotate(pp_eighun, alti_hun_angle)
    newRect_eighun = newpp_eighun.get_rect(center = eighun_center + pygame.math.Vector2(4 * INDEX + 2 * WIDTH, INDEX))

    newpp_eigtho = pygame.transform.rotate(pp_eigtho, alti_tho_angle)
    newRect_eigtho = newpp_eigtho.get_rect(center = eigtho_center + pygame.math.Vector2(4 * INDEX + 2 * WIDTH, INDEX))

    newpp_eigtent = pygame.transform.rotate(pp_eigtent, alti_tent_angle)
    newRect_eigtent = newpp_eigtent.get_rect(center = eigtent_center + pygame.math.Vector2(4 * INDEX + 2 * WIDTH, INDEX))


    if alti_input_box.INPUT >= 0 and alti_input_box.INPUT <= 100000:
        alti_set_meter = alti_input_box.INPUT / 100

    # SLIP UPDATE
    if slip_now_angle > slip_set_angle:
        slip_now_angle -= 0.5
        if slip_now_angle < slip_set_angle:
            slip_now_angle = slip_set_angle
    if slip_now_angle < slip_set_angle:
        slip_now_angle += 0.5
        if slip_now_angle > slip_set_angle:
            slip_now_angle = slip_set_angle
    
    ninPP = pygame.transform.rotate(nin, slip_now_angle)
    
    ninRect = ninPP.get_rect(center = nincenter + pygame.math.Vector2(INDEX, 2 * INDEX + HEIGHT))


    if slip_input_box.INPUT == 'L' :
        slip_set_angle = 20
        slip_set_x = slip_RIGHT_X
    elif slip_input_box.INPUT == 'R':
        slip_set_angle = -20
        slip_set_x = slip_LEFT_X
    elif slip_input_box.INPUT != '' :
        slip_set_angle = 0
        slip_set_x = 0

    if slip_set_x > slip_now_x:
        slip_now_x += 0.9 * 1.2
        if slip_now_x > slip_set_x:
            slip_now_x = slip_set_x
    elif slip_set_x < slip_now_x:
        slip_now_x -= 0.9 * 1.2
        if slip_now_x < slip_set_x:
            slip_now_x = slip_set_x

    if slip_now_x > 0:
        slip_now_y = -slip_now_x / 9.0
    else:
        slip_now_y = slip_now_x / 9.0

    # HEAD UPDATE
    fifPP = pygame.transform.rotate(fif, head_now_angle)

    fifRect = fifPP.get_rect(center = fifcenter + pygame.math.Vector2(2.5 * INDEX + WIDTH, 2 * INDEX + HEIGHT))

    if head_input_button.text == 'L':
        if head_now_angle <= head_input_box.rotation + head_move_speed and head_now_angle >= head_input_box.rotation - head_move_speed:
            head_now_angle = head_input_box.rotation
        else:
            head_now_angle -= head_move_speed
            head_now_angle %= 360
                
    if head_input_button.text == 'R':
        if head_now_angle <= head_input_box.rotation + head_move_speed and head_now_angle >= head_input_box.rotation - head_move_speed:
            head_now_angle = head_input_box.rotation
        else:
            head_now_angle += head_move_speed
            head_now_angle %= 360

    #if head_input_box.INPUT >= 0 and head_input_box.INPUT <= 360:
    #    head_set_angle = head_input_box.INPUT / 10 * 360 / 36
    #    head_set_angle %= 360


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

    tenRect = tenPP.get_rect(center = tencenter + pygame.math.Vector2(4 * INDEX + 2 * WIDTH, 2 * INDEX + HEIGHT))

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
            

    # BLIT
    window.fill(BACK)
    but = pygame.image.load("button.png")

    # --SPEED DRAW--
    six_img = pygame.image.load("six.png")
    window.blit(six_img, (INDEX, INDEX))
    window.blit(but, (INDEX, INDEX))
    window.blit(sixPP, pointRect)
    
    speed_input_box.update()
    speed_input_box.draw(window)
    # ---------------
    
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

    # --ALTI DRAW--
    eig_img = pygame.image.load("eigback.png")
    window.blit(eig_img, (4 * INDEX + 2 * WIDTH, INDEX))
    window.blit(but, (4 * INDEX + 2 * WIDTH, INDEX))
    window.blit(newpp_eigtent, newRect_eigtent)
    window.blit(newpp_eigtho, newRect_eigtho)
    window.blit(newpp_eighun, newRect_eighun)
    alti_input_box.update()
    alti_input_box.draw(window)
    # ---------------

    # --SLIP DRAW--
    nin_img = pygame.image.load("nin.png")
    mou = pygame.image.load("ninmou.png")
    window.blit(nin_img, (INDEX, 2 * INDEX + HEIGHT))
    window.blit(but, (INDEX, 2 * INDEX + HEIGHT))
    window.blit(ninPP, ninRect)
    window.blit(mou, (slip_now_x + INDEX, slip_now_y + 2 * INDEX + HEIGHT))
    slip_input_box.update()
    slip_input_box.draw(window)
    # ---------------

    # --HEAD DRAW--
    window.blit(fifPP, fifRect)
    fif_img = pygame.image.load("fiftop.png")
    window.blit(fif_img, (2.5 * INDEX + WIDTH, 2 * INDEX + HEIGHT))
    window.blit(but, (2.5 * INDEX + WIDTH, 2 * INDEX + HEIGHT))
    
    head_input_box.update()
    head_input_box.draw(window)

    head_input_button.draw(window)
    # ---------------

    # --UPDOWN DRAW--
    ten_img = pygame.image.load("ten.png")
    window.blit(ten_img, (4 * INDEX + 2 * WIDTH, 2 * INDEX + HEIGHT))
    window.blit(but, (4 * INDEX + 2 * WIDTH, 2 * INDEX + HEIGHT))
    window.blit(tenPP, tenRect)
    
    updown_input_box.update()
    updown_input_box.draw(window)

    updown_input_button.draw(window)
    # ---------------

    
    pygame.display.flip()
    pygame.display.update()
