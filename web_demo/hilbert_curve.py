import numpy as np
import random
import matplotlib.pyplot as plt
import math

def gen_1d_points(num_pts: int, lower_bound: int, upper_bound: int) -> list:
    arr = []

    for i in range(num_pts):
        arr.append(random.randint(lower_bound, upper_bound))

    return arr

def helper(hilb_idx: int, curr_order: int, hcurve_order: int, x: int, y: int) -> tuple:
    n1_hash = {0: (0, 0), 1: (0, 1), 2: (1, 1), 3: (1, 0)}

    # print(curr_order, x, y)

    if curr_order > hcurve_order:
        return int(x), int(y)

    l2_bits = hilb_idx & 3
    mult_constant = curr_order / 2

    match l2_bits:
        case 0:
            temp = y
            y = x
            x = temp
            return helper(hilb_idx>>2, curr_order*2, hcurve_order, x, y)
        case 1:
            y += mult_constant
            return helper(hilb_idx>>2, curr_order*2, hcurve_order, x, y)
        case 2:
            x += mult_constant
            y += mult_constant
            return helper(hilb_idx>>2, curr_order*2, hcurve_order, x, y)
        case 3:
            temp = y
            y = (mult_constant - 1) - x
            x = (mult_constant - 1) - temp
            x += mult_constant
            return helper(hilb_idx>>2, curr_order*2, hcurve_order, x, y)

def hilbex_to_cartesian(hilb_idx: int, hcurve_order: int) -> tuple:
    n1_hash = {0: (0, 0), 1: (0, 1), 2: (1, 1), 3: (1, 0)}

    idx = hilb_idx

    fnum = idx & 3
    coord = n1_hash[fnum]
    x = coord[0]
    y = coord[1]

    return helper(hilb_idx >> 2, 4, hcurve_order, x, y)

def hilbertize_arr(pts: list) -> np.ndarray:
    hcurve_order = int(math.sqrt(len(pts)))
    new_arr = [[0 for i in range(hcurve_order)] for j in range(hcurve_order)]# 
    # new_arr = np.ones((hcurve_order, hcurve_order))

    for idx, pt in enumerate(pts):
        x, y = hilbex_to_cartesian(idx, hcurve_order)
        new_arr[y][x] = pt

    return new_arr

if __name__ == '__main__':
    # pts =  gen_1d_points(16, 0, 255) # gen_1d_points(256*256, 0, 255)
    pts = [i for i in range(256)]
    print(pts)

    empty_img = hilbertize_arr(pts)

    plt.imshow(empty_img)
    plt.show()