import pygame
from sys import exit
from screen_buttons import Buttons,Screen,Window
from Cards_Coins import Cards,Coins


class Player1:
    def __init__(self):
        self.hand = []
        self.back_image = pygame.image.load("ASSETS/BACK CARDS/cardback.png").convert_alpha()
        self.total_coins = 1000
        self.round_bet = 0
        self.register_bet = False
        self.bet_turn = False

    def get_first_cards(self):
        """
        this gets images paths from deck list and make then into pygame surfaces
        and then stored them in a list where key will be file path and value will be pygame surface
        it is done so hand value can be found easily
        """
        img1_p,img2_p = deck.deal_first_cards()
        img1 = pygame.image.load(img1_p).convert_alpha()
        img2 = pygame.image.load(img2_p).convert_alpha()
        self.hand.append({img1_p:img1})
        self.hand.append({img2_p:img2})

    def display_hand(self,x_position,position_y):
        """
        this will display card on the screen using a for loop  and update x position by 80
        to give them space it will be updated each time player hit or double bet
        """
        for card in self.hand:
            for key,value in card.items():
                screen.blit(card[key],(x_position,position_y))
                x_position += 80

    def add_card(self):
        # same as get first cards it's going to return one image file path and mak e surface of it and
        # save into hand list which will be later drawn on screen using display() function
        img__ = deck.deal_one_card()
        img1 = pygame.image.load(img__).convert_alpha()
        self.hand.append({img__:img1})

    def return_hand(self):
        # return hand so hand value can be found
        return self.hand

    def check_playable(self):
        """
        it's going to return TRUE if  whether player has hit stay button or it's card hand
        value is greater than 21, so it can change player_turn to false else player has to do it manually
        """
        if buttons.check_stand() is True or deck.total_hands(self.hand) >= 21:
            return True
        else:
            return False

    def take_bet(self):
        """
        if player click on certain chips image it going add that to total  of player round
        it will keep  adding until player has  register bet so game can go on it can do that by clicking on bet image
        """
        global bet_msg
        if self.register_bet is False:
            if self.round_bet > self.total_coins:
                self.round_bet = 0
                bet_msg = "can,t bet more > total chips"
            if coins.check_5_coin() is True:
                self.round_bet += 5
            if coins.check_10_coin() is True:
                self.round_bet += 10
            if coins.check_20_coin() is True:
                self.round_bet += 20
            if coins.check_50_coin() is True:
                self.round_bet += 50
            if coins.check_100_coin() is True:
                self.round_bet += 100
        return self.round_bet

    def adding_removing_bet(self):
        """
        after winner has been decided if player has won the game it will add if loss it will cut it from total coins
        green winner
        "" or white = loss
        orange = blackjack
        """
        if check_winner.game_end is False:
            if check_winner.player1_state == "green":
                self.total_coins += self.round_bet
            elif check_winner.player1_state == "" or check_winner.player1_state == "white":
                self.total_coins -= self.round_bet
            elif check_winner.player1_state == "orange":
                self.total_coins += self.round_bet * 3.25

    def back_cards(self,x_pos,y_pos):
        """
        will show back card image when user registering bet
        """
        screen.blit(self.back_image,(x_pos,y_pos))
        x_pos += 80
        screen.blit(self.back_image,(x_pos,y_pos))


class Player2(Player1):
    """
    this player2 class will inherit all function and attribute from player 1 class
    except removing or adding to total coins
    """
    def __init__(self):
        super().__init__()

    def adding_or_losing(self):
        if check_winner.game_end is False:
            if check_winner.player2_state == "green":
                self.total_coins += self.round_bet
            elif check_winner.player2_state == "" or check_winner.player2_state == "white":
                self.total_coins -= self.round_bet
            elif check_winner.player2_state == "orange":
                self.total_coins += self.round_bet * 3.25


