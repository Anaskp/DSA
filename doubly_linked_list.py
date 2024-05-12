class Node:
    def __init__( self, data=None, next=None, prev=None ):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_linked_list:
    def __init__( self ):
        self.head = None

    def print( self ):

        if self.head is None:
            print( 'Empty' )
            return
        
        itr = self.head
        while( itr ):
            print( itr.prev if itr.prev is None else itr.prev.data, itr.data , itr.next if itr.next is None else itr.next.data )
            itr = itr.next

    def insert_at_beg( self, data ):
        node = Node( data, self.head )
        if self.head is not None:
            self.head.prev = node
        self.head = node


    def insert_at_end( self, data ):
        if self.head is None:
            self.head = Node( data, None, self.head )
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node( data, None, itr )

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.insert_at_beg( data )
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1 :
                node = Node( data, itr.next, itr.next.prev )
                itr.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    def get_length( self ):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def delete_at_beg( self ):
        if self.head is None:
            print( 'Empty' )
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end( self ):
        if self.head is None:
            print( 'Empty' )
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def delete_at( self, index ):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.delete_at_beg()
            return
        if index == self.get_length() - 1 :
            self.delete_at_end()
            return

        count = 0
        itr = self.head
        while itr :
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            count += 1
            itr = itr.next

    def insert_after_value( self, data_after, data ):
        if self.head is None:
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node( data, itr.next, itr )
                node.next.prev = node
                itr.next = node
                break
            itr = itr.next
        
        if itr is None:
            raise Exception( 'No data found' )


l1 = Doubly_linked_list()
l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_beg(30)
l1.insert_at_beg(40)
# l1.insert_at_end(50)
# l1.insert_at_end(60)
# l1.insert_at_end(70)
# l1.insert_at_end(80)
l1.print()
# l1.insert_at(55, 1)

print('---------')
# l1.delete_at_beg()
# l1.delete_at_beg()
# l1.delete_at_beg()
# l1.delete_at_beg()
# l1.delete_at_end()
# l1.delete_at(3)
l1.insert_after_value( 40, 55 )
l1.print()