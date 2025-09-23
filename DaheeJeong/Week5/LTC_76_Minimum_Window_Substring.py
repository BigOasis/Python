from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        t_dic = defaultdict(int)
        for ch in t:
            t_dic[ch] += 1

        s_dic = defaultdict(int)

        have, need = 0, len(t_dic)

        res = ""
        res_len = float("inf")

        start, s_length = 0, len(s)

        for end in range(s_length):
            c = s[end]
            s_dic[c] += 1

            if c in t_dic and s_dic[c] == t_dic[c]:
                have += 1

            # 모든 문자 조건을 충족했으면 줄이기 시작
            while have == need:
                window_size = end - start + 1
                if window_size < res_len:
                    res_len = window_size
                    res = s[start:end+1]

                # 왼쪽 문자 빼고 윈도우 줄이기
                left_c = s[start]
                s_dic[left_c] -= 1
                if left_c in t_dic and s_dic[left_c] < t_dic[left_c]:
                    have -= 1
                start += 1

        return res
