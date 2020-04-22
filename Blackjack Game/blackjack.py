"""Player goal: get closer to a total value of 21 than the dealer."""

from Player import Player
from Dealer import Dealer
from Deck import Deck

PLAYER = Player(10)
DEALER = Dealer()
deck = Deck()


def draw_cards():
    """Hand out cards to all and face up dealer's top card."""
    PLAYER.hit(deck)
    PLAYER.hit(deck)

    DEALER.hit(deck)
    DEALER.hit(deck)

    print('\nThe cards are dealt!\n')

    DEALER.face_up_top_card()


def player_makes_moves():
    """Player chooses whether hit or stay while value of their hand less than 21."""
    while PLAYER.calculate_hand() < 21:
        print('\nPlayer, you have following cards in your hand:')
        PLAYER.face_up_hand()

        player_action = str(input('\nHIT or STAY? ')).lower()

        if player_action == 'hit':
            PLAYER.hit(deck)
        elif player_action == 'stay':
            break
        else:
            print('\nPlease, enter your action.')
            continue


def dealer_makes_moves():
    """Dealer hits while value of their hand less than 17."""
    while DEALER.calculate_hand() < 17:
        DEALER.hit(deck)


def compare_hands(bet):
    """Compare hands and return game result from player's perspective."""
    if DEALER.calculate_hand() < PLAYER.calculate_hand():
        print('\nPlayer beats the dealer! Here player\'s cards are:')
        PLAYER.face_up_hand()
        print('\nAgainst dealer\'s cards:')
        DEALER.face_up_hand()
        PLAYER.get_payoff(bet)
        DEALER.remove_bet()
        return print(f'\nPlayer wins {bet}')
    if DEALER.calculate_hand() > PLAYER.calculate_hand():
        print('\nDealer beats the player! Here dealer\'s cards are:')
        DEALER.face_up_hand()
        print('\nAgainst player\'s cards:')
        PLAYER.face_up_hand()
        PLAYER.loss_deduction(bet)
        DEALER.remove_bet()
        if PLAYER.get_balance() == 0:
            return print('Player loses all their money!')
        return print(f'\nPlayer loses {bet}')

    if DEALER.calculate_hand() == PLAYER.calculate_hand():
        print('\nHere dealer\'s cards are:')
        DEALER.face_up_hand()
        print('\nAgainst player\'s cards:')
        PLAYER.face_up_hand()
        DEALER.remove_bet()
        return print('\nStandoff!')


def is_blackjack(bet):
    """The player is paid out immediately, if it is blackjack."""
    if PLAYER.calculate_hand() == 21:
        print('\nCongratulations! Blackjack!')
        PLAYER.face_up_hand()
        PLAYER.get_payoff(bet)
        DEALER.remove_bet()
        print(f'\nPlayer wins {bet}!')
        return True
    else:
        return False


def check_bust(bet):
    """Return whether a participant busts."""
    if PLAYER.calculate_hand() > 21:
        print('\nLooks like your hand value exceeds 21:')
        PLAYER.face_up_hand()
        PLAYER.loss_deduction(bet)
        DEALER.remove_bet()
        if PLAYER.get_balance() == 0:
            print(f'\nPlayer busts and loses all their money! Dealer wins!')
        else:
            print(f'\nPlayer busts and loses {bet}! Dealer wins!')
        return True
    if DEALER.calculate_hand() > 21:
        print('\nDealer busts!')
        DEALER.face_up_hand()
        PLAYER.get_payoff(bet)
        DEALER.remove_bet()
        print(f'\nPlayer win {bet}!')
        return True
    else:
        return False


def play_again():
    """Suggest player continue the game."""
    if str(input('\nDo you want to play again?\nEnter Yes or No. ')).lower() == 'yes':
        global deck
        deck = Deck()
        PLAYER.empty_hand()
        DEALER.empty_hand()
        return True
    else:
        print('\nSee you later! Bye-bye!')
        return False


def blackjack():
    """Game logic."""
    print('Welcome to Blackjack Game!\nPlayer goes first!\n' +
          'Player goal: get closer to a total value of 21 than the dealer does.\n')

    print(f'\nPlayer has {PLAYER.get_balance()} coins.')
    bet = PLAYER.place_bet()
    DEALER.accept_bet(bet)

    draw_cards()

    if not is_blackjack(bet):
        player_makes_moves()
        if not check_bust(bet):
            dealer_makes_moves()
            if not check_bust(bet):
                compare_hands(bet)


while True:
    blackjack()

    if PLAYER.get_balance() <= 0 or not play_again():
        break
