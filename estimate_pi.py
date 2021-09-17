import random

def estimate_pi(n):
    point_in_circle = 0
    point_in_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            point_in_circle += 1
        point_in_total += 1
    return 4 * point_in_circle/ point_in_total

print(estimate_pi(10000))   
