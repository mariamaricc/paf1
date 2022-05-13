#include<iostream>
#include<math.h>
using namespace std;

class HarmonicOscillator
{
    private:
    double x,y,vx,vy,F,k,t = 0,dt,g = -9.81;
    void move();

    public:
    HarmonicOscillator(double v, double F, double theta, double x0, double y0, double step, double k);
    double range();
    double time();
};