class Dealer(Player1):
    def __init__(self):
        super().__init__()
        """
        using get first card() func from parent class 
        also using add card() and return hand and back card() function
        from parent class and over writing display hand () fun 
        """
        self.show_value = False
        self.y_position = 50
        self.show_initial_hand = True

    def dealer_initial_hand(self):
        """
        this will only show when it,s players turn after that it will be removed
        """
        if self.show_initial_hand:
            screen.blit(self.back_image,(0,50))
            for key,value in self.hand[1].items():
                screen.blit(self.hand[1][key],(80,50))

    def display_hand(self,x_position,position_y):
        if self.show_initial_hand is False:
            for card in self.hand:
                for key,value in card.items():
                    screen.blit(card[key], (x_position, self.y_position))
                    x_position += 80

    def dealer_take_cards(self):
        """
        this will take cards from the deck and add them to dealer hand until
        dealer hand value is greater than 16
        """
        # dealer will not take cards from deck if both player are busted if one is busted it will take cards if both it will not
        if check_winner.player1_out is False or check_winner.player2_out is False:
            global dealer_turn
            while dealer_turn is True and deck.total_hands(self.hand) <= 16:
                self.add_card()
                if deck.total_hands(self.hand) >= 17:
                    self.show_value = True


class CHECKWINNERS:
    def __init__(self):
        """
        here all player hand will be compared to dealer if winner decided game end will be false
        using color scheme if user win loss or equal or black just because I am lazy
        white or "" = loss
        blue = TIE Hand
        green = winner
        orange means blackjack
        """
        self.game_end = True
        self.show_winner = False
        self.player1_out = False
        self.player2_out = False
        self.dealer_out = False
        self.player1_state = ""
        self.player2_state = ""
        self.dealer_state = ""

    def end_game_round(self):
        """
        just for so I don't have type it 2 or 3 times
        """
        if self.game_end is False:
            self.player1_out = True
            self.player2_out = True
            self.dealer_out = True

    def check_black_jack(self):
        if self.show_winner is True and self.game_end is True:
            if deck.total_hands(hand3) == 21 and len(hand3) == 2:
                self.game_end = False
                self.dealer_out = True
                self.dealer_state = "orange"

            if deck.total_hands(hand1) == 21 and len(hand1) == 2 and deck.total_hands(hand3) != 21:
                self.player1_state = "orange"
                self.player1_out = True

            if deck.total_hands(hand2) == 21 and len(hand2) == 2 and deck.total_hands(hand3) != 21:
                self.player2_out = True
                self.player2_state = "orange"

            if deck.total_hands(hand1) == 21 and len(hand1) == 2 and deck.total_hands(hand3) == 21:
                self.player1_state = "blue"
                self.dealer_state = "blue"
                self.player1_out = True

            if deck.total_hands(hand2) == 21 and len(hand2) == 2 and deck.total_hands(hand3) == 21:
                self.player2_out = True
                self.player2_state = "blue"
                self.dealer_state = "blue"

    def check_busted(self):
        if self.show_winner is True and self.game_end is True:
            if deck.total_hands(hand1) > 21:
                self.player1_out = True
                self.player1_state = "white"

            if deck.total_hands(hand2) > 21:
                self.player2_out = True
                self.player2_state = "white"

            if deck.total_hands(hand3) > 21:
                self.dealer_out = True
                self.dealer_state = "white"

            # 4 both players wins
            if deck.total_hands(hand3) > 21 and self.player1_out is False and self.player2_out is False:
                self.player1_state = "green"
                self.player2_state = "green"
                self.game_end = False
                self.end_game_round()

    def check_equal(self):
        if self.show_winner is True and self.game_end is True:
            if deck.total_hands(hand3) == deck.total_hands(hand1) and deck.total_hands(hand3) == deck.total_hands(hand2) and self.dealer_out is False and self.player1_out is False and self.player2_out is False:
                self.player1_state = "blue"
                self.player2_state = "blue"
                self.dealer_state = "blue"

                self.game_end = False
                self.end_game_round()

            elif deck.total_hands(hand1) == deck.total_hands(hand3) and self.player1_out is False:
                self.player1_out = True
                self.player1_state = "blue"

            elif deck.total_hands(hand2) == deck.total_hands(hand3) and self.player2_out is False:
                self.player2_out = True
                self.player2_state = "blue"

    def compare_hands(self):
        if self.show_winner is True and self.game_end is True:
            # 1 if dealer hands is greater than both
            if deck.total_hands(hand3) > deck.total_hands(hand1) and deck.total_hands(hand3) > deck.total_hands(hand2) and self.dealer_out is False and self.player1_out is False and self.player2_out is False:
                self.dealer_state = "green"
                self.game_end = False

            # 4 : if both player hand is greater than dealer
            elif deck.total_hands(hand1) > deck.total_hands(hand3) and deck.total_hands(hand2) > deck.total_hands(hand3) and self.player1_out is False and self.player2_out is False and self.dealer_out is False:
                self.player1_state = "green"
                self.player2_state = "green"
                self.game_end = False

            # 1: if dealer is not busted and both players are busted
            elif self.player2_out is True and self.player1_out is True and self.dealer_out is False:
                self.dealer_state = "green"
                self.game_end = False

            # 0:  if all players are busted
            elif self.player2_out is True and self.player1_out is True and self.dealer_out is True:
                self.game_end = False

            # 1: if dealer hand is greater than hanzala and ahmad is dead
            elif deck.total_hands(hand3) > deck.total_hands(hand1) and self.dealer_out is False and self.player1_out is False and self.player2_out is True:
                self.dealer_state = "green"
                self.game_end = False

            # 1:  if dealer hand is greater than ahmad and hanzala is dead
            elif deck.total_hands(hand3) > deck.total_hands(hand2) and self.dealer_out is False and self.player2_out is False and self.player1_out is True:
                self.dealer_state = "green"
                self.game_end = False

            # 2: if hanzala hand is greater than dealer and ahmad dead
            elif deck.total_hands(hand1) > deck.total_hands(hand3) and self.player1_out is False and self.player2_out is True and self.dealer_out is False:
                self.player1_state = "green"
                self.game_end = False

            # 2: if hanzala hand is greater than dealer but ahmad is not
            elif deck.total_hands(hand1) > deck.total_hands(hand3) > deck.total_hands(hand2) and self.player1_out is False and self.player2_out is False and self.dealer_out is False:
                self.player1_state = "green"
                self.game_end = False

            # 2:  if only hanzala is alive
            elif self.player1_out is False and self.player2_out is True and self.dealer_out is True:
                self.player1_state = "green"
                self.game_end = False

            # 3: if ahmad hand is greater than dealer and hanzala is dead
            elif deck.total_hands(hand2) > deck.total_hands(hand3) and self.player2_out is False and self.dealer_out is False and self.player1_out is True:
                self.player2_state = "green"
                self.game_end = False

            # 3: if ahmad is greater than dealer but hanzala is not
            elif deck.total_hands(hand2) > deck.total_hands(hand3) > deck.total_hands(hand1) and self.player2_out is False and self.dealer_out is False and self.player1_out is False:
                self.player2_state = "green"
                self.game_end = False

            #3: if only ahmad is alive
            elif self.player1_out is True and self.player2_out is False and self.dealer_out is True:
                self.player2_state = "green"
                self.game_end = False
            else:
                self.player1_state = "red"
                self.player2_state = "red"
                self.dealer_state = "red"

    def show_line_colors(self):
        main_screen.player1_win_equal_loss(self.player1_state)
        main_screen.player2_win_equal_loss(self.player2_state)
        main_screen.dealer_win_equal_loss(self.dealer_state)

    def show_each_message(self):
        if self.player1_state == "green":
            msg = "Hanzala you win"
            result.input_player1_msg(msg)
        elif self.player1_state == "" or self.player1_state == "white":
            msg = "Hanzala Lost"
            result.input_player1_msg(msg)
        elif self.player1_state == "blue":
            msg = "Tie Hand == Dealer"
            result.input_player1_msg(msg)

        elif self.player1_state == "orange":
            msg = " Black Black!!"
            result.input_player1_msg(msg)

        if self.player2_state == "green":
            msg = "Ahmad you win"
            result.input_player2_msg(msg)
        elif self.player2_state == "" or self.player2_state == "white":
            msg = "Ahmad Lost"
            result.input_player2_msg(msg)
        elif self.player2_state == "blue":
            msg = "Tie Hand == Dealer"
            result.input_player2_msg(msg)
        elif self.player2_state == "orange":
            msg = "Black Black!!"
            result.input_player2_msg(msg)

        if self.dealer_state == "green":
            msg = "Dealer WINS"
            result.input_dealer_msg(msg)
        elif self.dealer_state == "" or self.dealer_state == "white":
            msg = "Dealer Lost"
            result.input_dealer_msg(msg)
        elif self.dealer_state == "blue":
            msg = "Tie Hand == PLAYERS"
            result.input_dealer_msg(msg)
        elif self.dealer_state == "orange":
            msg = "Black Black!!"
            result.input_dealer_msg(msg)


