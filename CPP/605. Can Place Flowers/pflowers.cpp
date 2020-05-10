class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);
        for (int i=1; i < flowerbed.size() -1; i++){
            if (flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0){
                --n;
                ++i;
            }
        }
        return n <=0;
    }
};

class Soution{
    public:
    bool canPlaceFlowers(vector<int>&bed, int n){
        for (int i; i < bed.size(); i++){
            if (!bed[i] &&(i ==0 || !bed[i-1]) && (i == bed.size() -1 ||
                                                  !bed[i+1])){
                bed[i]==1;
                n--;
            }
            
        }
        return n <=0;
    }
    
};
