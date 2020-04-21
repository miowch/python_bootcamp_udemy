# Player goal: get closer to a total value of 21 than the dealer does

from Player import Player
from Dealer import Dealer
from Deck import Deck

player = Player()
dealer = Dealer()
deck = Deck()


def draw_cards():
    player.hit(deck)
    player.hit(deck)

    dealer.hit(deck)
    dealer.hit(deck)

    print('\nThe cards are dealt!\n')

    dealer.face_up_top_card()


def player_makes_moves():
    while player.calculate_hand() < 21:
        print('\nPlayer, you have following cards in your hand:')
        player.face_up_hand()

        player_action = str(input('\nHIT or STAY? ')).lower()

        if player_action == 'hit':
            player.hit(deck)
        elif player_action == 'stay':
            break
        else:
            print('\nPlease, enter your action.')
            continue


def dealer_makes_moves():
    while dealer.calculate_hand() < 17:
        dealer.hit(deck)


def compare_hands(bet):
    if dealer.calculate_hand() < player.calculate_hand():
        print('\nPlayer beats the dealer! Here player\'s cards are:')
        player.face_up_hand()
        print('\nAgainst dealer\'s cards:')
        dealer.face_up_hand()
        player.get_payoff(bet)
        dealer.remove_bet()
        return print(f'\nPlayer wins {bet}')
    elif dealer.calculate_hand() > player.calculate_hand():
        print('\nDealer beats the player! Here dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()
        player.loss_deduction(bet)
        dealer.remove_bet()
        if player.get_balance() != 0:
            return print(f'\nPlayer loses {bet}')
        else:
            return print('Player loses all their money!')
    elif dealer.calculate_hand() == player.calculate_hand():
        print('\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()
        dealer.remove_bet()
        return print('\nStandoff!')


def is_blackjack(bet):
    if player.calculate_hand() == 21:
        print('\nCongratulations! Blackjack!')
        player.face_up_hand()
        player.get_payoff(bet)
        dealer.remove_bet()
        print(f'\nPlayer wins {bet}!')
        return True
    else:
        return False


def check_bust(bet):
    if player.calculate_hand() > 21:
        print('\nLooks like your hand value exceeds 21:')
        player.face_up_hand()
        player.loss_deduction(bet)
        dealer.remove_bet()
        if player.get_balance() != 0:
            print(f'\nPlayer busts and loses {bet}! Dealer wins!')
            return True
        else:
            print(f'\nPlayer busts and loses all their money! Dealer wins!')
            return True
    elif dealer.calculate_hand() > 21:
        print('\nDealer busts!')
        dealer.face_up_hand()
        player.get_payoff(bet)
        dealer.remove_bet()
        print(f'\nPlayer win {bet}!')
        return True
    else:
        return False


def play_again():
    if str(input('\nDo you want to play again?\nEnter Yes or No. ')).lower() == 'yes':
        deck.assemble()
        player.empty_hand()
        dealer.empty_hand()
        return True
    else:
        print('\nSee you later! Bye-bye!')
        return False


def blackjack():
    print('Welcome to Blackjack Game!\nPlayer goes first!\n' +
          'Player goal: get closer to a total value of 21 than the dealer does.\n')

    print(f'\nPlayer has {player.get_balance()} coins.')
    bet = player.place_bet()
    dealer.accept_bet(bet)

    draw_cards()

    if not is_blackjack(bet):
        player_makes_moves()
        if not check_bust(bet):
            dealer_makes_moves()
            if not check_bust(bet):
                compare_hands(bet)


while True:
    blackjack()

    if player.get_balance() <= 0 or not play_again():
        break
