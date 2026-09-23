#递归加法
def recursive_sum(n):
    if n==1:
        return 1

    return n+recursive_sum(n-1)

print(recursive_sum(5))
print()


#递归乘法
def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)

print(factorial(5))
print()


#递归链表
def recursive_traverse(node):
    if node is None:
        return

    print(node.val)
    recursive_traverse(node.next)

#print放前面是正序，放后面是倒序
