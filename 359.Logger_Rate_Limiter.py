class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.ok = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp < self.ok.get(message,0):
            return False
        self.ok[message] = timestamp + 10
        return True
