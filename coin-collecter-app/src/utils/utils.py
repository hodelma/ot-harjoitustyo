import random

def set_position(rect, x, y, y_range):
    if x is None:
        rect.x = random.randint(0, 1250 - rect.width)
    else:
        rect.x = x

    if y is None:
        rect.y = random.randint(y_range[0], y_range[1])
    else:
        rect.y = y
