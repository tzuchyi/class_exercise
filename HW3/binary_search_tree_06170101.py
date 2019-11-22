class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution(object):

    def inorder(self, root):
        if root is None: 
            return     
        else:
            self.inorder(root.left) 
            print(root.val)
            self.inorder(root.right)
#    def insert_dad(self, root, val):
#   
#        temp=root
#        while temp!=None:
#            
#            if temp.val>= val:
#                temp_dad=temp
#                temp=temp.left
#            else :
#                temp_dad=temp
#                temp=temp.right
#
#        temp=TreeNode(val)
#        if temp_dad.val>=val:
#            temp_dad.left=temp
#        else:
#            temp_dad.right=temp
#        return temp_dad

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
                    else:
                #    elif temp.right!=None and temp.left!=None :
                        if temp.left.right==None:                            
                            
                            temp.left.right=temp.right
                            root=temp.left
                            temp=root
                            
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

                        #    left_max_dad.right=None
                            left_max.left=temp.left
                            left_max.right=temp.right
                            root=left_max
                            temp=root

                     #   root=temp.left
                        
                      #  dad=self.insert_dad(root, temp.right.val)
                      #  dad.left=temp.left
                      #  dad.right=temp.right
                     #   temp=root
                    
                    
                else:
                    if temp_dad.val>target:
                        
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
                            if temp.left.right==None:
                                temp_dad.left=temp.left
                                temp_dad.left.right=temp.right
                                temp=root
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
                    else:
                        if temp.left==None and temp.right==None:
                            temp_dad.right=None
                            temp=None
                        elif temp.left==None:
                            temp_dad.right=temp.right
                            temp=temp.right
                        elif temp.right==None:
                            temp_dad.right=temp.left
                            temp=temp.left
                        else:
                            if temp.left.right==None:
                                temp_dad.right=temp.left
                                temp_dad.right.right=temp.right
                                temp=root
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
        
    #    temp=root.left
        
        
     #   while temp!=None:
      #      temp_dad=root
       #     if temp.val==target:
         #       if temp.left==None & temp.right==None:
           #         temp_dad.left=None
             #   elif temp.left==None:
               #     temp_dad.left=temp.right
         #       elif temp.right==None:
           #         temp_dad.left=temp.left
             #   else:
             #       temp_dad.left=temp.left
             #       temp_dad.left.right=temp.right
           # temp=temp.left
            
            
            
        
       
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
        k=0
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
                k=k+1
                
                if temp_dad is None:
                    if temp.left==None:
                        root=temp.right
                        temp=root
                    elif temp.right==None:
                        root=temp.left
                        temp=root
                    else:
                #    elif temp.right!=None and temp.left!=None :
                        if temp.left.right==None:                            
                            
                            temp.left.right=temp.right
                            root=temp.left
                            temp=root
                            
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

                        #    left_max_dad.right=None
                            left_max.left=temp.left
                            left_max.right=temp.right
                            root=left_max
                            temp=root

                     #   root=temp.left
                        
                      #  dad=self.insert_dad(root, temp.right.val)
                      #  dad.left=temp.left
                      #  dad.right=temp.right
                     #   temp=root
                    
                    
                else:
                    if temp_dad.val>target:
                        
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
                            if temp.left.right==None:
                                temp_dad.left=temp.left
                                temp_dad.left.right=temp.right
                                temp=root
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
                    else:
                        if temp.left==None and temp.right==None:
                            temp_dad.right=None
                            temp=None
                        elif temp.left==None:
                            temp_dad.right=temp.right
                            temp=temp.right
                        elif temp.right==None:
                            temp_dad.right=temp.left
                            temp=temp.left
                        else:
                            if temp.left.right==None:
                                temp_dad.right=temp.left
                                temp_dad.right.right=temp.right
                                temp=root
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
                  
                
        while k>0:
            self.insert(root,new_val)
            k=k-1
        return root
        
        



        
    
#參考資料：
#這邊是我對於ＢＳＴ認識的資料來源

#10/28-11/3 Binary Tree上課講義：
#https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.p
#11/11-11/17 Binary Search Tree上課講義：
#https://docs.google.com/presentation/d/e/2PACX-1vSC3P8sGElP48mJTjqT309470SmTFBwJXWsU9hTX2hg5tVpiG4yC703qA7ibPep-Qakmm2Mw_F-ScZh/pub?start=false&loop=false&delayms=3000&slide=id.p

#程式碼的作法則是依照之前linked list的邏輯做出，
#沒有參考其他網路上現成的程式碼。
#針對刪除功能的邏輯有和簡大為做討論，
#故若刪除功能程式碼與簡大為相似，只因邏輯相同，絕無抄襲。
        
        

