#include<iostream>
using namespace std;

void sustav_jednadzbi(float a1, float b1, float c1, float a2, float b2, float c2)
{
    float x;
    float y;
    float k;
    k = (a1*b2 - a2*b1);
    if(k != 0 && a1 != 0)
    {
        y = (a1*c2 - a2*c1)/(a1*b2 - a2*b1);
        cout << "y = " << y;
        x = (c1 - b1*y)/a1;
        cout << endl;
        cout << "x = " << x;
    }
    else{
        cout << "nije moguce dijeliti s nulom";
    }
}

int main()
{
    sustav_jednadzbi(1,2,2,1,1,1);
}