// Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

// Example 1:

// Input: nums = [0,1]
// Output: 2
// Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
// Example 2:

// Input: nums = [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

// Constraints:

// 1 <= nums.length <= 105
// nums[i] is either 0 or 1.
// [0,1,0,1,0,1]
// [0,1,1,1]
// 
function findMaxLength(nums: number[]): number {
    let map = new Map<number, number>();
    map.set(0, -1);

    let count = 0;

    let maxLength = 0;
    for (let i = 0; i < nums.length; i ++){
        count += (nums[i] ? 1 : -1);
        if (map.has(count)){
            maxLength = Math.max(maxLength, i - (map.get(count) || 0))
        } else {
            map.set(count, i)
        }
    }
    return maxLength;
};
