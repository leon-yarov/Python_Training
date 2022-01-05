# recursive function merge two sorted lists
def Merge(list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + Merge(list1[1:], list2)
    if list1[0] > list2[0]:
        return [list2[0]] + Merge(list1, list2[1:])
    return [list1[0]] + Merge(list1[1:], list2[1:])


lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 3, 4, 6, 8, 10]
print(Merge(lst1, lst2))  # => [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]


def Mergesort(list):
    if len(list) <= 1:
        return list
    return Merge(Mergesort(list[:len(list) // 2]), Mergesort(list[len(list) // 2:]))


lst = [1, 19, 3, 10, 5, 3, 9]
print(Mergesort(lst))  # => [1, 3, 3, 5, 9, 10, 19]


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self is None:
            return
        Node.print_tree(self.left)
        print(self.data, end=' ')
        Node.print_tree(self.right)

    def mirror(self):
        if self is None:
            return
        Node.mirror(self.left)
        Node.mirror(self.right)
        self.left, self.right = self.right, self.left


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
root.print_tree()
print()
root.mirror()
root.print_tree()
print()


def isAnyOptionToSteal(n, weight):
    if n == 0: return True
    if n < 0: return False
    if len(weight) == 0: return False
    return isAnyOptionToSteal(n - weight[0], weight) or isAnyOptionToSteal(n - weight[0], weight[1:])


print(isAnyOptionToSteal(10, (4, 3)))  # => True
print(isAnyOptionToSteal(10, (4,)))  # => False
print(isAnyOptionToSteal(10, (4, 3, 2)))  # => True


def memo(f):
    cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return memoized


@memo  # equal to fun = memo(fun)
def fun(n):
    if n < 3:
        return n
    else:
        return fun(n - 1) + fun(n - 2) + fun(n - 3)


print(fun(35))
