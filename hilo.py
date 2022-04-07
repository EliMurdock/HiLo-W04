import random




score = 300
play_again = 'y'
first_card = 0

#creates card generator
class Card_Generator:
    def generate(current_card):
        while True:
            card = random.randint(1, 13)
            if card != current_card:
                break
        return card

class Score:
    def comparison(first_card, second_card, player_guess, score):
        #correct guess
        if ((first_card > second_card and player_guess == 'l') or
            (first_card < second_card and player_guess == 'h')):
            score += 100
        #incorrect guess
        else:
            score += -75
        return score



#runs card generator
first_card = Card_Generator.generate(first_card)
second_card = Card_Generator.generate(first_card)

# prints stuff
print()
print(f'The card is {first_card}')
player_guess = input('Higher or lower? (h/l) ')
print(f'Next card was: {second_card}')

score = Score.comparison(first_card, second_card, player_guess, score)
print(f'Your Score is: {score}')
play_again = input('Play again? (y/n) ').lower()

#runs game as many times as the player wants
while play_again == 'y':
    #runs card generator
    first_card = Card_Generator.generate(first_card)
    second_card = Card_Generator.generate(first_card)

    # prints cards, asks for guess
    print()
    print(f'The card is {first_card}')
    player_guess = input('Higher or lower? (h/l) ')
    print(f'Next card was: {second_card}')

    # adjusts score
    score = Score.comparison(first_card, second_card, player_guess, score)
    print(f'Your Score is: {score}')

    #breaks if score is less than 0
    if score <= 0:
        break

    #play again?
    play_again = input('Play again? (y/n) ').lower()
    print(play_again)

print()
print('Thanks for playing')