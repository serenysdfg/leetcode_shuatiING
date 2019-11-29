#好题
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # copy2
        order = {c: i for i, c in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):  # 利用zip
            for a, b in zip(word1, word2):
                if a != b:
                    if order[a] > order[b]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
        # copy1
        # return words == sorted(words, key=lambda x: list(map(order.index, x))) #根据order排序后是不是相同 
        # 比用内置的index块
        # copy4
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))  # 列表比较1.2.3.4
        # copy5

    words_dict = {c: i for i, c in enumerate(order)}

    def helper(x, y):
        nonlocal words_dict
        x_len, y_len = len(x), len(y)
        i, j = 0, 0
        while i < x_len and j < y_len:
            if x[i] == y[j]:
                i += 1
                j += 1
                continue
            if words_dict[x[i]] < words_dict[y[j]]:
                return -1
            if words_dict[x[i]] > words_dict[y[j]]:
                return 1
        if i == x_len and j == y_len:
            return 0
        if i < x_len:
            return 1
        if j < y_len:
            return -1

    return words == sorted(words, key=cmp_to_key(lambda x, y: helper(x, y)))
