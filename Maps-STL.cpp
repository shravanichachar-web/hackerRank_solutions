#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    // Fast I/O for performance on large test cases
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    cin >> q;
    
    map<string, int> m;
    
    while (q--) {
        int type;
        cin >> type;
        
        if (type == 1) {
            // Type 1: Add marks Y to student X
            string name;
            int marks;
            cin >> name >> marks;
            m[name] += marks; // If name doesn't exist, it initializes to 0 before adding
        } 
        else if (type == 2) {
            // Type 2: Erase the marks of student X
            string name;
            cin >> name;
            m.erase(name);
        } 
        else if (type == 3) {
            // Type 3: Print the marks of student X
            string name;
            cin >> name;
            
            map<string, int>::iterator itr = m.find(name);
            
            if (itr != m.end()) {
                cout << itr->second << "\n";
            } else {
                cout << "0\n";
            }
        }
    }
    
    return 0;
}
