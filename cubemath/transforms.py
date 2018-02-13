import numpy as np

def rotmat(angle, axis_num, thresh = 3):
    angle = np.deg2rad(angle)
    d = []
    #assemble the components of the rotation matrix.
    axis = [0, 0, 0]; axis[axis_num] = 1
    for v in axis:
        r_diag = np.cos(angle)+v**2*(1-np.cos(angle))
        #r_diag = np.cos(angle)**2 + (np.sin(angle)*v)**2 - 0.5
        d.append(r_diag)

    l = [0, 0, 0]; u = [0, 0, 0]
    l[0] = (1-np.cos(angle))*axis[0]*axis[1]+axis[2]*np.sin(angle)
    u[0] = (1-np.cos(angle))*axis[0]*axis[1]-axis[2]*np.sin(angle)
    #l[0] = np.sin(angle)**2*axis[0]*axis[1] + np.cos(angle)*np.sin(angle)*axis[2]
    #u[0] = np.sin(angle)**2*axis[0]*axis[1] - np.cos(angle)*np.sin(angle)*axis[2]

    l[1] = (1-np.cos(angle))*axis[0]*axis[2]-axis[2]*np.sin(angle)
    u[1] = (1-np.cos(angle))*axis[0]*axis[2]+axis[2]*np.sin(angle)
    #l[1] = np.sin(angle)**2*axis[0]*axis[2] - np.cos(angle)*np.sin(angle)*axis[1]
    #u[1] = np.sin(angle)**2*axis[0]*axis[2] + np.cos(angle)*np.sin(angle)*axis[1]

    l[2] = (1-np.cos(angle))*axis[1]*axis[2]+axis[0]*np.sin(angle)
    u[2] = (1-np.cos(angle))*axis[1]*axis[2]-axis[0]*np.sin(angle)
    #l[2] = np.sin(angle)**2*axis[1]*axis[2] + np.cos(angle)*np.sin(angle)*axis[0]
    #u[2] = np.sin(angle)**2*axis[1]*axis[2] - np.cos(angle)*np.sin(angle)*axis[0]

    r = np.array([[d[0], u[0], u[1]],
                  [l[0], d[1], u[2]],
                  [l[1], l[2], d[2]]])

    r = np.round(r, decimals=thresh)
    print(r)
    return r

def refmat(axis):

    v = np.transpose(np.zeros(3))
    v[xmatrix]
    #h=I-v*v'
    return np.identity(3)-np.matmul(v,np.transpose(v))


def rotate():
    pass

def reflect():
    pass

def dilate():
    pass
