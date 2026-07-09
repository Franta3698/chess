
array1 = list()
array2 = list()

def create_node(node):
     return
def node_to_array1(node):
        array1.append(str(node.val))
        if node.next is None:
            return
        node_to_array1(node.next)

def node_to_array2(node):
        array2.append(str(node.val))
        if node.next is None:
            return
        node_to_array2(node.next)

def list_to_reverse_int(numList):
     stringList = "".join(numList[::-1])
     return int(stringList)

def sum_to_nodeList(num1, num2):

     return num1 + num2

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_to_array1(l1)
        node_to_array2(l2)

        num1 = list_to_reverse_int(array1)
        num2 = list_to_reverse_int(array2)

        summed = num1 + num2

        




#First linked list: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

#Second linked list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

print_list(l1)
print_list(l2)

node_to_array1(l1)
node_to_array2(l2)

print(array1)
print(array2)
print(list_to_reverse_int(array1))
print(list_to_reverse_int(array2))

num1 = list_to_reverse_int(array1)
num2 = list_to_reverse_int(array2)


res = num1 + num2

resStr = list(str(res)[::-1])


for num in resStr:
     ListNode(num)
     pass






