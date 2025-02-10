import random  # Import required module


# Define a Die class
class Die:
    @staticmethod
    def roll_fair_die():
        return random.randint(1, 6)  # Simulates a fair 6-sided die roll


# Function to roll a fair die multiple times
def roll_fair_die_simulation(n):
    scores = [0] * 6  # List with 6 elements initialized to 0

    for _ in range(n):
        score = Die.roll_fair_die()
        scores[score - 1] += 1  # Increment the corresponding index

    print(f"\nResults for {n} rolls:")
    print("Face | Count  | Probability")
    print("---------------------------")
    for i in range(6):
        probability = scores[i] / n
        print(f"  {i + 1:^4} | {scores[i]:<6} | {probability:.4f}")


# Function to roll an unfair die multiple times
def roll_unfair_die_simulation(n):
    def roll_unfair_die():
        """Simulate an unfair die (biased towards 6)."""
        weights = [0.1, 0.15, 0.2, 0.15, 0.1, 0.3]  # Probabilities for faces 1-6
        return random.choices([1, 2, 3, 4, 5, 6], weights)[0]

    scores = [0] * 6

    for _ in range(n):
        score = roll_unfair_die()
        scores[score - 1] += 1

    print(f"\nResults for unfair die ({n} rolls):")
    print("Face | Count  | Probability")
    print("---------------------------")
    for i in range(6):
        probability = scores[i] / n
        print(f"  {i + 1:^4} | {scores[i]:<6} | {probability:.4f}")


if __name__ == "__main__":
    roll_fair_die_simulation(1000)  # Simulate 1,000 fair die rolls
    roll_fair_die_simulation(10000)  # Simulate 10,000 fair die rolls
    roll_unfair_die_simulation(10000)  # Simulate 10,000 unfair die rolls
