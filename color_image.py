import cv2
import numpy as np


img = cv2.imread("image.jpg")

height, width, depth = img.shape
circle_img = np.zeros((height, width), np.uint8)

mask = cv2.circle(circle_img, (int(width / 2), int(height / 2)), 1, 1, thickness=-1)
masked_img = cv2.bitwise_and(img, img, mask=circle_img)

circle_locations = mask == 1
bgr = img[circle_locations]

rgb = bgr[..., ::-1]

print(rgb)