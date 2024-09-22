# Allá Tú Problem Simulation

## Introduction
The **Allá Tú** problem is based on the Spanish TV game show **Allá Tú** (similar to **Deal or No Deal** in other countries), where contestants select one of 22 boxes in the hope of winning the highest prize (600,000€). As boxes are progressively opened, contestants are given the opportunity to **switch boxes** at certain intervals. The goal of this simulation is to explore the win rate the 600,000€ prize using two strategies:
1. **Switching boxes** at predefined stages.
2. **Sticking** with the original choice.

In the real show, the host may also offer the contestant a sum of money to stop playing and accept a guaranteed amount. However, **this simulation does not consider the scenario where contestants take such deals**. We assume that the contestant is focused on maximizing their chances of winning the 600,000€ prize, which is the only scenario **mathematically relevant** or of interest for this analysis. Therefore, the simulation centers around the decision to switch boxes or stay with the original box at various stages, comparing both strategies.

The box order in the simulation defines the points in the game where a box is opened, based on the **number of remaining boxes**.

## Simulation Overview
In this simulation, the contestant can either:
- **Switch** to a different unopened box whenever prompted.
- **Stick** with their original box and never switch.

## Formalized Probabilities

1. **Win rate by not switching**:

   The probability remains constant throughout the game since the contestant sticks with the initially chosen box.

   $$\[
   P(\text{Win if no switch}) = \frac{1}{n}
   \]$$

   Where \(n = 22\) is the total number of boxes.

2. **Win rate by switching**:
   The win rate by switching increases as more boxes are eliminated. The general formula is:

   $$\[
   P(\text{Win if switch}) = \frac{n-1}{n} \times \frac{1}{k-1}
   \]$$

   Where:
   - n is the number of boxes.
   - k is the number of unopened boxes.
---
 Here are the probabilities for each case.

### Case 1: Sticking

1. **Sticking**:
   $$\[
   P(\text{Win if no switch}) = \frac{1}{22} \times \approx 0.0455\)
   \]$$

---

### Case 2: Box Order = [16, 10, 4]

1. **When 16 boxes remain** (\(k=6\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{22 - 6 - 1} = \frac{21}{22} \times \frac{1}{15} \approx 0.0636
   \]$$

2. **When 10 boxes remain** (\(k=12\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{22 - 12 - 1} = \frac{21}{22} \times \frac{1}{9} \approx 0.106
   \]$$

3. **When 4 boxes remain** (\(k=18\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{22 - 18 - 1} = \frac{21}{22} \times \frac{1}{3} \approx 0.3182
   \]$$

---

### Case 3: Box Order = [16, 11, 7, 4, 2]

1. **When 16 boxes remain** (\(k=6\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{15} \approx 0.0636
   \]$$

2. **When 11 boxes remain** (\(k=11\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{10} \approx 0.0955
   \]$$

3. **When 7 boxes remain** (\(k=15\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{6} \approx 0.1591
   \]$$

4. **When 4 boxes remain** (\(k=18\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{3} \approx 0.3182
   \]$$

5. **When 2 boxes remain** (\(k=20\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{1} \approx 0.9545
   \]$$

---

### Case 4: Box Order = [19, 16, 13, 10, 7, 4]

1. **When 19 boxes remain** (\(k=3\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{18} \approx 0.0534
   \]$$

2. **When 16 boxes remain** (\(k=6\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{15} \approx 0.0636
   \]$$

3. **When 13 boxes remain** (\(k=9\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{12} \approx 0.0795
   \]$$

4. **When 10 boxes remain** (\(k=12\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{9} \approx 0.106
   \]$$

5. **When 7 boxes remain** (\(k=15\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{6} \approx 0.1591
   \]$$

6. **When 4 boxes remain** (\(k=18\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{3} \approx 0.3182
   \]$$

---

### Case 5: Box Order = [19, 16, 13, 10, 7, 4, 2]

1. **When 19 boxes remain** (\(k=3\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{18} \approx 0.0534
   \]$$

2. **When 16 boxes remain** (\(k=6\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{15} \approx 0.0636
   \]$$

3. **When 13 boxes remain** (\(k=9\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{12} \approx 0.0795
   \]$$

4. **When 10 boxes remain** (\(k=12\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{9} \approx 0.106
   \]$$

5. **When 7 boxes remain** (\(k=15\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{6} \approx 0.1591
   \]$$

6. **When 4 boxes remain** (\(k=18\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{3} \approx 0.3182
   \]$$

7. **When 2 boxes remain** (\(k=20\) boxes opened):
   $$\[
   P(\text{Win if switch}) = \frac{21}{22} \times \frac{1}{1} \approx 0.9545
   \]$$

---

## Simulation Results
Each scenario is simulated with **1,000,000 iterations**, and the results shows the number of wins, losses, and the respective win rates and losing for both strategies:

#### Case 1: Sticking
- **Wins** 45,452 times
- **Losses** 954,548 times
- **Win rate** 4.54%
- **Loss rate** 95.46%
#### Case 2: Box Order = [16, 10, 4]: Switching Boxes
- **Wins** 60,558 times
- **Losses** 93.9442 times
- **Win rate** 6.06%
- **Loss rate** 93.94%
#### Case 3: Box Order = [16, 11, 7, 4, 2]: Switching Boxes
- **Wins** 81,809 times
- **Losses** 918,191 times
- **Win rate** 8.18%
- **Loss rate** 91.82%
#### Case 4: Box Order = [19, 16, 13, 10, 7, 4]: Switching Boxes
- **Wins** 70,297 times
- **Losses** 929,703 times
- **Win rate** 7.02%
- **Loss rate** 92.98%
#### Case 5: Box Order = [19, 16, 13, 10, 7, 4, 2]: Switching Boxes
- **Wins** 79,354 times
- **Losses** 920,646 times
- **Win rate** 7,93%
- **Loss rate** 92,06%


## Conclusion
In all scenarios, switching boxes significantly increases the win rate as more boxes are opened and eliminated, while the win rate by not switching remains constant at $$\(\frac{1}{22} \approx 0.0455\)$$ throughout the game.

## Requirements
- Python 3.x
