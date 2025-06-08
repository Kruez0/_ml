from Micrograd.Engine import Value

x = Value(0.0)
y = Value(0.0)
z = Value(0.0)

learn = 0.1
epoch = 100

for epoch in range(epoch):
    loss = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8

    loss.backward()

    x.data -= learn * x.grad
    y.data -= learn * y.grad
    z.data -= learn * z.grad

    x.grad = 0
    y.grad = 0
    z.grad = 0

    if epoch % 10 == 0:
        print('Epoch', epoch,': Loss =', round(loss.data, 4),', x =', round(x.data, 4),', y =', round(y.data, 4),', z =', round(z.data, 4))

print('Best result: x =', round(x.data, 4), ', y =', round(y.data, 4), ', z =', round(z.data, 4))
