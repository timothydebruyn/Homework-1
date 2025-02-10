#region imports
from Dice import rollDice
from Die import rollUnFairDie
#endregion

#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities

    nDice = int(input("Enter the number of dice to roll: "))  # number of dice
    nMinScore = nDice  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1  # number of possible scores
    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        total_score = rollDice(N=nDice)  # call with N=nDice
        nTally[total_score - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start
    print(f"After rolling {nDice:.2f} dice {nRolls:.2f} times:")
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = nMinScore + i
        probability = nTally[i] / nRolls
        print(f"Probability of rolling a {score}: {probability:.3f}")

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities

    nDice = 5 # number of dice
    nMinScore = nDice # total score if each die scores 1
    nMaxScore = nDice * 6 # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1 # number of possible scores
    nTally = [0] * nNumScores # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000 # how many times to roll the dice
    for _ in range(nRolls):  # each loop rolls dice and increments a score
        total_score = sum(rollUnFairDie() for _ in range(nDice))# call with N=nDice
        nTally[total_score - nMinScore] += 1 # increment score-nMinScore item b/c 0 indexing start
    print("After rolling {nDice} unfair dice {nRolls} times:")
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = nMinScore + i
        probability = nTally[i] / nRolls
        print(f"Probability of rolling a {score}: {probability:.3f}")
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()