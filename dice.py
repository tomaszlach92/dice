import random

DICE_TYPES = {'D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100'}


def dice_game():
    """Function for dice game"""
    user_dice = input("Wprowadź formułę kostki: ")
    for dice in DICE_TYPES:
        if dice in user_dice:
            try:
                multiply, modifier = user_dice.split(dice)
            except ValueError:
                return "Wprowadzono niepoprawne dane"
            dice_value = int(dice[1:])
            break
    else:
        return "Wprowadzono niepoprawne dane"
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wprowadzono niepoprawne dane"
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wprowadzono niepoprawne dane"
    return sum([random.randint(1, dice_value) for i in range(multiply)]) + modifier


if __name__ == '__main__':
    print(dice_game())
