class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #     #copy回溯法
        #     res = []
        #     self.dfs(s, [], res)
        #     return res

        # def dfs(self, s, path, res): #path用来获取4段
        #     if len(s) > (4 - len(path)) * 3:
        #         return
        #     if not s and len(path) == 4:
        #         res.append('.'.join(path))
        #         return
        #     for i in range(min(3, len(s))):#主要
        #         curr = s[:i+1] #1个或者两个或者三个
        #         if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255: #01 02 012
        #             continue
        #         self.dfs(s[i+1:], path + [s[:i+1]], res)
        result = list()
        if not s or 4 > len(s) or len(s) > 12:
            return result

        self._restoreIpAddresses(s, 4, 0, "", result)
        return result

    def _restoreIpAddresses(self, s, n, index, ip, result):
        if n == 0:
            if index == len(s):
                result.append(ip)
            return

        def isNum(num):
            if 0 <= int(num) <= 255 and str(int(num)) == num:
                return True
            return False

        for i in range(index + 1, len(s) + 1):
            if isNum(s[index:i]):
                self._restoreIpAddresses(s, n - 1, i, s[index:i] if ip == "" else ip + '.' + s[index:i], result)
            else:
                break


