#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>
#include <iomanip>
#include <stack>
using namespace std;

const long double PI = 3.14159265358;
const long double CONST_TIME = 10;

struct Point{
    long double x, y;
    
};

Point operator+(Point a, Point b){
    return {b.x + a.x, b.y + a.y};
}

struct Vector{
    long double x, y, length, speed, angle;
    void init(long double input_speed, long double input_length){
        this -> speed = input_speed;
        this -> length = input_length;
        this -> x = length;
        this -> y = 0;
        this -> angle = 0;
    }
    void update_pos(long double time){
        this -> angle = this -> speed * PI / CONST_TIME * time;
        //this -> angle = this -> angle - (this -> angle / (PI * 2)) * (PI * 2);
        this -> x = this -> length * cos(this -> angle);
        this -> y = this -> length * sin(this -> angle);
    }
};

struct Construction{
    int n;
    vector<Vector> v;
    vector<Point> p;
    void init(int input_n, vector<Vector> input_v){
        this -> n = input_n;
        this -> v = input_v;
        p.resize(n);
    }
    void update_vectors(long double time){
        Point tmp = {0, 0};
        for (int i = 0; i < n; ++i)
        {
            v[i].update_pos(time);
            tmp = tmp + (Point){v[i].x, v[i].y};
            p[i] = tmp;
        }
    }
};
