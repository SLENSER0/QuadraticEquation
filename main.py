a, b, c = map(float, input().split())

# calculate the discriminant
d = b ** 2 - 4 * a * c

x1 = (-b - d ** 0.5) / (2 * a)
x2 = (-b + d ** 0.5) / (2 * a)

print(f'x1 = {x1}\nx2 = {x2}')


