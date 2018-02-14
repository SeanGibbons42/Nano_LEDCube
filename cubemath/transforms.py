import numpy as np

def rotmat(angle, axis_num, thresh = 3):
    angle = np.deg2rad(angle)
    d = []
    #assemble the components of the rotation matrix.
    axis = [0, 0, 0]; axis[axis_num] = 1
    for v in axis:
        r_diag = np.cos(angle)+v**2*(1-np.cos(angle))
        d.append(r_diag)

    l = [0, 0, 0]; u = [0, 0, 0]
    l[0] = (1-np.cos(angle))*axis[0]*axis[1]+axis[2]*np.sin(angle)
    u[0] = (1-np.cos(angle))*axis[0]*axis[1]-axis[2]*np.sin(angle)

    l[1] = (1-np.cos(angle))*axis[0]*axis[2]-axis[1]*np.sin(angle)
    u[1] = (1-np.cos(angle))*axis[0]*axis[2]+axis[1]*np.sin(angle)

    l[2] = (1-np.cos(angle))*axis[1]*axis[2]+axis[0]*np.sin(angle)
    u[2] = (1-np.cos(angle))*axis[1]*axis[2]-axis[0]*np.sin(angle)

    r = np.array([[d[0], u[0], u[1]],
                  [l[0], d[1], u[2]],
                  [l[1], l[2], d[2]]])

    r = np.round(r, decimals=thresh)

    return r

def refmat(axis):

    v = np.zeros(3)
    if axis == 0:
        v[1] = 1
    elif axis == 1:
        v[0] = 1
    elif axis == 2:
        v[2] = 1
    else:
        raise ValueError("Invalid Axis Selection. Use 0=X, 1=Y, 2=Z")

    #h=I-v*v'
    return np.identity(3)-2*np.outer(v,np.transpose(v))
