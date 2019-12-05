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
                
                
#參考資料
#### 原理及概念上理解：
#https://zh.wikipedia.org/wiki/散列函數  
#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html  
#https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/   
#https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p
                        
                    
                
