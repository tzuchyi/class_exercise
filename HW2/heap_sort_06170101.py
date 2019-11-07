class Solution(object):
    def checkdad(self,arr,me):#接下來檢查爸爸
        if me !=0:#當我還不是第一個老大的時候我都還要繼續望上檢查爸爸
            dad=(me-1)//2
            if arr[me]>=arr[dad]:
                arr[me],arr[dad]=arr[dad],arr[me]
                me=dad#當我交換之後我就要換成爸爸繼續和我的爸爸檢查
                self.checkdad(arr,me)
    def checkson(self,arr,me):#那就來做一個工具 只和小孩比
        if me <=(len(arr))//2-1:
            left_son=2*me+1
            right_son=2*me+2
            if right_son<=len(arr)-1:#狀況又分成右小孩存在與右小孩不存在
                if arr[me]<=arr[left_son]:
                    arr[me],arr[left_son]=arr[left_son],arr[me]
                    if arr[me]<=arr[right_son]:
                        arr[me],arr[right_son]=arr[right_son],arr[me]
                    self.checkdad(arr,me)#當我出現交換位置 我就要回去和爸爸作比較 這是我等一下要寫的另一個工具
                elif arr[me]<=arr[right_son]:
                    arr[me],arr[right_son]=arr[right_son],arr[me]
                    self.checkdad(arr,me)
            else:#這邊就是右小孩不存在的狀況
                if arr[me]<=arr[left_son]:
                    arr[me],arr[left_son]=arr[left_son],arr[me]
                    self.checkdad(arr,me)
    def maxheap(self,arr):#現在就是把一個一個要檢查的人拿來檢查
        for i in range(len(arr)):
            self.checkson(arr,i)
    def heap_sort(self,arr):#最後一步
        final=[]#先設定我最後的解答
        while len(arr)!=0:#只要我的陣列還有東西就要繼續跑
            self.maxheap(arr)
            final.append(arr[0])#把最大的數加進去
            arr[0],arr[-1]=arr[-1],arr[0]#交換位置到最後一個
            arr.pop()#再拿掉最後一個數
        return final#就成功啦 萬歲
