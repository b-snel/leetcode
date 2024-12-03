package main

func GetAverages(nums []int, k int) []int {
	windowSize := k*2 + 1
	n := len(nums)
	averages := make([]int, n)
	for i := range averages {
		averages[i] = -1
	}
	if windowSize > n {
		return averages
	}
	windowSum := 0
	for i := 0; i < windowSize; i++ {
		windowSum += nums[i]
	}
	averages[k] = windowSum / windowSize
	for i := windowSize; i < n; i++ {
		windowSum = windowSum - nums[i-windowSize] + nums[i]
		averages[i-k] = windowSum / windowSize
	}
	return averages
}
