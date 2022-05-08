#include<iostream>
#include<math.h>
using namespace std;

class Particle
{
    private:
    double x,y,vx,vy,t = 0,dt,g = -9.81;
    void move();

    public:
    Particle(double v, double theta, double x0, double y0, double step = 0.001);
    double range();
    double time();
};