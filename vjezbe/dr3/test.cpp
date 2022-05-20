#include <iostream>
#include <HarmonicOscillator.h>

using namespace std;

int main()
{
    HarmonicOscillator obj1(0.5, 10, 2, 1000);
    obj1.oscillate();
}