TANK_CAPACITY = 255

n = int(input())
current_tank_capacity = 0

for _ in range(n):
    current_liters = int(input())

    if current_tank_capacity + current_liters > TANK_CAPACITY:
        print("Insufficient capacity!")
    else:
        current_tank_capacity += current_liters

print(current_tank_capacity)


