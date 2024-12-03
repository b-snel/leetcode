package main

func MinStartValue(nums []int) int {
	prefixSum := 0
	minPrefixSum := 0

	for _, num := range nums {
		prefixSum += num
		minPrefixSum = min(minPrefixSum, prefixSum)
	}

	return 1 - minPrefixSum
}
