import random

def f(x, y, z):
    return x*x + y*y + z*z - 2*x - 4*y - 6*z + 8

x, y, z = 1, 1, 1
go = 0.0001
fails = 0
max_fails = 100000

for fail in range(max_fails):
    dx = random.uniform(-go, go)
    dy = random.uniform(-go, go)
    dz = random.uniform(-go, go)

    newx = x + dx
    newy = y + dy
    newz = z + dz

    if f(newx, newy, newz) < f(x, y, z):
        x, y, z = newx, newy, newz
        fails = 0
    else:
        fails += 1
        if fails >= max_fails:
            break

print("x:", x, "y:", y, "z:", z)
