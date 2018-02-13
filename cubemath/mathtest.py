import numpy as np
import transforms

def rot_test():
    angles = [0, 90, 180, 270, 360]
    axes = [0, 1, 2]
    tpoint = np.transpose(np.array([1,1,1]))
    print("Testing: Rotation Matricies")
    for axis in axes:
        for angle in angles:
            r = transforms.rotmat(angle, axis)
            rpoint = np.matmul(r,tpoint)

            tpoint_base = tpoint/np.linalg.norm(tpoint)
            rpoint_base = rpoint/np.linalg.norm(rpoint)

            dp = np.dot(tpoint_base, rpoint_base)
            dp = round(dp, 3)
            if dp == 1 and angle == 0 or angle == 360:
                print("Test Passed")
            elif dp == -1 and angle == 180:
                print("Test Passed")
            elif dp == 0 and angle == 90 or angle == 180:
                print("Test Passed")
            else:
                print("Test Failed:")
                print("\tangle =", angle)
                print("\taxis =", axis)
                print("\tresult =", rpoint)
                print("\tDot Product =", dp)



def rev_test():
    pass

rot_test()
#print(transforms.rotmat(90,0))
