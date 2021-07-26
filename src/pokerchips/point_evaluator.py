def evaluate_points(chips):
    points = 0
    for chip in chips:
        points = points + get_chip_points(chip)
    return points

def get_chip_points(chip):
    return chip.value