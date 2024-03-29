class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if end <= start:
            return False
        
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:           
            return False
        
        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False
        
        self.intervals[i:i] = [start, end]
        
        return True