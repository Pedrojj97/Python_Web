class Solution:
    def isHappy(self, n: int) -> bool:
        n_temp = n
        a_list = []# 保存每次展开的数字平方和
        sqrt_add = 0

        while sqrt_add % 100 != 0 or sqrt_add == 0:
            n_str = str(n_temp)
            n_list = list(n_str)
            if n_temp in a_list:
                return False
            a_list.append(n_temp)
            for i in range(len(n_list)):
                sqrt_add += int(n_list[i])**2
            n_temp = sqrt_add
        return True


if __name__ == '__main__':
    s = Solution()
    s.isHappy(2)