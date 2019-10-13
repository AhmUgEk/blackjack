"""
Single player Blackjack game.
"""

# Imports:
from blackjack_classes import Card, Deck, Hand, Chips
from blackjack_functions import hit, hit_or_stand, replay, show_all, show_some, take_bet
from time import sleep


playing = True

print('Welcome to Blackjack!\n')

player_chips = Chips()

while True:

    playing_deck = Deck()
    playing_deck.shuffle()

    comp_hand = Hand()
    player_hand = Hand()

    comp_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())
    comp_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())

    print(player_chips)

    player_chips.bet = take_bet(player_chips)

    while playing:

        show_some(player_hand, comp_hand)

        player_choice = hit_or_stand(playing_deck, player_hand)

        if player_hand.value > 21:
            player_chips.lose_bet()
            print('Player busts!\n')
            break

        if player_choice == 'H':
            continue
        else:

            while comp_hand.value < 17:
                comp_hand.add_card(playing_deck.deal())
                show_all(player_hand, comp_hand)
                sleep(3)
                continue
            else:
                if comp_hand.value > 21:
                    show_all(player_hand, comp_hand)
                    player_chips.win_bet()
                    print('Dealer busts!' + '\n')
                    sleep(5)
                    print('\n' * 100)
                    break
                elif player_hand.value < comp_hand.value:
                    player_chips.lose_bet()
                    print('Dealer wins!\n')
                    sleep(5)
                    print('\n' * 100)
                    break
                elif player_hand.value > comp_hand.value:
                    show_all(player_hand, comp_hand)
                    player_chips.win_bet()
                    print('Player wins!\n')
                    sleep(5)
                    print('\n' * 100)
                    break
                elif player_hand.value == comp_hand.value:
                    show_all(player_hand, comp_hand)
                    print('Push!\n')
                    sleep(5)
                    print('\n' * 100)
                    break

                break
            break

    if replay():
        continue
    else:
        playing = False
        break
    break