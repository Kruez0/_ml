# Optimization of Quadratic Functions

The goal is to find values of `x`, `y`, and `z` that minimize `f`.

## How It Works
- Starts with initial values `x = 1`, `y = 1`, and `z = 1`.
- At each iteration, randomly changes the value of `x`, `y`, and `z` by a small amount (`±0.0001`).
- If the new position have a lower function value, it accepts the new values.
- Otherwise, it counts will not accept and is therefore failed.
- Stops after 100,000 failed attempts (no improvement).

## Output
```
x: 1.0000011102044783 y: 1.9999956457560786 z: 2.9999990631416353
```
