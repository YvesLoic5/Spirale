import math
import matplotlib.pyplot as plt

with open("heart.dat", "w") as f_out:
    theta = 0.0
    t_max = 2 * math.pi

    while theta <= t_max:
        x_coord = 16 * math.sin(theta)**3
        y_coord = 13 * math.cos(theta) - 5 * math.cos(2*theta) - 2 * math.cos(3*theta) - math.cos(4*theta)

        f_out.write(f"{x_coord:.5f} {y_coord:.5f}\n")

        theta += 0.01

x = []
y = []

with open("heart.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.figure(figsize=(8, 8))
mini = min(x + y) * 1.2
maxi = max(x + y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x, y)
plt.savefig("heart.png")
plt.show()
