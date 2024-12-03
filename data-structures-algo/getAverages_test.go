package main

import (
	"reflect"
	"testing"
)

func TestGetAverages(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "test1",
			args: args{
				nums: []int{7, 4, 3, 9, 1, 8, 5, 2, 6}, k: 3,
			},
			want: []int{-1, -1, -1, 5, 4, 4, -1, -1, -1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetAverages(tt.args.nums, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetAverages() = %v, want %v", got, tt.want)
			}
		})
	}
}
