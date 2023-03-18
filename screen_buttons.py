import pygame


class Screen:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("ASSETS/BACKGROUND/forth.png").convert_alpha()
        self.image_rect = self.image.get_rect(topleft=(0, 0))
        self.font = pygame.font.Font("ASSETS/fonts/Pixeltype.ttf", 35)

    def draw_main_screen(self):
        self.screen.blit(self.image, self.image_rect)
        self.make_window_beat()
        self.name_show()

    def make_window_beat(self):
        pygame.draw.line(self.screen, "white", (0, 350), (1300, 350),2)
        pygame.draw.line(self.screen, "white", (0, 480), (1300, 480),2)
        pygame.draw.line(self.screen, "white", (550, 350), (550, 680),2)
        pygame.draw.line(self.screen,"white",(0,680),(1200,680),2)

        pygame.draw.line(self.screen, "white", (0, 40), (550, 40),2)
        pygame.draw.line(self.screen, "white", (550, 40), (550, 300),2)
        pygame.draw.line(self.screen, "white", (0, 300), (550, 300),2)
        pygame.draw.line(self.screen, "white", (0, 170), (550, 170),2)

        pygame.draw.line(self.screen, "white",(920,40),(1200,40),2)
        pygame.draw.line(self.screen,"white",(920,0),(920,40),2)

        pygame.draw.line(self.screen,"white",(660,40),(880,40),2)
        pygame.draw.line(self.screen,"white",(660,0),(660,40),2)
        pygame.draw.line(self.screen,"white",(880,0),(880,40),2)

        pygame.draw.line(self.screen,"white",(280,520),(550,520),2)# for player1
        pygame.draw.line(self.screen,"white",(280,480),(280,520),2)

        pygame.draw.line(self.screen, "white", (930, 520), (1200, 520), 2)
        pygame.draw.line(self.screen, "white", (930, 480), (930, 520), 2)

        pygame.draw.line(self.screen,"white",(280,210),(550,210),2)
        pygame.draw.line(self.screen,"white",(280,170),(280,210),2)

        pygame.draw.line(self.screen,"white",(460,550),(550,550),2)# for player1
        pygame.draw.line(self.screen,"white",(460,520),(460,550),2)# money box

        pygame.draw.line(self.screen, "white", (460, 580), (550, 580), 2)  # for player1
        pygame.draw.line(self.screen, "white", (460, 550), (460, 580), 2)  # bet box

        pygame.draw.line(self.screen, "white", (1110, 550), (1200, 550), 2)  # for player2
        pygame.draw.line(self.screen, "white", (1110, 520), (1110, 550), 2)

        pygame.draw.line(self.screen, "white", (1110, 580), (1200, 580), 2)  # for player2
        pygame.draw.line(self.screen, "white", (1110, 550), (1110, 580), 2)

    def player1_win_equal_loss(self,color):
        if color == "":
            color = "white"
        else:
            color = color
        pygame.draw.line(self.screen,color,(0,350),(550,350),2)
        pygame.draw.line(self.screen,color,(0,480),(550,480),2)
        pygame.draw.line(self.screen, color, (280, 520), (550, 520), 2)  # for player1
        pygame.draw.line(self.screen, color, (280, 480), (280, 520), 2)

    def player2_win_equal_loss(self, color):
        if color == "":
            color = "white"
        else:
            color = color
        pygame.draw.line(self.screen, color, (550, 350), (1300, 350),2)
        pygame.draw.line(self.screen, color, (550, 480), (1300, 480),2)
        pygame.draw.line(self.screen, color, (930, 520), (1200, 520), 2)
        pygame.draw.line(self.screen, color, (930, 480), (930, 520), 2)

    def dealer_win_equal_loss(self, color):
        if color == "":
            color = "white"
        else:
            color = color
        pygame.draw.line(self.screen, color, (0, 40), (550, 40),2)
        pygame.draw.line(self.screen, color, (0, 170), (550, 170),2)
        pygame.draw.line(self.screen,color,(550,40),(550,170),2)
        pygame.draw.line(self.screen, color, (280, 210), (550, 210), 2)
        pygame.draw.line(self.screen, color, (280, 170), (280, 210), 2)

    def name_show(self):
        player_name1 = self.font.render("HANZALA Khan", False, "white")
        self.screen.blit(player_name1, (0, 490))
        hand_name = self.font.render("HANZALA HAND", False, "white")
        self.screen.blit(hand_name, (0, 325))

        player_name2 = self.font.render("Ahmad Khan", False, "white")
        self.screen.blit(player_name2, (560, 490))
        hand_name = self.font.render("AHMAD HAND", False, "white")
        self.screen.blit(hand_name, (560, 320))

        dealer = self.font.render("Dealer HAND", False, "white")
        self.screen.blit(dealer, (0, 10))

        player1_coin_label = self.font.render("Total Chips",False,"white")
        self.screen.blit(player1_coin_label,(340,525))

        player1_coin_label = self.font.render("Round Bet", False, "white")
        self.screen.blit(player1_coin_label, (350, 560))

        player2_coin_label = self.font.render("Total Chips", False, "white")
        self.screen.blit(player2_coin_label, (990, 525))

        player2_coin_label = self.font.render("Round Bet", False, "white")
        self.screen.blit(player2_coin_label, (1000, 560))

    def hand_value_hanzala(self, value:int = 0):
        show_value = self.font.render(f"Value {value}", False, "white")
        self.screen.blit(show_value, (200, 325))

    def hand_value_ahmad(self, value: int = 0):
        show_value = self.font.render(f"Value {value}", False, "white")
        self.screen.blit(show_value, (750, 320))

    def hand_value_dealer(self, value: int = 1):
        show_value = self.font.render(f"Value {value}", False, "white")
        self.screen.blit(show_value, (200, 10))


