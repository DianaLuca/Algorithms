def power(x, n, count_steps):
    count_steps += 1
    if n == 0:
        return 1, count_steps
    y, count_steps = power(x, n//2, count_steps)

    if n % 2 == 0:
        return y*y, count_steps
    else:
        return x*y*y, count_steps

# test: complexity O(logN)

res, steps = power(2, 5, 0)
print(res, steps)

