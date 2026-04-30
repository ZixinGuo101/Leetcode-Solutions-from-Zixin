class FreqStack(object):

    def __init__(self):
        self.val_to_freq = dict()
        self.freq_to_val = dict()
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.val_to_freq:
            self.val_to_freq[val] = 1
        else:
            self.val_to_freq[val] += 1
        f = self.val_to_freq[val]

        self.max_freq = f if self.max_freq < f else self.max_freq

        if f not in self.freq_to_val:
            self.freq_to_val[f] = []
        self.freq_to_val[f].append(val)
        # print("push")
        # print(self.freq_to_val[self.max_freq])

    def pop(self):
        """
        :rtype: int
        """
        
        mq = self.freq_to_val[self.max_freq]
        num = mq.pop()
        self.val_to_freq[num] -= 1
        if self.val_to_freq[num] == 0:
            del self.val_to_freq[num]

        if len(mq) == 0:
            del self.freq_to_val[self.max_freq]
            self.max_freq -= 1
        # print(self.val_to_freq)
        # print(self.freq_to_val[self.max_freq])
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()