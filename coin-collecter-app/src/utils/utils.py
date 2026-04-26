import random

def set_position(rect, x, y, y_range):
    """Set the position of a sprite rectangle, using random values if not specified.

    Args:
        rect: The pygame Rect object to position.
        x: Desired x coordinate, or None for random horizontal position.
        y: Desired y coordinate, or None for random position within y_range.
        y_range: Tuple specifying the minimum and maximum y values when y is None.
    """
    if x is None:
        rect.x = random.randint(0, 1250 - rect.width)
    else:
        rect.x = x

    if y is None:
        rect.y = random.randint(y_range[0], y_range[1])
    else:
        rect.y = y
