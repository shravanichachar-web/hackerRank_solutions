#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    // Fast I/O for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    cin >> q;
    
    set<int> s;
    
    while (q--) {
        int type, x;
        cin >> type >> x;
        
        if (type == 1) {
            // Type 1: Add element x to the set
            s.insert(x);
        } 
        else if (type == 2) {
            // Type 2: Delete element x from the set
            s.erase(x);
        } 
        else if (type == 3) {
            // Type 3: Check if element x is in the set
            set<int>::iterator itr = s.find(x);
            if (itr != s.end()) {
                cout << "Yes\n";
            } else {
                cout << "No\n";
            }
        }
    }
    
    return 0;
}
