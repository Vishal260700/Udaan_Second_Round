

# input is source destination and date

class Bus:
    def __init__(self, object):
        self.companyName = object['companyName']
        self.busNumber = object['busNumber']
        self.start = None
        self.destination = None
        self.startTime = None
        self.endTime = None
        self.freq = None
        self.capacity = 0
    
    def checkAvailability(self, )