class Buttons:
    def __init__(self,screen):
        self.screen = screen
        self.play_image = pygame.image.load("ASSETS/Buttons/play_button_blue.png").convert_alpha()
        self.play_image_blur = pygame.image.load("ASSETS/Buttons/play_button_blue_fade.png").convert_alpha()
        self.play_rec = self.play_image.get_rect(midbottom=(100,740))
        self.visible_play = True

        self.hit_image = pygame.image.load("ASSETS/Buttons/hit_button_blue.png").convert_alpha()
        self.hit_rec = self.hit_image.get_rect(midbottom=(200,740))
        self.visible_hit = True

        self.stand_image = pygame.image.load("ASSETS/Buttons/stand_button_blue.png").convert_alpha()
        self.stand_rec = self.stand_image.get_rect(midbottom=(300,740))
        self.visible_stand = True

        self.double_image = pygame.image.load("ASSETS/Buttons/doubledown_button_blue.png").convert_alpha()
        self.double_rec = self.double_image.get_rect(midbottom=(400,740))

        self.reset_image = pygame.image.load("ASSETS/Buttons/new_reset3.5.png").convert_alpha()
        self.reset_rec = self.reset_image.get_rect(midright=(1200,715))

    def draw_buttons(self):
        if self.visible_play is True:
            self.screen.blit(self.play_image,self.play_rec)
        else:
            self.screen.blit(self.play_image_blur, self.play_rec)

        if self.visible_hit is True:
            self.screen.blit(self.hit_image,self.hit_rec)

        if self.visible_stand is True:
            self.screen.blit(self.stand_image,self.stand_rec)

        self.screen.blit(self.double_image,self.double_rec)
        self.screen.blit(self.reset_image,self.reset_rec)

    def check_play(self):
        if self.visible_play is True:
            mouse_pos = pygame.mouse.get_pos()
            left, _, _ = pygame.mouse.get_pressed()
            if left:
                if self.play_rec.collidepoint(mouse_pos):
                    self.visible_play = False
                    return True
            else:
                return False

    def check_hit(self):
        if self.visible_hit is True:
            mouse_pos = pygame.mouse.get_pos()
            left,_,_ = pygame.mouse.get_pressed()
            if left:
                if self.hit_rec.collidepoint(mouse_pos):
                    return True
            else:
                return False

    def check_stand(self):
        if self.visible_stand is True:
            mouse_pos = pygame.mouse.get_pos()
            left, _, _ = pygame.mouse.get_pressed()
            if left:
                if left:
                    if self.stand_rec.collidepoint(mouse_pos):
                        return True
            else:
                return False

    def check_double(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.double_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_reset(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, Right = pygame.mouse.get_pressed()
        if left:
            if self.reset_rec.collidepoint(mouse_pos):
                return True
        else:
            return False


class Window:
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.Font("ASSETS/fonts/IndianPoker.ttf",18)

    def bet_message(self,text="hanzala choose your bet"):
        surf = self.font.render(f"{text}", False, "green")
        surf_rect = surf.get_rect(topright=(1190, 10))
        self.screen.blit(surf, surf_rect)

    def player_turn(self):
        surf = self.font.render(f"TURN",False,"white")
        surf_rect = surf.get_rect(topright=(650,15))
        self.screen.blit(surf,surf_rect)

    def player_turn_text(self,text=""):
        surf = self.font.render(f"{text}",False,"green")
        surf_rect = surf.get_rect(topright=(830,10))
        self.screen.blit(surf,surf_rect)

    def input_player1_msg(self,msg):
        surf = self.font.render(f"{msg}", False, "green")
        surf_rect = surf.get_rect(topright=(490,490))
        self.screen.blit(surf, surf_rect)

    def input_player2_msg(self,msg):
        surf = self.font.render(f"{msg}", False, "green")
        surf_rect = surf.get_rect(topright=(1160,490))
        self.screen.blit(surf, surf_rect)

    def input_dealer_msg(self,msg):
        surf = self.font.render(f"{msg}", False, "green")
        surf_rect = surf.get_rect(topright=(490, 180))
        self.screen.blit(surf, surf_rect)

    def total_coins_player1(self,coins_remaining):
        surf = self.font.render(f"{coins_remaining}", False, "green")
        surf_rect = surf.get_rect(topright=(530, 525))
        self.screen.blit(surf, surf_rect)

    def bet_player1(self, total_bet):
        surf = self.font.render(f"{total_bet}", False, "green")
        surf_rect = surf.get_rect(topright=(525, 555))
        self.screen.blit(surf, surf_rect)

    def total_coins_player2(self,coins_remaining):
        surf = self.font.render(f"{coins_remaining}", False, "green")
        surf_rect = surf.get_rect(topright=(1170, 530))
        self.screen.blit(surf, surf_rect)

    def bet_player2(self, total_bet):
        surf = self.font.render(f"{total_bet}", False, "green")
        surf_rect = surf.get_rect(topright=(1160, 555))
        self.screen.blit(surf, surf_rect)

    def show_game_info(self):
        game_info = self.font.render(f"Press Space to Start The Game", False, "red")
        game_info_rec = game_info.get_rect(topleft=(500, 50))
        self.screen.blit(game_info, game_info_rec)