def reset():
    """
    when user clicks on rest button after round is finished it will rest the screen so players can bet again
    """
    global value1,value2,value3,show_play,hanzala_turn,ahmad_turn,dealer_turn,turn,bet_msg
    player1.hand = []
    player2.hand = []
    dealer.hand = []
    player1.round_bet = 0
    player2.round_bet = 0
    player1.register_bet = False
    player2.register_bet = False
    player1.bet_turn = True
    player2.bet_turn = False
    value1 = 0
    value2 = 0
    value3 = 0
    hanzala_turn = False
    ahmad_turn = False
    dealer_turn = False
    dealer.show_initial_hand = True
    check_winner.show_winner = False
    check_winner.game_end = True
    check_winner.player1_out = False
    check_winner.player2_out = False
    check_winner.dealer_out = False
    buttons.visible_play = True
    check_winner.player1_state = ""
    check_winner.player2_state = ""
    check_winner.dealer_state = ""
    turn = ""
    bet_msg = "Hanzala choose your bet"
    show_play = False


# BASIC Setup
pygame.init()
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("BlackJack BY Hanzala")
frame_rate = pygame.time.Clock()

#classes
main_screen = Screen(screen)
buttons = Buttons(screen)
deck = Cards(screen)
result = Window(screen)
check_winner = CHECKWINNERS()
coins = Coins(screen)
player1 = Player1()
player2 = Player2()
dealer = Dealer()

