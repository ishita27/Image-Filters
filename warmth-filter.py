import cv2 as cv
import numpy as np
from scipy.interpolate import UnivariateSpline

class warmth_filter:
    """warmth-filter--
        This filter will improve all tones and absorb
        the blues by adding a slight yellow tint.
        Ideally to be used on portraits.
    """

    def __init__(self):
        # create look-up tables for increasing and decreasing red and blue resp.
        self.increaseChannel = self.LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 70, 140, 210, 256])
        self.decreaseChannel = self.LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 30,  80, 120, 192])

    def render(self, img_rgb):
        img_rgb = cv.imread(img_rgb)
        cv.imshow("Original", img_rgb)
        r,g,b = cv.split(img_rgb)
        b = cv.LUT(b, self.increaseChannel).astype(np.uint8)
        r = cv.LUT(r, self.decreaseChannel).astype(np.uint8)
        img_rgb = cv.merge((r,g,b))

        # saturation increased
        h,s,v = cv.split(cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV))
        s = cv.LUT(s, self.increaseChannel).astype(np.uint8)


        return cv.cvtColor(cv.merge((h,s,v)), cv.COLOR_HSV2RGB)

    def LUT_8UC1(self, x, y):
        #Create look-up table using scipy spline interpolation function
        spl = UnivariateSpline(x, y)
        return spl(range(256))

class_object = warmth_filter()
file_name = "beach.jpg" #File_name will come here
res = class_object.render(file_name)
cv.imwrite("warm_image.jpg", res)
cv.imshow("Warm-Filter version", res)
cv.waitKey(0)
cv.destroyAllWindows()
