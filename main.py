import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
import numpy as np

GREEN = colors.to_rgba('green')
BLUE = colors.to_rgba('blue')

FRAMES = 100
STEPS_PER_FRAME = 10

TOTAL_POINTS = FRAMES * STEPS_PER_FRAME
SQUARESIZE = 10
CIRCLERAD = SQUARESIZE/2

def truncate_float_decimals(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

fig, ax = plt.subplots()

rect = patches.Rectangle(
    xy=(0, 0), width=SQUARESIZE, height=SQUARESIZE,
    facecolor='skyblue', edgecolor='navy', linewidth=2, alpha=0.3
)

circle = patches.Circle(
    xy=(CIRCLERAD, CIRCLERAD), radius=CIRCLERAD,
    facecolor='turquoise', edgecolor='navy', linewidth=2, alpha=0.3
)

ax.add_patch(rect)
ax.add_patch(circle)

scatter = ax.scatter([], [], s=15)

ax.set_xlim(0, SQUARESIZE)
ax.set_ylim(0, SQUARESIZE)
ax.set_aspect('equal')
fig.subplots_adjust(bottom=0.15)

points = np.zeros((TOTAL_POINTS, 2))
point_colors = np.zeros((TOTAL_POINTS, 4))

counter_text = fig.text(0.5, 0.02, "", ha='center')

in_counter = 0

def update(frame):
    x, y = np.random.uniform(0, 10), np.random.uniform(0, 10)

    global in_counter
    for i in range(STEPS_PER_FRAME):
        idx = frame * STEPS_PER_FRAME + i
        x, y = np.random.uniform(0, SQUARESIZE), np.random.uniform(0, SQUARESIZE)
        is_in_circle = np.hypot(x - CIRCLERAD, y - CIRCLERAD) <= CIRCLERAD
        if is_in_circle:
            in_counter += 1
            new_color = GREEN
        else:
            new_color = BLUE
        points[idx] = (x, y)
        point_colors[idx] = new_color
    scatter.set_offsets(points[:frame * STEPS_PER_FRAME + STEPS_PER_FRAME])
    scatter.set_facecolors(point_colors[:frame * STEPS_PER_FRAME + STEPS_PER_FRAME])

    total = (frame + 1) * STEPS_PER_FRAME


    Pi_approx = 4 * in_counter / total
    counter_text.set_text(f"π approx: {truncate_float_decimals(Pi_approx,5)}")

    return scatter, counter_text

anim = FuncAnimation(fig, update, frames=FRAMES, interval=5, blit=False, repeat = False)
'''#gif recording:
anim.save("pi-montecarlo.gif", writer = 'pillow', fps = 100)
in_counter = 0
points[:] = 0
point_colors[:] = 0
scatter.set_offsets(np.empty((0, 2)))
scatter.set_facecolors([])
'''
plt.show()
