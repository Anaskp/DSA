class Node:
    def __init__( self, data=None, next=None ):
        self.data = data
        self.next = next

class Linked_List:
    
    def __init__( self ):
        self.head = None

    def print( self ):

        if self.head is None:
            print( 'Empty' )
            return
        
        itr = self.head
        while( itr ):
            print( itr.data )
            itr = itr.next

    def insert_values( self, data_list ):
        self.head = None

        for data in data_list:
            self.insert_at_end( data )

    def get_length( self ):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beg( self, data ):
        node = Node( data, self.head )
        self.head = node

    def insert_at_end( self, data ):
        if self.head is None:
            self.head = Node( data, None )
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node( data, None )

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
                node = Node( data, itr.next )
                itr.next = node
                break
            count += 1
            itr = itr.next

    def delete_at_beg( self ):

        if self.head is None:
            print( 'Empty' )
            return
        
        self.head = self.head.next

    def delete_at_end( self ):
        if self.head is None:
            print( 'Empty' )
            return
        
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def delete_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr :
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_after_value( self, data_after, data ):
        if self.head is None:
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node( data, itr.next )
                break
            itr = itr.next
        
        if itr is None:
            raise Exception( 'No data found' )
        
    def remove_by_value( self, data ):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        
        if itr.next is None:
            raise Exception( 'No data found' )
        


l1 = Linked_List()
l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_beg(30)
l1.insert_at_beg(40)
# l1.insert_at_end(50)
# values = [ 'apple', 'orange', 'banana', 'strawberry' ]
# l1.insert_values(values)
# print( l1.get_length() )
l1.print()
# l1.delete_at_beg()
#l1.delete_at_end()
print('-----')
# l1.delete_at(2)
# l1.insert_at(55, 5)
l1.insert_after_value(10,60)
# l1.remove_by_value(20)
l1.print()
