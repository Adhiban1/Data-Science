// incomplete c++ project...

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
typedef vector<vector<float>> Matrix;

Matrix matSum(Matrix a, Matrix b)
{
    int i = a.size();
    int j = a[0].size();
    for (int k = 0; k < i; k++)
        for (int l = 0; l < j; l++)
            a[k][l] = a[k][l] + b[k][l];
    return a;
}

Matrix matSub(Matrix a, Matrix b)
{
    int i = a.size();
    int j = a[0].size();
    for (int k = 0; k < i; k++)
        for (int l = 0; l < j; l++)
            a[k][l] = a[k][l] - b[k][l];
    return a;
}

void matPrint(Matrix a)
{
    for (vector<float> i : a)
    {
        for (float j : i)
        {
            cout << j << ' ';
        }
        cout << '\n';
    }
}

Matrix matDot(Matrix a, Matrix b) {
    int i = a.size();
    int j = a[0].size();
    int k = b[0].size();
    Matrix c;
    for(int i1 = 0; i1 < i; i1++) {
        vector<float> temp;
        for(int k1 = 0; k1 < k; k1++) {
            float element = 0;
            for(int j1 = 0; j1 < j; j1++) {
                element += a[i1][j1] * b[j1][k1];
            }
            temp.push_back(element);
        }
        c.push_back(temp);
    }
    return c;
}

Matrix scalarMatSum(float a, Matrix b) {
    for(int i = 0; i < b.size(); i++) {
        for(int j = 0; j < b[0].size(); j++) {
            b[i][j] = b[i][j] + a;
        }
    }
    return b;
}

Matrix scalarMatMul(float a, Matrix b) {
    for(int i = 0; i < b.size(); i++) {
        for(int j = 0; j < b[0].size(); j++) {
            b[i][j] = b[i][j] * a;
        }
    }
    return b;
}

float randint(int a, int b) {
    return rand() % (b-a+1) + a;
}

Matrix randMatrix(int a, int b, int s, int e) {
    Matrix c;
    for(int i = 0; i < a; i++){
        vector<float> temp;
        for(int j = 0; j < b; j++) {
            temp.push_back(randint(s, e));
        }
        c.push_back(temp);
    }
    return c;
}

int main()
{   
    Matrix X = randMatrix(10, 1, 0, 100);
    Matrix W = randMatrix(1, 10, 0, 100);
    float B = randint(0, 100);
    float Y = B + matDot(W, X)[0][0];

    Matrix w = randMatrix(1, 10, 0, 100);
    float b = randint(0, 100);

    float loss = pow((Y - matDot(w,X)[0][0] - b), 2);
}