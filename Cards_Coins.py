import pygame
import os
import random


class Cards:
    def __init__(self,screen):
        self.images = self.creating_deck()
        self.screen = screen

    @staticmethod
    def creating_deck():
        img_list = []
        folder = "ASSETS/CARDS FRONTS/"

        for filename in os.listdir(folder):
            file_path = os.path.join(folder,filename)
            img_list.append(file_path)
        return img_list

    def deal_first_cards(self,num:int = 2):
        img = random.sample(self.images,num)
        r_img1,r_img2 = img
        self.images.remove(r_img1)
        self.images.remove(r_img2)
        return img

    def deal_one_card(self):
        img = random.sample(self.images,1)
        self.images.remove(*img)
        img = str(*img)
        return img

    @staticmethod
    def total_hands(hand):
        values = {
            "ASSETS/CARDS FRONTS/2_of_spades.png":2,
            "ASSETS/CARDS FRONTS/2_of_clubs.png":2,
            "ASSETS/CARDS FRONTS/2_of_hearts.png":2,
            "ASSETS/CARDS FRONTS/2_of_diamonds.png":2,
            "ASSETS/CARDS FRONTS/3_of_spades.png": 3,
            "ASSETS/CARDS FRONTS/3_of_clubs.png": 3,
            "ASSETS/CARDS FRONTS/3_of_hearts.png": 3,
            "ASSETS/CARDS FRONTS/3_of_diamonds.png": 3,
            "ASSETS/CARDS FRONTS/4_of_spades.png": 4,
            "ASSETS/CARDS FRONTS/4_of_clubs.png": 4,
            "ASSETS/CARDS FRONTS/4_of_hearts.png": 4,
            "ASSETS/CARDS FRONTS/4_of_diamonds.png": 4,
            "ASSETS/CARDS FRONTS/5_of_spades.png": 5,
            "ASSETS/CARDS FRONTS/5_of_clubs.png": 5,
            "ASSETS/CARDS FRONTS/5_of_hearts.png": 5,
            "ASSETS/CARDS FRONTS/5_of_diamonds.png": 5,
            "ASSETS/CARDS FRONTS/6_of_spades.png": 6,
            "ASSETS/CARDS FRONTS/6_of_clubs.png": 6,
            "ASSETS/CARDS FRONTS/6_of_hearts.png": 6,
            "ASSETS/CARDS FRONTS/6_of_diamonds.png": 6,
            "ASSETS/CARDS FRONTS/7_of_spades.png": 7,
            "ASSETS/CARDS FRONTS/7_of_clubs.png": 7,
            "ASSETS/CARDS FRONTS/7_of_hearts.png": 7,
            "ASSETS/CARDS FRONTS/7_of_diamonds.png": 7,
            "ASSETS/CARDS FRONTS/8_of_spades.png": 8,
            "ASSETS/CARDS FRONTS/8_of_clubs.png": 8,
            "ASSETS/CARDS FRONTS/8_of_hearts.png": 8,
            "ASSETS/CARDS FRONTS/8_of_diamonds.png": 8,
            "ASSETS/CARDS FRONTS/9_of_spades.png": 9,
            "ASSETS/CARDS FRONTS/9_of_clubs.png": 9,
            "ASSETS/CARDS FRONTS/9_of_hearts.png": 9,
            "ASSETS/CARDS FRONTS/9_of_diamonds.png": 9,
            "ASSETS/CARDS FRONTS/10_of_spades.png": 10,
            "ASSETS/CARDS FRONTS/10_of_clubs.png": 10,
            "ASSETS/CARDS FRONTS/10_of_hearts.png": 10,
            "ASSETS/CARDS FRONTS/10_of_diamonds.png": 10,
            "ASSETS/CARDS FRONTS/ace_of_spades.png": 11,
            "ASSETS/CARDS FRONTS/ace_of_clubs.png": 11,
            "ASSETS/CARDS FRONTS/ace_of_hearts.png": 11,
            "ASSETS/CARDS FRONTS/ace_of_diamonds.png": 11,
            "ASSETS/CARDS FRONTS/jack_of_spades.png": 10,
            "ASSETS/CARDS FRONTS/jack_of_clubs.png": 10,
            "ASSETS/CARDS FRONTS/jack_of_hearts.png": 10,
            "ASSETS/CARDS FRONTS/jack_of_diamonds.png": 10,
            "ASSETS/CARDS FRONTS/king_of_spades.png": 10,
            "ASSETS/CARDS FRONTS/king_of_clubs.png": 10,
            "ASSETS/CARDS FRONTS/king_of_hearts.png": 10,
            "ASSETS/CARDS FRONTS/king_of_diamonds.png": 10,
            "ASSETS/CARDS FRONTS/queen_of_spades.png": 10,
            "ASSETS/CARDS FRONTS/queen_of_clubs.png": 10,
            "ASSETS/CARDS FRONTS/queen_of_hearts.png": 10,
            "ASSETS/CARDS FRONTS/queen_of_diamonds.png": 10}
        hand_value = 0
        num_aces = 0
        for dick_list in hand:
            for key,value in dick_list.items():
                hand_value += values[key]
                if key in ["ASSETS/CARDS FRONTS/ace_of_diamonds.png","ASSETS/CARDS FRONTS/ace_of_clubs.png",
                           "ASSETS/CARDS FRONTS/ace_of_spades.png","ASSETS/CARDS FRONTS/ace_of_hearts.png"]:
                    num_aces += 1
            while num_aces > 0 and hand_value > 21:
                hand_value -= 10
                num_aces -= 1
        return hand_value

    def reshuffle_deck(self):
        if len(self.images) < 5:
            self.images = []
            self.images = self.creating_deck()


