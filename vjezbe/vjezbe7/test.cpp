#include <iostream>
#include <Particle.h>
using namespace std;

int main()
{
    Particle p1(100, 45, 0, 0);
    cout << "domet= " << p1.range() << endl;
    cout << "vrijeme= " << p1.time()<< endl;

    Particle p2(10, 60, 0, 0);
    cout << "domet " << p2.range()<< endl;
    cout << "vrijeme= " << p2.time()<< endl;

    return 0;
}