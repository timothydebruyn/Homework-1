# region imports
from Die import rollFairDie, rollUnFairDie # Importing the Die class
# endregion

# region functions
def rollDice(N=1):
    """
    Simulates rolling N fair dice and returns the total score.
    :param N: The number of dice to roll
    :return: The total score from rolling N dice
    """
    total = 0
    for _ in range(N):
        total += rollFairDie()  # Assuming Die has a roll() method for fair dice
    return total

def rollUnFairDice(N=1):
    """
    Simulates rolling N unfair dice and returns the total score.
    :param N: The number of dice to roll
    :return: The total score from rolling N dice
    """
    total = 0
    for _ in range(N):
        total += rollUnFairDie()  # Assuming Die has a roll_unfair() method for unfair dice
    return total
# endregion
