'''
referred to https://youtu.be/A0g-aitC6k4
'''

class Solution {
public:
    int countTriplets(vector<int>& arr) {
        
        int N = arr.size();
        int prefix[N+1];
        int count = 0;
            
        prefix[0] = 0;
        
        for (int i=1 ; i <= N; i++){
            prefix[i] = prefix[i - 1] ^ arr[i - 1];
        }
        
        for (int i = 0; i < N; i++){
            for (int j = i + 1 ; j < N; j++){
                for (int k = j; k < N; k++){
                    
                    if ((prefix[j]^ prefix[i]) == (prefix[j]^prefix[k+1])){
                        count ++;
                    }
                }
                  
            }            
        }
        return count;
    }
};


