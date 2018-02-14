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

def ref_test():
    print("Reflection Test")
    a = np.transpose(np.array([1,1,1]))

    for axis in range(3):
        r = transforms.refmat(axis)
        result = np.matmul(r,a)
        print("Axis =",axis,"  result =",result.tolist())
    """
    r1 = transforms.refmat(0,1)
    r2 = transforms.refmat(0,3)
    result1 = np.matmul(r1,a)
    result2 = np.matmul(r2,a)

    print("X = 1:", result1)
    print("x = 3:", result2)
    """

#rot_test()
ref_test()
#print(transforms.rotmat(90,0))
