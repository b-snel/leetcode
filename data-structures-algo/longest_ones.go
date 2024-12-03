package main

func LongestOnes(nums []int, k int) (resp int) {
	left, right := 0, 0
	for ; right < len(nums); right++ {
		if nums[right] == 0 {
			k--
		}
		if k < 0 {
			resp = max(resp, right-left)
			if nums[left] == 0 {
				k++
			}
			left++
		}
	}
	return max(resp, right-left)
}

func LongestOnesEarlyEscape(nums []int, k int) int {
	ans, curr, left := 0, 0, 0
	for right := 0; right < len(nums); right++ {
		if curr+k == len(nums) {
			return len(nums)
		}
		curr += nums[right]

		for curr+k <= (right - left) {
			if nums[left] == 1 {
				curr--
			}
			left++
		}
		if ans < curr+k {
			ans = curr + k
		}
	}

	return ans
}
