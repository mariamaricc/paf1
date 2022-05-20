#include<iostream>
#include<HarmonicOscillator.h>
#include<math.h>
using namespace std;

<<<<<<< HEAD
void HarmonicOscillator::move()
{
    vx += double(0);
    F = -k*x;
    x += vx * dt;
    y += vy * dt;
    t += dt;
}
HarmonicOscillator::HarmonicOscillator(double v,double F, double theta, double x0, double y0, double step = 0.001, double k)
{
    vx = v * cos(3.141592653589793238463 * theta/180);
    vy = v * sin(3.141592653589793238463 * theta/180);
    x = x0;
    y = y0;
    dt = step;
}
double HarmonicOscillator::time()
{
    double time=0;

    while(y>=0){
        move();
    }
    time = t;
    return time;
}
double HarmonicOscillator::range()
{
    double range=0;

    while(y>=0){
        move();
    }
    range = x;
    return range;
=======

HarmonicOscillator::HarmonicOscillator(double x0, double k, double m, double time, double step)
{
    x[0] = x0;
    v[0] = 0.;
    a[0] = - k * x0 / m;
    t[0] = 0;
    dt = step;
    m = m;
    k = k;
    time = time;
}
void HarmonicOscillator::oscillate()
{
    move();
>>>>>>> 68d7a10128e1a045396ce299e6dff5ebfd0a91a9
}