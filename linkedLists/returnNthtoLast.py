from linkList import LinkedList

def nthToLast(ll, n):
    p1 = ll.head
    p2 = ll.head

    for i in range (n):
        if p2 == None:
            return
        else:
            p2 = p2.next
    
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1
    

customLL = LinkedList()
customLL.generate(10, 0, 98)    

print(customLL)
newll = nthToLast(customLL, 3)
print(newll)
