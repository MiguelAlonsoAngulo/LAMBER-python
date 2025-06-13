from lambertbattin.vector import *;
from lambertbattin.seebatt import *;
from lambertbattin.seebattk import *;

eps = 1e-10;

def v_equals(v1, v2):
    if (len(v1) == len(v2)):
        equal = True;

        for i in range(0, len(v1)):
            if (abs(v1[i] - v2[i]) > eps):
                equal = False;
                break;

        return equal;
    else:
        return False;

def test_v_create_01():
    v1 = [0.0, 0.0, 0.0, 0.0, 0.0];

    assert(v_equals(v_create(5), v1)), "failure in v_create_01";

def test_v_dot_01():
    r = 80;
    v1 = [0,1,2,3,4];
    v2 = [5,6,7,8,9];

    assert(abs(v_dot(v1, v2) - r) < eps), "failure in v_dot_01";

def test_v_norm_01():
    r = 5.47722557505166;
    v1 = [0,1,2,3,4];

    assert(abs(v_norm(v1) - r) < eps), "failure in v_norm_01";

def test_v_cross_01():
    v1 = [1,2,3];
    v2 = [4,5,6];
    r = [-3,6,-3];

    assert(v_equals(v_cross(v1, v2), r)), "failure in v_cross_01";

def test_v_seebatt_01():
    r = 7.56024881510026;

    assert(abs(seebatt(3) - r) < eps), "failure in v_seebatt_01";

def test_v_seebattk_01():
    r = 0.230769230769231;

    assert(abs(seebattk(3) - r) < eps), "failure in v_seebattk_01";
