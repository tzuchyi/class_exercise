class Solution:
    def str2num(self, num):
        int_num = 0
        pos = 1
        for n in num[::-1]:
            int_num += (ord(n) -  48) * pos
            pos = pos * 10
        print(int_num)
        return int_num

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = self.str2num(num1)
        n2 = self.str2num(num2)
        return repr(n1 * n2)
