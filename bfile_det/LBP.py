import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def get_hull(adder_pts: list, pt: tuple) -> np.ndarray:
    hull = []
    pti, ptj = pt
    for (i, j) in adder_pts:
        hull.append((pti + i, ptj + j))
    
    return hull

def get_points(arr: np.ndarray, pts: list) -> np.ndarray:
    arr_pts = []

    for (i, j) in pts:
        arr_pts.append(arr[i][j])
    
    return arr_pts

def extract_lbp(img: np.ndarray):
    adder_pts = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    lbp_mat = np.zeros(img.shape)
    for i in range(1, len(img) - 1):
        for j in range(1, len(img) - 1):
            hull = get_hull(adder_pts, (i, j))
            barr = (get_points(img, hull) > img[i][j])*1

            num = int(''.join(map(str, barr)), base=2)
            lbp_mat[i][j] = num
    
    return lbp_mat

if __name__ == '__main__':
    fp = './hat_woman_LBP.jpg'

    img = cv2.imread(fp, 0)

    start = time.time()
    lbp_img = extract_lbp(img)
    print(f"finished in {time.time() - start}s")

    plt.imshow(lbp_img)
    plt.show()