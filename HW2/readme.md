## 學習歷程：
> [mergesort學習歷程](https://nbviewer.jupyter.org/github/tzuchyi/class_exercise/blob/master/HW2/mergesort_製作歷程.ipynb)  
> [heapsort學習歷程](https://nbviewer.jupyter.org/github/tzuchyi/class_exercise/blob/master/HW2/heapsort_製作歷程.ipynb)  

## merge與heap的排序比較
> merge與heap平均、最快、最慢花費時間皆相同，皆為O(nlogn)    
> 但在空間上heap所佔的空間會較merge少，因為heap是直接在原本的序列上做更改，並沒有增加新的序列。merge為O(n)、heap為O(1)。  
> 這個部分因為只聽老師上課講解，誤以為拿掉底部的數是指會生成新的序列，故我製作的heapsort空間複雜度和mergesort相同，接生成了新的序列。  

## 參考資料：  
> merge_sort演算法了解 https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_17    
>> 做比較時查找merge資料 https://kopu.chat/2017/08/10/合併排序-merge-sort/  
  
> heap_sort演算法了解 https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_17  
>> 做比較時查找heap資料 http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php  
  
>> 基本上我這兩個演算法都只有依照老師上課講解其進行方式，將步驟轉換成程式碼，因此沒有特別的參考資料。  
  
> 如何取log https://blog.csdn.net/robertsong2004/article/details/46651503  
> 如何取整數 http://kuanghy.github.io/2016/09/07/python-trunc
