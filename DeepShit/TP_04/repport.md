# Practical Work 04 - 14.03.2023 - Universal Representation Theorem Model Selection

Realized by: Thomas Dagier and Quentin Rod

## Exercise 1 - Function Approximation

### A - Compute the formulas for gradient descent for this problem

![ex1-1.jpg](repport_files/ex1-1.jpg)

![ex1-2.jpg](repport_files/ex1-2.jpg)

### B - Implement MBGB for this model in the notebook

See **function_approximation_stud.ipynb**. While we were implementing the equations we found in the previous exercise, we noticed that the equations were not 100% correct. We made few changes inside the notebook with a note.

### C - Study the impact of different setting by looking at the learning curves

![.](repport_files/alpha01.png)

Alpha = 0.1

![.](repport_files/alpha02.png)

Alpha = 0.2

![.](repport_files/batch5.png)

Batch = 5

![.](repport_files/batch50.png)

Batch = 50

![.](repport_files/epoch10.png)

Epochs = 10

![.](repport_files/epoch1000.png)

Epochs = 1000

![.](repport_files/neuron5.png)

Neurons = 5

![.](repport_files/neuron50.png)

Neurons = 50

A good balance would be alpha=0.2, batch size = 20, neurons = 50 and epochs = 1'000

## Exercice 2

### A - Complete the code

See **overfitting_stud.ipynb**.

### B - Construct different models of differenet coplexities (parameter order)

Version 1 (score_train_1.csv):

| order | error rate (train) | error rate (test) |
|-------|--------------------|-------------------|
|   1   |        0.05        |        0.14       |
|   2   |        0.06        |        0.16       |
|   3   |        0.04        |        0.12       |
|   4   |        0.05        |        0.11       |
|   5   |        0.04        |        0.11       |
|   6   |        0.04        |        0.10       |
|   7   |        0.04        |        0.11       |

Version 2 (score_train_2.csv):

| order | error rate (train) | error rate (test) |
|-------|--------------------|-------------------|
|   1   |        0.10        |        0.11       |
|   2   |        0.03        |        0.05       |
|   3   |        0.01        |        0.06       |
|   4   |        0.02        |        0.08       |
|   5   |        0.00        |        0.05       |
|   6   |        0.00        |        0.04       |
|   7   |        0.00        |        0.04       |

### C - Determine the model best suited for the problem at hand

Version 1 (score_train_1.csv):

![.](repport_files/version1.png)

Version 2 (score_train_2.csv):

![.](repport_files/version2.png)

The best model would be the model where the test error is minimized for both version. In our case, it seems like the order 7 with 4'000 epochs is the best model.
