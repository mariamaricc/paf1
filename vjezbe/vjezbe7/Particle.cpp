#include<iostream>
#include<Particle.h>
#include<math.h>
using namespace std;

void Particle::move()
{
    vx += double(0);
    vy += g * dt;
    x += vx * dt;
    y += vy * dt;
    t += dt;
}
Particle::Particle(double v, double theta, double x0, double y0, double step)
{
    vx = v * cos(3.141592653589793238463 * theta/180);
    vy = v * sin(3.141592653589793238463 * theta/180);
    x = x0;
    y = y0;
    dt = step;
}
double Particle::time()
{
    double time=0;

    while(y>=0){
        move();
    }
    time = t;
    return time;
}
double Particle::range()
{
    double range=0;

    while(y>=0){
        move();
    }
    range = x;
    return range;
}