package main

import (
	"testing"
)

func TestLongestOnes(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{
			name:     "basic test",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        2,
			expected: 6,
		},
		{
			name:     "zero start",
			nums:     []int{0, 0, 0, 1},
			k:        4,
			expected: 4,
		},
		{
			name:     "early escape",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        2,
			expected: 6,
		},
		{
			name:     "early escape 2",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        3,
			expected: 10,
		},

		// Add more test cases here
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := LongestOnes(tt.nums, tt.k); got != tt.expected {
				t.Errorf("LongestOnes() = %v, want %v", got, tt.expected)
			}
		})
	}
}

func TestBothImplementations(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{
			name:     "basic test",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        2,
			expected: 6,
		},
		{
			name:     "zero start",
			nums:     []int{0, 0, 0, 1},
			k:        4,
			expected: 4,
		},
		{
			name:     "early escape",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        2,
			expected: 6,
		},
		{
			name:     "early escape 2",
			nums:     []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        3,
			expected: 10,
		},

		// Add more test cases here
	}

	for _, tt := range tests {
		t.Run(tt.name+" (Regular)", func(t *testing.T) {
			if got := LongestOnes(tt.nums, tt.k); got != tt.expected {
				t.Errorf("LongestOnes() = %v, want %v", got, tt.expected)
			}
		})

		t.Run(tt.name+" (EarlyEscape)", func(t *testing.T) {
			if got := LongestOnesEarlyEscape(tt.nums, tt.k); got != tt.expected {
				t.Errorf("LongestOnesEarlyEscape() = %v, want %v", got, tt.expected)
			}
		})
	}
}

func BenchmarkLongestOnes(b *testing.B) {
	testCases := []struct {
		name string
		nums []int
		k    int
	}{
		{
			name: "small input",
			nums: []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:    2,
		},
		{
			name: "medium input",
			nums: generateArray(1000),
			k:    50,
		},
		{
			name: "large input",
			nums: generateArray(10000),
			k:    500,
		},
	}

	for _, tc := range testCases {
		b.Run("Regular_"+tc.name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				LongestOnes(tc.nums, tc.k)
			}
		})

		b.Run("EarlyEscape_"+tc.name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				LongestOnesEarlyEscape(tc.nums, tc.k)
			}
		})
	}
}

func generateArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		if i%3 == 0 {
			arr[i] = 0
		} else {
			arr[i] = 1
		}
	}
	return arr
}
