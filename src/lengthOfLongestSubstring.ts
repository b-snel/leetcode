// Given a string s, find the length of the longest substring without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.


function lengthOfLongestSubstring(s: string): number {
    let maxLength = 0;
    let seenMap = new Map<string, number>();
    let right = 0;

    for (let left = 0; left < s.length; left++) {
        while (right < s.length && !seenMap.has(s[right])) {
            seenMap.set(s[right], right);
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        }
        seenMap.delete(s[left]);
    }

    return maxLength;
};