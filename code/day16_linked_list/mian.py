#节点类
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#创建节点
node_a = ListNode(10)
node_b = ListNode(20)
node_c = ListNode(30)

#连接
node_a.next = node_b
node_b.next = node_c

print(node_a.val)
print(node_a.next.val)
print(node_a.next.next.val)
print()


#再链表头部插入新节点
new_node = ListNode(5)

new_node.next = node_a

head_node = new_node

#遍历链表
current_node = head_node

while current_node:
    print(current_node.val)
    current_node = current_node.next

new_tail = ListNode(40)

tail_node = head_node

while tail_node.next:
    tail_node = tail_node.next

tail_node.next = new_tail

current_node_2 = head_node

while current_node_2:
    print(current_node_2.val)
    current_node_2 = current_node_2.next
