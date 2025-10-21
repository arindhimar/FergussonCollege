#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v = {1, 2, 4, 2, 3, 1, 4, 5, 1};

    int n = v.size();
    
    int second_highest = INT_MIN;

    int highest = v[0];

    for(int i=1;i<n;i++){
        if(v[i] > highest) {
            second_highest = highest;
            highest = v[i];
        } else if(v[i] > second_highest && v[i] < highest) {
            second_highest = v[i];
        }
    }

    return 0;
}