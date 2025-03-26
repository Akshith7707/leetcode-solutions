class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = []
        stri = ""
        for i in range(len(s)):
            if s[i] == " ":
                arr.append(stri)
                stri = ""
            else:
                stri += s[i]
        arr.append(stri)

        arr1 = []
        for i in arr:
            if i != "":
                arr1.append(i)

        return len(arr1[-1])