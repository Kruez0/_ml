# Binary MLP Classifier with PyTorch
>Did it by self, dont understand use chatgpt and ask friends.
Simple Multi-Layer Perceptron (MLP) implemented in PyTorch to classify 7-bit binary input patterns into 4-bit binary output targets.

## Intro
The model is trained to map 7-dimensional binary inputs to corresponding 4-dimensional binary outputs. 

## Model Architecture

- Input layer: 7 neurons
- Hidden layers: 
  - First hidden layer with 32 neurons, ReLU activation
  - Second hidden layer with 16 neurons, ReLU activation
- Output layer: 4 neurons (raw logits)

## Optimizer

- Adam optimizer with learning rate 0.01

## Usage

Run the script to train the model for 1000 epochs. Loss is printed every 100 epochs. After training, the model predicts the output for each input and prints the binary predicted vectors.

## Example output
```
Epoch 600 | Loss: 0.0001
Epoch 700 | Loss: 0.0001
Epoch 800 | Loss: 0.0001
Epoch 900 | Loss: 0.0000
[1, 1, 1, 1, 1, 1, 0] Predicted: 0000
[0, 1, 1, 0, 0, 0, 0] Predicted: 0001
[1, 1, 0, 1, 1, 0, 1] Predicted: 0010
[1, 1, 1, 1, 0, 0, 1] Predicted: 0011
[0, 1, 1, 0, 0, 1, 1] Predicted: 0100
[1, 0, 1, 1, 0, 1, 1] Predicted: 0101
[1, 0, 1, 1, 1, 1, 1] Predicted: 0110
[1, 1, 1, 0, 0, 0, 0] Predicted: 0111
[1, 1, 1, 1, 1, 1, 1] Predicted: 1000
[1, 1, 1, 1, 0, 1, 1] Predicted: 1001
```

