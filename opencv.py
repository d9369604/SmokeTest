import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


def compare(image, template):
    res_img = template.replace('golden', 'result')
    if os.path.exists(res_img): os.remove(res_img)
    img = cv2.imread(image)
    template = cv2.imread(template)
    # print(template.shape)
    w, h = template.shape[:2][::-1]

    meth = 'cv2.TM_CCOEFF_NORMED'
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(max_val)
    # if max_val > 0.9:
    #     print('Match')
    # else:
    #     print('No')
    # return True if max_val > 0.9 else False

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

    # plt.subplot(122),\
    plt.imshow(img)
    plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.savefig(res_img, dpi=300)
    # plt.suptitle(meth)
    #
    # plt.show()
    # print(max_val)
    return True if max_val > 0.99 else False

if __name__ == '__main__':
    import os
    os.chdir(r'C:\Users\Gary\Desktop')
    compare('larger.png', 'template3.png')