class Coins:
    def __init__(self,screen):
        self.screen = screen
        self.five_image = pygame.image.load("ASSETS/CHIPS/new5_coin.png").convert_alpha()
        self.five_rec = self.five_image.get_rect(midleft=(600,715))

        self.ten_image = pygame.image.load("ASSETS/CHIPS/new10_coin.png").convert_alpha()
        self.ten_rec = self.ten_image.get_rect(midleft=(660, 715))

        self.twenty_image = pygame.image.load("ASSETS/CHIPS/new20_coin.png").convert_alpha()
        self.twenty_rec = self.twenty_image.get_rect(midleft=(720, 715))

        self.fifty_image = pygame.image.load("ASSETS/CHIPS/new50_coin.png").convert_alpha()
        self.fifty_rec = self.fifty_image.get_rect(midleft=(780, 715))

        self.hundred_image = pygame.image.load("ASSETS/CHIPS/new100_coin.png").convert_alpha()
        self.hundred_rec = self.hundred_image.get_rect(midleft=(840, 715))

        self.bet_image = pygame.image.load("ASSETS/CHIPS/bet_3.png").convert_alpha()
        self.bet_rec = self.hundred_image.get_rect(midleft=(950, 710))

    def show_buttons(self):
        self.screen.blit(self.five_image,self.five_rec)
        self.screen.blit(self.ten_image,self.ten_rec)
        self.screen.blit(self.twenty_image,self.twenty_rec)
        self.screen.blit(self.fifty_image,self.fifty_rec)
        self.screen.blit(self.hundred_image,self.hundred_rec)
        self.screen.blit(self.bet_image,self.bet_rec)

    def check_5_coin(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.five_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_10_coin(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.ten_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_20_coin(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.twenty_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_50_coin(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.fifty_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_100_coin(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.hundred_rec.collidepoint(mouse_pos):
                return True
        else:
            return False

    def check_register_bet(self):
        mouse_pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        if left:
            if self.bet_rec.collidepoint(mouse_pos):
                return True
            else:
                return False
