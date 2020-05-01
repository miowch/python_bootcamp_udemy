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

    dealer_hand = dealer.calculate_hand()
    player_hand = player.calculate_hand()

    if dealer_hand < player_hand:
        prize = player.get_bet()

        print('\n🎉 Player beats the dealer! 🎉\nHere player\'s cards are:')
        player.face_up_hand()
        print('\nAgainst dealer\'s cards:')
        dealer.face_up_hand()

        player.get_payoff()
        dealer.remove_bet()
        print(f'\n✨ Player wins {prize} ✨')
    elif dealer_hand > player_hand:
        loss = player.get_bet()

        print('\n🤡 Dealer beats the player! 🤡\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()

        player.loss_deduction()
        dealer.remove_bet()
        if player.get_balance() == 0:
            print('💩 Player loses all their money! 💩')
        else:
            print(f'\n💩 Player loses {loss} 💩')
    else:
        print('\nHere dealer\'s cards are:')
        dealer.face_up_hand()
        print('\nAgainst player\'s cards:')
        player.face_up_hand()
        dealer.remove_bet()
        print('\n🤝 Standoff! 🤝')


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


def is_21_exceeded(participant):
    """Return whether a participant busts."""
    return participant.calculate_hand() > 21


def bust_dealer(bet, dealer, player):
    print('\nDealer busts!')
    dealer.face_up_hand()
    player.get_payoff()
    dealer.remove_bet()
    print(f'\n🎉 Player win {bet}! 🎉')


def bust_player(bet, dealer, player):
    print('\nLooks like your hand value exceeds 21:')
    player.face_up_hand()
    player.loss_deduction()
    dealer.remove_bet()
    if player.get_balance() == 0:
        print(f'\n💩 Player busts and loses all their money! Dealer wins! 💩')
    else:
        print(f'\n💩 Player busts and loses {bet}! Dealer wins! 💩')


def play_again(deck, dealer, player):
    """Suggest player continue the game."""
    if str(input('\nDo you want to play again?\nEnter Yes or No. ')).lower() == 'yes':
        return True
    print('\n🙃 See you later! Bye-bye! 🙂')
    return False


def gather_cards(deck, dealer, player):
    deck.assemble()
    dealer.empty_hand()
    player.empty_hand()


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
        if not is_21_exceeded(player):
            dealer_makes_moves(deck, dealer)
            if not is_21_exceeded(dealer):
                compare_hands(dealer, player)
            else:
                bust_dealer(bet, dealer, player)
        else:
            bust_player(bet, dealer, player)


def run_game():
    """Run the game."""
    player = Player(10)
    dealer = Dealer()
    deck = Deck()

    while True:
        blackjack(deck, dealer, player)

        if player.get_balance() <= 0 or not play_again(deck, dealer, player):
            break
        else:
            gather_cards(deck, dealer, player)


if __name__ == '__main__':
    run_game()
