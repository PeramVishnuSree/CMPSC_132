# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        cur = self.head
        new = Node(value)

        if cur is None:
            self.head = new
            self.tail = new
            return

        if cur.value > new.value:
            new.next = cur
            self.head = new
            return

        while cur.next is not None:
            if cur.next.value > new.value:
                break
            cur = cur.next
        new.next = cur.next
        cur.next = new

        cur = self.head
        while cur.next != None:
            cur = cur.next
        self.tail = cur
        return


    def replicate(self):
        ans = SortedLinkedList()
        cur = self.head
        while cur != None:
            if cur.value <= 0 or type(cur.value) is float:
                ans.add(cur.value)
                ans.add(cur.value)
            else:
                for i in range(int(cur.value)):
                    ans.add(cur.value)

            cur = cur.next
        return ans
        pass


    def removeDuplicates(self):
        cur = self.head
        log = [cur.value]
        while cur.next != None:
            if cur.next.value not in log:
                cur = cur.next
                log.append(cur.value)
            else:
                cur.next = cur.next.next

if __name__=='__main__':
    import doctest
    # doctest.testmod()  # OR
    doctest.run_docstring_examples(SortedLinkedList, globals(), name='LAB4',verbose=True)