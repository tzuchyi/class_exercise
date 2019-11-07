import math
class Solution(object):
    def comparetwolist(self,a,b):#先製作一個比較兩數列的工具
        c=[]
        while len(a)*len(b)!=0:#當兩數列長度相乘不為零，代表裡面都還有元素存在
            if a[0]>=b[0]:#如果a的第一個數比較大，就把他加到新的c
                c.append(a[0])
                a.pop(0)#再把它拿掉
            else:
                c.append(b[0])#這個是如果b第一個數比較大的情況
                b.pop(0)
        if len(a)==0:#當a長度為零，直接把剩下的b接進c
            c=c+b
        else:
            c=c+a
        return c#最後回傳c
    def merge_sort(self,arr):
        for k in range(1,math.ceil(math.log(len(arr),2))+1):

            j=2**k
            final=[]
            n=len(arr)
            if len(arr)%j==0:
                for i in range(n//j):      
                    final=final+self.comparetwolist(arr[j*i:j*i+j//2],arr[j*i+j//2:j*i+j])
                arr=final
            else:

                for i in range(n//j):
                    final=final+self.comparetwolist(arr[j*i:j*i+j//2],arr[j*i+j//2:j*i+j])
                lost=(n//j)*j
                final=final+self.comparetwolist(arr[(n//j)*j:(n//j)*j+j//2],arr[(n//j)*j+j//2:])
                arr=final
        return arr