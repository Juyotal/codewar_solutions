from linkList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        visited = set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else: 
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll



customLL = LinkedList()
customLL.generate(10, 0, 7)    

print(customLL)
newll = removeDups(customLL)
print(newll)
