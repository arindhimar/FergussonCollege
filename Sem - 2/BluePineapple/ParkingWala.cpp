#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    string IA[4] = {"A", "B", "C", "D"};
    // string OA[4] = {"B", "A", "D", "C"};
    // string OA[4] = {"D", "A", "C", "B"};


    string OA[4] = {"D", "C", "B", "A"};

    
    unordered_map<string, int> indexMap;
    for (int i = 0; i < 4; i++) {
        indexMap[IA[i]] = i;//iska n ayega
    }

    string temp;

    for (int i = 0; i < 4; i++) {
        if (IA[i] != OA[i]) {
            int index = indexMap[OA[i]];
            temp = IA[i];
            IA[i] = IA[index];
            // indexMap[IA[index]] = index;
            IA[index] = temp;
            indexMap[temp] = index;
        }
        
    }

    
    for (const auto& car : IA) {
        cout << car << " ";
    }
    cout << endl;

    return 0;
}