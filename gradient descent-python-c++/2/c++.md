# Gradient Descent in c++
Importing libraries
```c++
#include <iostream>
#include <vector>
#include <cmath>
```
```c++
using namespace std;
```
Let us take matrix element type as **float**, in c++ we are going to use `vector` to make matrix. Let us take `vector<vector<float>>` as Matrix. Typing `vector<vector<float>>` is large, so let us give the name `Matrix` to it.
```c++
typedef vector<vector<float>> Matrix;
```
Matrix sum function
```c++
Matrix matSum(Matrix a, Matrix b)
{
    int i = a.size();
    int j = a[0].size();
    for (int k = 0; k < i; k++)
        for (int l = 0; l < j; l++)
            a[k][l] = a[k][l] + b[k][l];
    return a;
}
```
Matrix Subtraction function
```c++
Matrix matSub(Matrix a, Matrix b)
{
    int i = a.size();
    int j = a[0].size();
    for (int k = 0; k < i; k++)
        for (int l = 0; l < j; l++)
            a[k][l] = a[k][l] - b[k][l];
    return a;
}
```
Matrix Print function
```c++
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
```
Matrix dot product function
```c++
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
```
Adding scalar to Matrix function
```c++
Matrix scalarMatSum(float a, Matrix b) {
    for(int i = 0; i < b.size(); i++) {
        for(int j = 0; j < b[0].size(); j++) {
            b[i][j] = b[i][j] + a;
        }
    }
    return b;
}
```
Multiplying scalar to Matrix function
```c++
Matrix scalarMatMul(float a, Matrix b) {
    for(int i = 0; i < b.size(); i++) {
        for(int j = 0; j < b[0].size(); j++) {
            b[i][j] = b[i][j] * a;
        }
    }
    return b;
}
```
Random number function
```c++
float randint(int a, int b) {
    return rand() % (b-a+1) + a;
}
```
Matrix with random elements function
```c++
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
```
***This c++ project is not completed...***
