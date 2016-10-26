#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys, math

def form(a, b, x, y):
        return ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150))

def main(args):
        if len(args) != 2:
            print "Usage: ./202invendus a b"
            sys.exit(2)

        try:
            a = int(args[0])
            b = int(args[1])
        except:
            print "Usage: Number must be an INT over than 50."
            sys.exit(2)
        if a < 51 or b < 51:
            print "Usage: Number must be an INT over than 50."
            sys.exit(2)

        print "\t\tX=10\tX=20\tX=30\tX=40\tX=50\tloi de Y"

        res = list(range(6))
        for i in range(6):
            res[i] = list(range(6))
        y = 10
        while y < 51:
            print "Y=%d\t\t" % y,
            x = 10
            while x < 51:
                res[y/10-1][x/10-1] = form(float(a), float(b), float(x), float(y))
                print "%.3f\t" % form(float(a), float(b), float(x), float(y)),
                x = x + 10
            res[y/10-1][5] = res[y/10-1][0] + res[y/10-1][1] + res[y/10-1][2] + res[y/10-1][3] + res[y/10-1][4];
            print "%.3f" % res[y/10-1][5]
            y = y + 10
        print "loi de X\t",
        i = 0
        while i < 5:
            res[5][i] = res[0][i] + res[1][i] + res[2][i] + res[3][i] + res[4][i];
            print "%.3f\t" % res[5][i],
            i = i + 1
        print "1\n\n"

        z = list(range(9))
        for i in range(9):
            z[i] = list(range(9))

        z[0] = res[0][0];
        z[1] = res[0][1] + res[1][0];
        z[2] = res[0][2] + res[2][0] + res[1][1];
        z[3] = res[3][0] + res[0][3] + res[1][2] + res[2][1];
        z[4] = res[4][0] + res[0][4] + res[3][1] + res[1][3] + res[2][2]; # HO la jolie pyramide :)
        z[5] = res[1][4] + res[4][1] + res[2][3] + res[3][2];
        z[6] = res[2][4] + res[4][2] + res[3][3];
        z[7] = res[3][4] + res[4][3];
        z[8] = res[4][4];
        print "z\t\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal\n",
        print "p(Z=z)\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t1\n\n" % (z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8]),

        ex = 10*res[5][0] + 20*res[5][1] + 30*res[5][2] + 40*res[5][3] + 50*res[5][4];
        ey = 10*res[0][5] + 20*res[1][5] + 30*res[2][5] + 40*res[3][5] + 50*res[4][5];
        ez = 20*z[0] + 30*z[1] + 40*z[2] + 50*z[3] + 60*z[4] + 70*z[5] + 80*z[6] + 90*z[7] + 100*z[8];
        print "espérance de X:\t\t%.3f\n" % ex,
        vx = 100*res[5][0] + 400*res[5][1] + 900*res[5][2] + 1600*res[5][3] + 2500*res[5][4] - (ex*ex);
        print "variance de X:\t\t%.3f\n" % vx,
        print "écart type de X:\t%.3f\n" % math.sqrt(vx),
        print "espérance de Y:\t\t%.3f\n" % ey,
        vy = 100*res[0][5] + 400*res[1][5] + 900*res[2][5] + 1600*res[3][5] + 2500*res[4][5] - (ey*ey);
        print "variance de Y:\t\t%.3f\n" % vy,
        print "écart type de Y:\t%.3f\n" % math.sqrt(vy),
        print "espérance de Z:\t\t%.3f\n" % ez,
        vz = 400*z[0] + 900*z[1] + 1600*z[2] + 2500*z[3] + 3600*z[4] + 4900*z[5] + 6400*z[6] + 8100*z[7] + 10000*z[8] - (ez*ez);
        print "variance de Z:\t\t%.3f\n" % vz,
        print "écart type de Z:\t%.3f\n" % math.sqrt(vz),

if __name__ == "__main__":
    main(sys.argv[1:])
