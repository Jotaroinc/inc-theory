def inc_loop(n, steps=10):
    cycle = []
    for _ in range(steps):
        if n % 3 == 0:
            n = n / 3
            cycle.append(("Rest", n))
        elif n % 3 == 1:
            n = 2 * n + 1
            cycle.append(("Expand", n))
        else:
            n = n - 1
            cycle.append(("Contract", n))
    return cycle

print(inc_loop(7))
