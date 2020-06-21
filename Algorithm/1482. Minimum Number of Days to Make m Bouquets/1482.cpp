class Solution {

    int n;

public:

    int minDays(vector<int>& bloomDay, int m, int K) {
    
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        
        // impossible case
        if ((long long)m*K > (long long)bloomDay.size()) return -1;
        
        n = bloomDay.size();
        int left = INT_MAX;
        int right = INT_MIN;
        
        for (int i = 0; i < n; i ++){
        
            left = min(left, bloomDay[i]);
            right = max(right, bloomDay[i]);
        
        }
        
        while (left < right){
        
            int mid = left + ((right-left) >> 1);
            
            if (!check(bloomDay, m, K, mid)) left = mid+1;
            
            else right = mid;
        
        }
        
        return left;           
    }
    
    bool check(vector<int> & bloomDay, int m, int K, int target){
    
        int cnt = 0 ; 
        int len = 0;
        
        for (int i = 0; i < n; i++){
        
            if (bloomDay[i] <= target){
            
                ++len;
                
                if (len = K){++cnt; len = 0;}
            }
            
            else len = 0;
        }
        
        return cnt >= m;
       
    }
};
