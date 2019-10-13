"""
File containing game functions.
"""

def take_bet(player_balance):
    bet = 0

    while bet == 0:
        try:
            bet_size = int(input('Enter a stake: '))
        except:
            print('That is not a valid number!\n')
        else:
            if bet_size <= int(player_balance.total):
                bet += bet_size
            else:
                print('Insufficient funds.\n')
                continue
    return bet


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

    if hand.value <= 21:
        return hand.value
    else:
        return 'Bust!'


def hit_or_stand(deck, hand):
    global playing

    while True:
        choice = input('Do you wish to Hit, "H", or Stand, "S"? ... ').upper()

        if choice == 'H' or choice == 'HIT':
            hit(deck, hand)
            return choice
        elif choice == 'S' or choice == 'STAND':
            return choice
        else:
            print('That choice is not valid!\n')
            continue


def show_some(player, dealer):
    print(f"Player's cards are {player.cards}.\n")
    print(f"Dealer's second card is {dealer.cards[1]}.\n")


def show_all(player, dealer):
    print(f"Player's cards are {player.cards}.\n")
    print(f"Dealer's cards are {dealer.cards}.\n")


def replay():
    again = (input('Would you like to go again? Enter "Y" or "N"... ')).lower()

    return again == 'y'