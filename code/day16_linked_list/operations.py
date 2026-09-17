#合成函数

def delete_value(head,target):
    if head is None:
        return None

    if head.val == target:
        return head.next

    current_delete = head

    while current_delete.next:
         if current_delete.next.val == target:
                current_delete.next=current_delete.next.next
                break

                current_delete = current_delete.next

    return head


#反转链表
#需要三个指针
#prev 前一个节点
#current 当前正在处理的节点
#next_node 先保存原来的下一个节点

def reverse_list(head):
     prev = None
     current = head

     while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

     return prev
