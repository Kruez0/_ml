import torch
import matplotlib.pyplot as plt

x = torch.tensor([0, 1, 2, 3, 4], dtype=torch.float32)
y = torch.tensor([1.9, 3.1, 3.9, 5.0, 6.2], dtype=torch.float32)

p = [torch.tensor(0.0, requires_grad=True), torch.tensor(0.0, requires_grad=True)]

def predict(p, x_val):
    return p[0] + p[1] * x_val

def MSE(p, x, y):
    y_pred = predict(p, x)
    return torch.mean((y - y_pred) ** 2)

def gradient_descent(f, p, lr=0.01, max_loops=100000, dump_period=1000):
    for loop in range(max_loops):
        loss = f(p, x, y)
        loss.backward()
        
        grads = [param.grad.item() for param in p]
        glen = torch.sqrt(sum(param.grad**2 for param in p)).item()
        
        if loop % dump_period == 0:
            print(f'loop {loop}, p = {[param.item() for param in p]}, f(p) = {loss.item():.4f}, glen = {glen:.6f}')
        
        if glen < 0.00001:
            break
        
        with torch.no_grad():
            for param in p:
                param -= lr * param.grad
                param.grad.zero_()

    print(f'loop {loop}, p = {[param.item() for param in p]}, f(p) = {loss.item():.4f}, glen = {glen:.6f}')
    return p

# Run gradient descent
optimal_p = gradient_descent(MSE, p, max_loops=3000, dump_period=100)

# Plot result
with torch.no_grad():
    y_predicted = optimal_p[0] + optimal_p[1] * x
    print('y_predicted =', y_predicted.tolist())

    plt.plot(x.numpy(), y.numpy(), 'ro', label='Original data')
    plt.plot(x.numpy(), y_predicted.numpy(), label='Fitted line')
    plt.legend()
    plt.show()
