class FrequencyTracker:

    def __init__(self):
        # dictionary to save the freqency of each inputed data
        self.freq = defaultdict(int)
        # dictionary to save the freqency of the freqency or how many freqency of that sepcific freqency exist in the dictionary
        self.freq_of_freq = defaultdict(int)

    def add(self, number: int) -> None:
        #  when adding we reduce the freqency of the freqencies because we are adding new count of that value
        self.freq_of_freq[self.freq[number]] -= 1
        self.freq[number] += 1
        # and finally we need to increament the new freqency of the data 
        self.freq_of_freq[self.freq[number]] += 1

        

    def deleteOne(self, number: int) -> None:
        # if the frequency of the number is greater than 0 or there is a number do the following actions 
        if self.freq[number] >0:
            # we reduce the previous freqency count and inicreament the new frequncy count
            self.freq_of_freq[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.freq_of_freq[self.freq[number]] += 1

        

    def hasFrequency(self, frequency: int) -> bool:
        #  checkes if the frequency count is in the dictonary
        if frequency in self.freq_of_freq and self.freq_of_freq[frequency] > 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)