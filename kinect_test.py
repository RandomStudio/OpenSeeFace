import cv2
import numpy as np

import pyk4a
from pyk4a import Config, PyK4A


def main():
    k4a = PyK4A(
        Config(
            color_resolution=pyk4a.ColorResolution.OFF,
            depth_mode=pyk4a.DepthMode.PASSIVE_IR,
            synchronized_images_only=False,
        )
    )
    k4a.start()

    dyn_range = 152
    #exposure = 0

    while 1:
        capture = k4a.get_capture()
        
        if np.any(capture.ir):
            buf = capture.ir
            #exp = max(0, int(exposure*dyn_range))
            #buf += exp
            buf = buf.clip(0, int(65535/dyn_range))
            buf *= int(dyn_range)
            cv2.imshow("k4a", buf)
            key = cv2.waitKey(10)
            if key != -1:
                if key == 43:
                    dyn_range+=8
                    print("Dynamic Range :" + str(dyn_range))
                elif key == 45:
                    dyn_range-=8
                    print("Dynamic Range :" + str(dyn_range))
                    '''
                    elif key == 62:
                        exposure +=1
                        print("Exposure :" + str(exposure))
                    elif key == 60:
                        exposure -=1
                        print("Exposure :" + str(exposure))
                    '''
                elif key == 113:
                    print("q")
                    cv2.destroyAllWindows()
                    break
                else:
                    print(key)
    k4a.stop()


if __name__ == "__main__":
    main()
