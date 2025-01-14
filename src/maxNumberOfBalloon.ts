// Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

// You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

// Example 1:



// Input: text = "nlaebolko"
// Output: 1
// Example 2:



// Input: text = "loonbalxballpoon"
// Output: 2
// Example 3:

// Input: text = "leetcode"
// Output: 0
 

// Constraints:

// 1 <= text.length <= 104
// text consists of lower case English letters only.
function maxNumberOfBalloons(text: string): number {
    let ans = 0;
    let count = new Map<string, number>()
    for (let char of text){
        count.set(char, (count.get(char) || 0) + 1)
    }
    console.log(count.get('l'))
    while ((count.get('b') || 0) > 0 && (count.get('a') || 0) > 0 && ((count.get('l') || 0) > 1) && ((count.get('o') || 0) > 1) && (count.get('n') || 0) > 0){
    ans += 1;
        for (let singleChar of ['b','a','n']){
            count.set(singleChar, (count.get(singleChar) || 0) - 1)
        }
        for (let doubleChar of ['l','o']){
            count.set(doubleChar, (count.get(doubleChar) || 0) - 2)
        }
    }

    return ans
};