# bool VALUES
Game_rolling = False
show_play = False
add_remove_chips = False
# using bool values to keep track of player and dealer turn
hanzala_turn = False
ahmad_turn = False
dealer_turn = False

value1 = 0# for player1
value2 = 0# player2
value3 = 0# dealer
turn = ""
bet_msg = ""

# adding user event, so it can be trigger by pygame to add or remove players chips
ADDREMOVECHIPS = pygame.USEREVENT
pygame.time.set_timer(ADDREMOVECHIPS,500)

#background
bg_image = pygame.image.load("ASSETS/BACKGROUND/R.jpg").convert_alpha()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.bet_turn = True
                bet_msg = "Hanzala choose your bet"
                Game_rolling = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player1.bet_turn is True:
                player1.take_bet()
                if player1.round_bet >= 5:
                    if coins.check_register_bet() is True:
                        bet_msg = "Ahmad choose your bet"
                        player1.register_bet = True
                        player2.bet_turn = True
                        player1.bet_turn = False

            elif player2.bet_turn is True:
                player2.take_bet()
                if player2.round_bet >= 5:
                    if coins.check_register_bet() is True:
                        player2.register_bet = True
                        player2.bet_turn = False
            """
            this if statement will check whether play button
            has been clicked if true it will deal all players including dealer 
            their initial two cards so game can start 
            """
            if player2.register_bet is True and player1.register_bet is True:
                bet_msg = "click play to start the game"
                if buttons.check_play():
                    player1.get_first_cards()
                    player2.get_first_cards()
                    dealer.get_first_cards()
                    turn = "HANZALA TURN"
                    hanzala_turn = True
                    show_play = True

            if hanzala_turn is True:
                bet_msg = "Press stand to pass turn"
                """
                first turn will be of hanzala it will first check if hit 
                button has been clicked if true or also check double button if true it will add card to player hand 
                list and then it will check player has click stay button or player card 
                value is greater than 21 if True it will change hanzala turn to false 
                and ahmad turn to true so game can progress further  
                """
                if buttons.check_hit():
                    player1.add_card()

                if buttons.check_double() and len(player1.hand) == 2:
                    player1.add_card()
                    player1.round_bet += player2.round_bet
                    hanzala_turn = False
                    turn = "AHMAD TURN"
                    ahmad_turn = True

                if player1.check_playable():
                    hanzala_turn = False
                    turn = "AHMAD TURN"
                    ahmad_turn = True

            elif ahmad_turn is True:
                """"
                here alot of bool alot of bool values are change  because it is  last player
                the if statement are same as hanzala  2nd bool will show dealer full cards not hiding anything 
                3rd will make dealer take cards from deck until value it's greater than 16
                4th will show dealer hand value on screen which was hidden until now
                5th will enable check_winner if statements so winner can be decided
                """
                if buttons.check_hit():
                    player2.add_card()

                if buttons.check_double() and len(player2.hand) == 2:
                    player2.add_card()

                if player2.check_playable():
                    add_remove_chips = True
                    turn = "DEALER TURN"
                    ahmad_turn = False
                    dealer.show_initial_hand = False
                    dealer.show_value = True
                    dealer_turn = True
                    check_winner.show_winner = True

        if event.type == ADDREMOVECHIPS:
            if add_remove_chips is True:
                player1.adding_removing_bet()
                if player1.total_coins < 5:
                    player1.total_coins = 1000
                player2.adding_or_losing()
                if player2.total_coins < 5:
                    player2.total_coins = 1000
                add_remove_chips = False

    if Game_rolling:
        """
         this will just display back image and lines and back cards will draw all buttons
         before player press play button when player press play button show play if statement will always
         be true until the round end so images can stay on the screen.
         """
        main_screen.draw_main_screen()
        player1.back_cards(0,360)
        player1.back_cards(555,360)
        dealer.back_cards(0,50)
        buttons.draw_buttons()
        coins.show_buttons()

        result.total_coins_player1(player1.total_coins)
        result.total_coins_player2(player2.total_coins)
        result.bet_player1(player1.round_bet)
        result.bet_player2(player2.round_bet)

        result.player_turn()
        result.bet_message(bet_msg)
        if show_play:
            "this is main loop of game"
            result.player_turn_text(turn)
            player1.display_hand(0,360)# this will display player1 hand
            player2.display_hand(555,360) # this will display player2 hand
            dealer.dealer_initial_hand() # if true it will show only dealer one card
            dealer.display_hand(0,50) # on contrast when it is false it will show dealer full hand

            hand1 = player1.return_hand() # this 3 lines will return both player hand and dealer hand, so it be used to decide winner
            hand2 = player2.return_hand()
            hand3 = dealer.return_hand()

            value1 = deck.total_hands(hand1) # this three lines will both player  and dealer value, so after it  be display on screen
            value2 = deck.total_hands(hand2)
            value3 = deck.total_hands(hand3)

            deck.reshuffle_deck() # to reshuffle deck

            if dealer.show_value:
                main_screen.hand_value_dealer(value3)
            main_screen.hand_value_hanzala(value1)
            main_screen.hand_value_ahmad(value2)

            if dealer_turn is True:
                check_winner.check_black_jack()
                check_winner.check_busted()
                dealer.dealer_take_cards()  # so dealer can get  multiple cards if cards  value is less than 17
                check_winner.check_equal()
                check_winner.compare_hands()
                check_winner.show_each_message()

            if check_winner.game_end is False:
                bet_msg = "click reset to restart game"
                check_winner.show_line_colors()
                if buttons.check_reset():
                    add_remove_chips = False
                    reset()
    else:
        screen.blit(bg_image,(0,0))
        result.show_game_info()

    pygame.display.update()
    frame_rate.tick(60)
