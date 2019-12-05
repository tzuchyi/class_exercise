from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
      
    
    
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    
    
    
    def add(self, key):
        
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity
        for i in range(self.capacity):
            if index==i:
                head=self.data[i]
                if self.data[i]==None:
                    
                    self.data[i]=ListNode(key)
                else:
                    while head.next!=None:
                        head=head.next
                    head.next.val=key
                    
                


        
        
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity
        for i in range(self.capacity):
            if index==i:
                head=self.data[i]
                
                while head!=None:
                    if head.val==key and head.next==None:
                        self.data[i]=None
                        head=self.data[i]
                    elif head.val==key and head.next!=None:
                        self.data[i]=head.next
                        head=self.data[i]
                    else:
                        while head.val!=key and head.next!=None:
                            dad=head
                            head=head.next
                        if head.val==key:
                            if head.next==None:
                                dad.next=None
                                head=None
                            else:
                                dad.next=head.next
                                head=dad
                        else:
                            head=None
                        
                        
                    
        
    def contains(self, key):
        
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity
        for i in range(self.capacity):
            if index==i:
                head=self.data[i]
                if self.data[i]==None:
                    return False
                else:
                    while head.val!=key and head.next!=None:
                        head=head.next
                    if head.val==key:
                        return True
                    else:
                        return False
                        
                    
                
