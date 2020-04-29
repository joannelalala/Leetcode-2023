#include <stdio.h>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;
using std::vector;
using std::string;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> res;
        unordered_set<int> st;
        int cur = 0;
        for (int i = 0; i < 9; ++i) cur = cur << 3 | (s[i] & 7);
        for (int i = 9; i < s.size(); ++i) {
            cur = ((cur & 0x7ffffff) << 3) | (s[i] & 7);
            if (st.count(cur)) res.insert(s.substr(i - 9, 10)); // if happened before, then increment by 1
            else st.insert(cur); // otherwise, push back by 1
        }
        return vector<string>(res.begin(), res.end()); // convert back set to vector
    }
};
