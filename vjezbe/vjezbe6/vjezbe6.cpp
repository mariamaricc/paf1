#include<iostream>
#include<cmath>
using namespace std;

void pravac(float x1, float y1, float x2,float y2)
{
    float k = (y2-y1)/(x2-x1);
    float l = y1 - k*x1;
    cout << "y = " << k << "x + " << l;
}

void kruznica(float x,float y, float p, float q, float r)
{
    float r1;
    r1 = sqrt((x-p)*(x-p)+(y-q)*(y-q));
    if (r1<r)
        cout << "tocka se nalazi unutar kruznice";
    else
        cout << "tocka se ne nalazi unutar kruznice";
}

void polje(int a, int b)
{
    if(a<b){
        for(int i=a+1; i<b; i++)
        cout << i;
    }
    else if(b<a){
        for(int i=b+1; i<a; i++)
        cout << i;
    }
    else
        cout << "nema cijelih brojeva izmedu a i b";

}



int main()
{
    pravac(1,2,3,4);
    cout << endl;
    kruznica(1,1,0,0,1);
    cout << endl;
    polje(-5,-5);
    return 0;
}
