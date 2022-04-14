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

int polje(int niz[100],int a, int b)
{   
    int max, min,j=0;
    if(a<b){
        max = b;
        min = a;
    }
    else if(b<a)
    {
        max = a;
        min = b;
    }
    for(int i=min; i<=max; i++)
    {
        j++;
    }
    for(int i=0; i<j; i++)
    {
        niz[i] = i+min;
        cout << niz[i]<<",";
    }
    
    return j;
}

void funkcija(int niz[100],int j)
{
    for(int i=j-1; i>=0; i--)
    {
        cout << niz[i]<<" ";
    }
}

void funkcija2(int niz[100], int j, int idx1, int idx2)
{
    
    for(int i=)
}

int main()
{
    int niz[100];
    pravac(1,2,3,4);
    cout << endl;
    kruznica(1,1,0,0,1);
    cout << endl;
    int j = polje(niz,10,20);
    funkcija(niz,j);
    return 0;
}
