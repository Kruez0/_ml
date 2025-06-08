from Micrograd.Engine import Value

x = Value(1)
y = x.sigmoid()
y.backward()
print(f"Sigmoid Output: ", y)
print(f"Sigmoid Gradient (dy/dx): ", x.grad)

a = Value(1)
b = a.exp()
b.backward()
print(f"Exp Output: ", a)
print(f"Exp Gradient (dy/dx): ", b)
