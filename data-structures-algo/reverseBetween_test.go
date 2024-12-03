package main

import (
	"reflect"
	"testing"
)

func Test_reverseBetween(t *testing.T) {
	type args struct {
		head  *ListNode
		left  int
		right int
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		// Input:
		// [1,2,3]
		// 1
		// 2
		// Expected:
		// [2,1,3]
		{
			name: "nil tail",
			args: args{
				head:  &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}},
				left:  1,
				right: 2,
			},
			want: &ListNode{Val: 2, Next: &ListNode{Val: 1, Next: &ListNode{Val: 3}}},
		},
		{
			name: "test 1",
			args: args{
				head:  &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}},
				left:  2,
				right: 4,
			},
			want: &ListNode{Val: 1, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 5}}}}},
		},
		{
			name: "adjacent left and right",
			args: args{
				head:  &ListNode{Val: 3, Next: &ListNode{Val: 5}},
				left:  1,
				right: 2,
			},
			want: &ListNode{Val: 5, Next: &ListNode{Val: 3}},
		},
		{
			name: "single node",
			args: args{
				head:  &ListNode{Val: 1},
				left:  1,
				right: 1,
			},
			want: &ListNode{Val: 1},
		},
		{
			name: "reverse entire list",
			args: args{
				head:  &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}},
				left:  1,
				right: 3,
			},
			want: &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}},
		},
		{
			name: "reverse middle portion",
			args: args{
				head:  &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}},
				left:  2,
				right: 3,
			},
			want: &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}},
		},
		{
			name: "reverse last two nodes",
			args: args{
				head:  &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}},
				left:  2,
				right: 3,
			},
			want: &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 2}}},
		},
		{
			name: "nil head",
			args: args{
				head:  nil,
				left:  1,
				right: 1,
			},
			want: nil,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverseBetween(tt.args.head, tt.args.left, tt.args.right); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("reverseBetween() = %v, want %v", got, tt.want)
			}
		})
	}
}
