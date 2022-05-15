#include<iostream>
#include<HarmonicOscillator.h>
#include<math.h>
using namespace std;


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
}