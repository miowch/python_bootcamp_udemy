"""Player goal: get closer to a total value of 21 than the dealer."""

from Player import Player
from Dealer import Dealer
from Deck import Deck


def draw_cards(deck, dealer, player):
    """Hand out cards to all and face up dealer's top card."""
    for i in range(1, 3):
        player.hit(deck)
        dealer.hit(deck)
        i += 1

    print('\nThe cards are dealt!\n')
    dealer.face_up_top_card()


def player_makes_moves(deck, player):
    """Player chooses whether hit or stay while value of their hand less than 21."""
    while player.calculate_hand() < 21:
        print('\nPlayer, you have following cards in your hand:')
        player.face_up_hand()
        action = str(input('\nHIT or STAY? ')).lower()
        if action == 'hit':
            player.hit(deck)
        elif action == 'stay':
            break
        else:
            print('\nPlease, enter your action.')
            continue


def dealer_makes_moves(deck, dealer):
    """Dealer hits while value of their hand less than 17."""
    while dealer.calculate_hand() < 17:
        dealer.hit(deck)


def compare_hands(dealer, player):
    """Compare hands and return game result from player's perspective."""
    if dealer.calculate_hand() < player.calculate_hand():
        prize = player.get_bet()

        print('\n🎉 Player beats the dealer! 🎉\nHere player\'s cards are:')
        player.face_up_hand()
        print('\nAgainst dealer\'s cards:')
        dealer.face_up_hand()

        player.get_payoff()
        dealer.remove_bet()
        return print(f'\n✨ Player wins {prize} ✨')
    if dealer.calculate_hand() > player.calculate_hand():
        loss = player.get_bet()

        print('\n🤡 Dealer beats the player! 🤡\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()

        player.loss_deduction()
        dealer.remove_bet()
        if player.get_balance() == 0:
            return print('💩 Player loses all their money! 💩')
        return print(f'\n💩 Player loses {loss} 💩')

    if dealer.calculate_hand() == player.calculate_hand():
        print('\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()
        dealer.remove_bet()
        return print('\n🤝 Standoff! 🤝')


def is_blackjack(dealer, player):
    """The player is paid out immediately, if it is blackjack."""
    if player.calculate_hand() == 21:
        prize = player.get_bet()
        print('\n😎 Congratulations! Blackjack! 😎')
        player.face_up_hand()
        player.get_payoff()
        dealer.remove_bet()
        print(f'\n✨ Player wins {prize}! ✨')
        return True
    return False


def check_bust(dealer, player):
    """Return whether a participant busts."""
    bet = player.get_bet()
    if player.calculate_hand() > 21:
        print('\nLooks like your hand value exceeds 21:')
        player.face_up_hand()
        player.loss_deduction()
        dealer.remove_bet()
        if player.get_balance() == 0:
            print(f'\n💩 Player busts and loses all their money! Dealer wins! 💩')
        else:
            print(f'\n💩 Player busts and loses {bet}! Dealer wins! 💩')
        return True
    if dealer.calculate_hand() > 21:
        print('\nDealer busts!')
        dealer.face_up_hand()
        player.get_payoff()
        dealer.remove_bet()
        print(f'\n🎉 Player win {bet}! 🎉')
        return True
    return False


def play_again(deck, dealer, player):
    """Suggest player continue the game."""
    if str(input('\nDo you want to play again?\nEnter Yes or No. ')).lower() == 'yes':
        deck.assemble()
        player.empty_hand()
        dealer.empty_hand()
        return True
    print('\n🙃 See you later! Bye-bye! 🙂')
    return False


def blackjack(deck, dealer, player):
    """Game logic."""
    print('Welcome to Blackjack Game! 🍸\nPlayer goes first!\n' +
          'Player goal: get closer to a total value of 21 than the dealer does.\n')

    print(f'\nPlayer has {player.get_balance()} coins.')
    bet = player.place_bet()
    dealer.accept_bet(bet)

    draw_cards(deck, dealer, player)

    if not is_blackjack(bet, player):
        player_makes_moves(deck, player)
        if not check_bust(dealer, player):
            dealer_makes_moves(deck, dealer)
            if not check_bust(dealer, player):
                compare_hands(dealer, player)


def run_game():
    """Run the game."""
    player = Player(10)
    dealer = Dealer()
    deck = Deck()

    while True:
        blackjack(deck, dealer, player)

        if player.get_balance() <= 0 or not play_again(deck, dealer, player):
            break


if __name__ == '__main__':
    run_game()
