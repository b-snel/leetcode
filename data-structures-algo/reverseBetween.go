package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]

// Input: head = [3,5], left = 1, right = 2

// Input:
// [1,2,3]
// 1
// 2
// Expected:
// [2,1,3]
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || head.Next == nil || left == right {
		return head
	}
	var dummy *ListNode = head
	var curr *ListNode = head
	var prev *ListNode = nil
	var leftPrev *ListNode = head
	// Move the ptr to the first break
	for i := 0; i < left-1; i++ {
		nextNode := curr.Next
		prev = curr
		leftPrev = prev
		curr = nextNode
	}
	// Flip nodes within range
	for i := left - 1; i < right; i++ {
		nextNode := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextNode
	}
	tail := leftPrev.Next
	if tail == nil {
		// If there is no tail, then we are reversing the entire list
		dummy.Next = curr
		return prev
	} else {
		// If there is a tail, then we are reversing a sublist
		tail.Next = curr
		leftPrev.Next = prev
		return dummy
	}
}
