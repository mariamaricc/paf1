#include<iostream>
#include<math.h>
using namespace std;

class HarmonicOscillator
{
    private:
    double x[1000], v[1000], t[1000], a[1000], dt, m, k, time, g = -9.81;
    void move();

    public:
    HarmonicOscillator(double x0, double k, double m, double time, double step = 0.001);
    void oscillate();
};