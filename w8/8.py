import torch

x = torch.tensor(0.0, requires_grad=True)
y = torch.tensor(0.0, requires_grad=True)
z = torch.tensor(0.0, requires_grad=True)

learn = 0.1
epoch = 100

for epoch in range(epoch):
    loss = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8

    loss.backward()
    with torch.no_grad():
        x -= learn * x.grad
        y -= learn * y.grad
        z -= learn * z.grad
        x.grad.zero_()
        y.grad.zero_()
        z.grad.zero_()

    if epoch % 10 == 0:
        print('Epoch', epoch, ': Loss =', round(loss.item(), 4),', x =', round(x.item(), 4),', y =', round(y.item(), 4),', z =', round(z.item(), 4))

print('Best result: x =', round(x.item(), 4),', y =', round(y.item(), 4),', z =', round(z.item(), 4))
