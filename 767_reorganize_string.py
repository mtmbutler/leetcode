class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        self.S = S
        check_array = []
        for ch in self.S:
            if ch not in check_array:
                check_array.append(ch)

        for ch in check_array:
            count = 0
            for j in self.S:
                if j == ch:
                    count += 1
            if count > len(self.S)//2:
                return ''

        char_list = []
        for ch in self.S:
            char_list.append(ch)

        ret_str = ''
        outcasts = []
        for i in range(len(char_list)-1):
            if char_list[i] != char_list[i+1]:
                ret_str.append(char_list[i])
            else:
                outcasts.append(char_list[i])
        
        for letter in outcasts:
            for i in range(0,len(ret_str)-1):
                if ret_str[i] != letter and ret_str[i+1] != letter:
                    ret_str = ret_str[:i+1] + letter + ret_str[i+1:]
                    break



