class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution(object):


    def insert(self, root, val):
   
        temp=root
        while temp!=None:
            
            if temp.val>= val:
                temp_dad=temp
                temp=temp.left
            else :
                temp_dad=temp
                temp=temp.right
                
        temp=TreeNode(val)
        if temp_dad.val>=val:
            temp_dad.left=temp
        else:
            temp_dad.right=temp
        return temp
 
        
    def delete(self, root, target):
        
        temp=root
        temp_dad=None
        
        
        while temp!=None:
            
            if temp.val>target:
                temp_dad=temp
                temp=temp.left

            elif temp.val<target:
                temp_dad=temp
                temp=temp.right                                
            
            elif temp.val==target:
                if temp_dad is None:
                    if temp.left==None:
                        root=temp.right
                        temp=root
                    elif temp.right==None:
                        root=temp.left
                        temp=root
                    else :
                        
                        left_max=temp.left
                        left_max_dad=temp
                        while left_max.right!=None:
                            left_max_dad=left_max
                            left_max=left_max.right
                        if left_max.left==None:
                            left_max_dad.right=None
                        else:
                            left_max_dad.right=left_max.left
                            
                   
                        left_max.left=temp.left
                        left_max.right=temp.right
                        root=left_max
                        temp=root

                  
                    
                else:
                    if temp.left==None and temp.right==None:
                        temp_dad.left=None
                        temp=None
                    elif temp.left==None:
                        temp_dad.left=temp.right
                        temp=temp.right
                    elif temp.right==None:
                        temp_dad.left=temp.left
                        temp=temp.left
                    else:
                        
                        left_max=temp.left
                        left_max_dad=temp
                        while left_max.right!=None:
                            left_max_dad=left_max
                            left_max=left_max.right
                        if left_max.left==None:
                            left_max_dad.right=None
                        else:
                            left_max_dad.right=left_max.left
                            
                        #left_max_dad.right=None
                        left_max.left=temp.left
                        left_max.right=temp.right
                        
                        if temp_dad.val>target:
                            temp_dad.left=left_max
                        else:
                            temp_dad.right=left_max
                        temp=root
                        
                        
                       
                        
                        
            
                    
        return root
        

            
        
       
    def search(self, root, target):
        
        temp=root
        temp_dad=None
        
        
        while temp!=None:
            
            if temp.val>target:
                temp_dad=temp
                temp=temp.left

            elif temp.val<target:
                temp_dad=temp
                temp=temp.right                                
            
            else:
                return temp
        return None

        
        
    def modify(self, root, target, new_val):
        temp=root
        temp_dad=None
        k=0
        
        while temp!=None:
            
            if temp.val>target:
                temp_dad=temp
                temp=temp.left

            elif temp.val<target:
                temp_dad=temp
                temp=temp.right                                
            
            elif temp.val==target:
                if temp_dad is None:
                    if temp.left==None:
                        root=temp.right
                        temp=root
                    elif temp.right==None:
                        root=temp.left
                        temp=root
                    else :
                        
                        left_max=temp.left
                        left_max_dad=temp
                        while left_max.right!=None:
                            left_max_dad=left_max
                            left_max=left_max.right
                            
                        left_max_dad.right=None
                        left_max.left=temp.left
                        left_max.right=temp.right
                        root=left_max
                        temp=root
                            
                    
                else:
                    if temp.left==None and temp.right==None:
                        temp_dad.left=None
                        temp=None
                    elif temp.left==None:
                        temp_dad.left=temp.right
                        temp=temp.right
                    elif temp.right==None:
                        temp_dad.left=temp.left
                        temp=temp.left
                    else:
                        
                        left_max=temp.left
                        left_max_dad=temp
                        while left_max.right!=None:
                            left_max_dad=left_max
                            left_max=left_max.right
                            
                        left_max_dad.right=None
                        left_max.left=temp.left
                        left_max.right=temp.right
                        
                        if temp_dad.val>target:
                            temp_dad.left=left_max
                        else:
                            temp_dad.right=left_max
                        temp=root                        
                  
                k=k+1
        while k>0:
            self.insert(root,new_val)
            k=k-1
        return root
        
        

