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


def blackjack():
    print('Welcome to Blackjack Game!\nPlayer goes first!\n' +
          'Player goal: get closer to a total value of 21 than the dealer does.\n')

    print(f'\nPlayer has {player.get_balance()} coins.')
    bet = player.place_bet()
    dealer.accept_bet(bet)

    draw_cards()

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

    if player.calculate_hand() > 21:
        print('\nLooks like your hand value exceeds 21:')
        player.face_up_hand()
        player.loss_deduction(bet)
        dealer.remove_bet()
        return print(f'\nPlayer busts and loses {bet}! Dealer wins!')
    elif player.calculate_hand() == 21 and player.count_cards_in_hand() == 2:
        print('\nCongratulations! Blackjack!')
        player.face_up_hand()
        player.get_payoff(bet)
        dealer.remove_bet()
        return print(f'\nPlayer wins {bet}!')

    while dealer.calculate_hand() < 21:
        if dealer.calculate_hand() < player.calculate_hand():
            dealer.hit(deck)
        elif dealer.calculate_hand() == player.calculate_hand():
            print('\nStandoff! Here dealer\'s cards are:')
            dealer.face_up_hand()
            print('\nAgainst player\'s cards:')
            player.face_up_hand()
            dealer.remove_bet()
            break
        else:
            print('\nDealer beats the player! Here dealer\'s cards are:')
            dealer.face_up_hand()
            print('\nAgainst player\'s cards:')
            player.face_up_hand()
            player.loss_deduction(bet)
            dealer.remove_bet()
            return print(f'\nPlayer loses {bet}')

    if dealer.calculate_hand() > 21:
        print('\nDealer busts!')
        dealer.face_up_hand()
        player.get_payoff(bet)
        dealer.remove_bet()
        return print(f'\nPlayer win {bet}!')

    if player.calculate_hand() == dealer.calculate_hand() == 21:
        print('\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()
        dealer.remove_bet()
        return print('\nStandoff!')


while True:
    blackjack()

    if player.get_balance() > 0:
        play_again = str(input('\nDo you want to play again?\nEnter Yes or No. ')).lower()

        if play_again == 'yes':
            deck.assemble()
            player.empty_hand()
            dealer.empty_hand()
        else:
            print('\nSee you later! Bye-bye!')
            break
