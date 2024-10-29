# Greedy algorithms

A greedy algorithm is an approach to solving problems by maing a sequence of choices, each of which seems best at the moment, with the hope that these local choices lead to an overalll optimal solution

In other words, it builds a solution piece by piece, always choosing the option that provides the most immediate benefit or smallest cost without revisiting previous choices. Greedy algorithms are fast and straightforward but don't always guarantee the best solution for every problem. They work best for problems where a local optimum also leads to a global optimum, like finding the shortest path or minimizing total waiting time

## Largest number

Greedy Strategy

- Make some greedy choice
- Prove that it is a safe choice
- Reduce to a subproblem
- Solve the subproblem

## Reduction to Subproblem

- Make some first choice
- Then solve a problem of the same kind
- Smaller: fewer digits, fewer patients
- This is called a "subproblem"

Safe choice

- A choice is called safe if there is an optimal solution consistent with this first choice
- Not all first choices are safe
- Greedy choices are often unsafe

## Celebration Party

## Maximum Value of the Loot

The **Maximum Value of the Loot**, where a burglar wants to maximize the value of loot (spices) that he can carry in a knapsack with a limited weight capacity. He can take parts of items, not just whole ones, making this a “fractional” problem.

### Problem Overview

1. **Items** have different **values** and **weights**.
2. **Goal:** Maximize the total value of items in the knapsack without exceeding its weight capacity.
3. **Approach:** The burglar can choose any fraction of an item, meaning he can take just part of an item to use the knapsack’s weight most efficiently.

### Greedy Strategy

1. **Value per Weight:** Calculate the value per unit weight for each item (e.g., \$6/kg for item 1).
2. **Take Highest Value per Weight First:** Prioritize items with the highest value per weight, adding as much of these items as possible until the knapsack is full.
3. **Fill Remaining Space:** If an item doesn’t completely fit, take only as much as the remaining capacity allows.

### Why This Works (Proof)

The greedy approach works because each choice (adding the highest value-per-weight item first) leads to an optimal solution. By always choosing the highest value-per-weight item, the burglar maximizes the total value without sacrificing knapsack space.

### Steps of the Algorithm

1. Sort items by value per weight.
2. Start with the item with the highest value per weight, adding it fully if it fits, or partially if only part fits.
3. Repeat with the next highest value-per-weight item until the knapsack reaches full capacity.

This approach guarantees that the solution is both **efficient** and **optimal** for maximizing the value in the knapsack.

The **implementation and optimization** of the greedy algorithm for the **Maximum Value of the Loot**.

### Implementation Steps

1. **Recall the Algorithm**: While there’s still capacity in the knapsack, repeatedly select the item with the highest value per unit weight:
   - If it fits, take it entirely.
   - If not, take only as much as needed to fill the knapsack.
2. **Best Item Function**: A helper function, `BestItem`, is used to identify the item with the highest value per weight that hasn’t yet been fully taken. This function iterates through all items and returns the best option.
3. **Knapsack Function**:
   - Starts with an empty knapsack and zero total value.
   - Repeatedly calls `BestItem` to choose items until the knapsack is full.
   - Updates the remaining capacity and total value after each addition.
   - The algorithm stops when either all items are taken or the knapsack reaches capacity.

### Optimizing the Algorithm

1. **Sort by Value per Weight**: Instead of calling `BestItem` each time, sort items by value per weight at the beginning.
2. **KnapsackFast Function**: After sorting, simply select items in descending order of value per weight, skipping the repeated calls to `BestItem`.
3. **Improved Time Complexity**:
   - Original algorithm complexity: \(O(n^2)\) due to multiple calls to `BestItem`.
   - Optimized version: \(O(n \log n)\) after sorting, as each iteration is now constant time, reducing the overall runtime significantly.

The optimized algorithm efficiently solves the fractional knapsack problem by maximizing value while reducing computational time.

A **summary of greedy algorithm concepts** and the general strategy for applying them to various problems.

### Key Concepts of Greedy Algorithms

1. **Greedy Choice**: The approach selects the best choice available at each step.
2. **Safe Choice**: A choice is "safe" if it can be proven to lead to an optimal solution. Proving this involves showing that an optimal solution exists that begins with this choice.
3. **Subproblem**: After making a safe choice, the problem reduces to a smaller, similar subproblem. This subproblem is then solved with the same greedy approach until the problem is fully resolved.

### Examples of Safe Choices in Problems

- **Maximizing Salary**: Start with the maximum digit.
- **Minimizing Patient Wait Time**: Start with the patient with the minimum treatment time.
- **Grouping Children by Age**: Start with the leftmost child and group based on age range.
- **Fractional Knapsack**: Take as much as possible of the item with the highest value per unit weight.

### Strategy for Using Greedy Algorithms

1. **Formulate the Greedy Choice**: Identify what seems like the best immediate option.
2. **Prove It’s a Safe Choice**: Demonstrate that starting with this choice can lead to an optimal solution.
3. **Reduce to Subproblem**: After making the safe choice, repeat the process on the smaller problem until it's fully solved.

### Importance of Proving Safety

Greedy algorithms don’t work for all problems. Without proving the choice is safe, you risk implementing an incorrect solution. Failing to prove safety may lead to wasted time debugging, as not all greedy choices lead to optimal solutions.

This structured approach, from safe choice to subproblem, ensures the greedy algorithm is both **efficient and correct**.
