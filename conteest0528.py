# -*- coding: utf-8 -*-
# @Time : 2022/5/28 22:44
# @Author : minghe_liu
# @File : conteest0528
from collections import defaultdict

a = ["tP x M VC h lmD", "D X XF w V", "sh m Pgl", "pN pa", "C SL m G Pn v", "K z UL B W ee",
     "Yf yo n V U Za f np",
     "j J sk f qr e v t",
     "L Q cJ c J Z jp E", "Be a aO", "nI c Gb k Y C QS N", "Yi Bts",
     "gp No g s VR",
     "py A S sNf",
     "ZS H Bi De dj dsh",
     "ep MA KI Q Ou"]
b = ["OXlq", "IFGaW", "XQPeWJRszU", "Gb", "HArIr", "Gb", "FnZd", "FnZd", "HArIr", "OXlq", "IFGaW", "XQPeWJRszU",
     "EMoUs", "Gb", "EMoUs", "EMoUs"]


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        ans = defaultdict(set)
        for m, s in zip(messages, senders):
            print(s, ':', m)
            words = m.split()
            for word in words:
                ans[s].add(word)

        a = max(map(lambda x: len(x), ans.values()))
        ret = []
        for k, v in ans.items():
            if len(v) == a:
                ret.append(k)
        ret.sort()

        print(ans)
        print(ret, a)
        return ret[-1]


if __name__ == "__main__":
    Solution().largestWordCount(a, b)
