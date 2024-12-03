package main

import "testing"

func TestMinStartValue(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{nums: []int{-3, 2, -3, 4, 2}},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MinStartValue(tt.args.nums); got != tt.want {
				t.Errorf("MinStartValue() = %v, want %v", got, tt.want)
			}
		})
	}
}
