#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
using namespace std;
using std::vector;
using std::string;

class Solution{
public: 
    int nthUglyNumber(int n){
        vector<int> res(1,1);
        int i2 = 0; int i3 = 0; int i5 = 0; //initialize to 0
        while (res.size() < n){
            int m2= res[i2]*2 , m3 = res[i3]*3, m5 = res[i5]*5;
            int mn = min(m2, min(m3, m5));
            if (mn == m2) ++i2; // check which one is the smallest, sort
            if (mn == m3) ++i3;
            if (mn == m5) ++i5;
            res.push_back(mn);
        }
        return res.back();
    }
};
