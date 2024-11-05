import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

num_rolls = int(input("Enter the number of rolls: "))
num_sides = int(input("Enter the number of sides on the die: "))

rolls = np.random.randint(1, num_sides + 1, num_rolls)
outcomes = Counter(rolls)
pmf = {outcome: count / num_rolls for outcome, count in outcomes.items()}

print("Outcome : Probability")
for outcome, probability in sorted(pmf.items()):
    print(f"{outcome} : {probability:.2f}")

plt.bar(pmf.keys(), pmf.values(), color='skyblue')
plt.xlabel("Dice Outcome")
plt.ylabel("Probability")
plt.title(f"PMF for {num_rolls} Rolls of a {num_sides}-Sided Die")
plt.xticks(range(1, num_sides + 1))
plt.show()