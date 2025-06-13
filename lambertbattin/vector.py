import math as m

def v_create(n):
    if (n > 0):
        return [0.0]*n;
    else:
        raise Exception();

def v_dot(v1, v2):
    if (len(v1) == len(v2)):
        r = 0.0;

        for i in range(0, len(v1)):
            r = r + v1[i]*v2[i];

        return r;
    else:
        raise Exception();

def v_norm(v):
    r = 0.0;

    for i in range(0, len(v)):
        r = r + v[i]*v[i];

    return m.sqrt(r);

def v_cross(v1, v2):
    if (len(v1) == 3) and (len(v2) == 3):
        v3 = v_create(3);

        v3[0] = v1[1]*v2[2] - v1[2]*v2[1];
        v3[1] = v1[2]*v2[0] - v1[0]*v2[2];
        v3[2] = v1[0]*v2[1] - v1[1]*v2[0];

        return v3;
    else:
        raise Exception();
