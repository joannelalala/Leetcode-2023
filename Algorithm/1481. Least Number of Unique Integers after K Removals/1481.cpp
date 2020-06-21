// Refer to https://www.acwing.com/file_system/file/content/whole/index/content/588309/

class Solution {

public:

    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
    
        int n = arr.size();
        
        sort(arr.begin(), arr.end());
        
        vector<int> counter;
        
        int cnt = 1;
        
        for (int i = 1; i<=n; i++){
            
            if (i == n|| arr[i] != arr[i-1]){
            
                counter.push_back(cnt);
                cnt = 0;
            }
            
            cnt++;
        }        
        
        sort(counter.begin(), counter.end());
        
        
        for (int i = 0 ; i < counter.size(); i++){
        
            if (k >= counter[i])
                k -= counter[i];
            else return counter.size() - i;
            
        }
        
        return 0;
    }
};
