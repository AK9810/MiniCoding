# 戚梓鹏
# 2021.1.23
# MiniCoding.py
class Solution(object):
    def letters(self, digits):
        # 创建字母对应的字符列表的字典
        dic = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z'],
               }
        # 存储结果的数组
        ret = []
        if len(digits) == 0: return []
        # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
        if len(digits) == 1:
            return dic[int(digits[0])]
        # 递归调用
        result = self.letters(digits[:-1])
        # result是一个数组列表，遍历后字符串操作，加入列表
        for r in result:
            for j in dic[int(digits[-1])]:
                ret.append(r + j)

        output = ''
        for o in ret:
            output = output + str(o)+' '
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.letters([2,3]))
    print(s.letters([9]))
