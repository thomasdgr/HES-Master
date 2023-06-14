## Exercice 1 : Weight Initialization
### Activations with U[−1,  1] initialization
After few trainings we observed the following activation values over the different layers:

![Picture](/home/quentin/Documents/Master/TSM_DeLearn/TP_06/img/not_proper_results.png ){ width="400" style="display: block; margin: 0 auto" }

On all layers, we see that the most parts of neurons activation values are either 0 or 1. It means that they are saturating according to the sigmoid activation function. The reason is the standard deviation which is too big. We can observe the same problem in the figure 117 of the lesson.

### Activations with improved but non-optimal initialization
After few trainings we observed the following activation values over the different layers:

![Picture](/home/quentin/Documents/Master/TSM_DeLearn/TP_06/img/not_optimal_results.png ){ width="400" style="display: block; margin: 0 auto" }

We see that the closer the layer is to the output of the neural network, the closer the activation values are to 0. Either, the variance decreases throughout the neural net. It decreases by about half at each layer. The reason is that the used variance is 1 and doesn't correspond to the variance of the sigmoid function, which is 1/3.

### Activations with Xavier initialization
After few trainings we observed the following activation values over the different layers:

![Picture](/home/quentin/Documents/Master/TSM_DeLearn/TP_06/img/proper_results.png ){ width="400" style="display: block; margin: 0 auto" }

Wee see that the variance is almost constant over the layers.

## Exercice 2 : Batch Normalization
After few trainings we observed the following activation values over the different layers:
![Picture](/home/quentin/Documents/Master/TSM_DeLearn/TP_06/img/ex2_batch.png ){ width="600" style="display: block; margin: 0 auto" }

On all layers we see a similar saturation as when we used U[−1,  1] initialization. Normalization should not product this effect. This is probably due to a miscalculation in the back propagation. Indeed, a test does not pass.
