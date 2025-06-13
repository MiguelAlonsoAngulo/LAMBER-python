from lambertbattin import *;

def main():
    r1 = [20.0e6, 20.0e6, 0];  # [m]
    r2 = [-20.0e6, 10.0e6, 0]; # [m]
    tof = 1.0 * 86400;
    V1, V2 = LAMBERTBATTIN(r1, r2, 'retro', tof);

    print(V1);
    print(V2);

    input();

if __name__ == '__main__':
    main();
