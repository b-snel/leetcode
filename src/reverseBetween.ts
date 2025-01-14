class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    let prev = null;
    let curr = head;
    while(curr){
        if(curr.next?.val === left){
            
        }
        let nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    }
    return head;
};