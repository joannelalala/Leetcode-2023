let twoSum = function(numbers, target){
    let leftPointer = 0;
    let rightPointer = numbers.length - 1;
    
    let result = []
    
    // two pointers start with the while loop when leftPointer < rightPointer
    while(leftPointer < rightPointer){
        let leftElement = numbers[leftPointer];
        let rightElement = numbers[rightPointer];
        if(leftElement + rightElement === target){ // if match, add to result 
            result.push(leftPointer + 1);
            result.push(rightPointer + 1);
            break;
        }else if(leftElement + rightElement > target){
            rightPointer --;
        }else{
            leftPointer ++;
        }
    }
    return result;
};

// Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
