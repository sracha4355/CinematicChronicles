from collections import deque
class plotPoints:
    def __init__(self, capacity=3):
        self.plotPoints = deque()
        self.capacity = capacity

    def addPlotPoint(self, plotPoint):
        if len(self.plotPoints) == self.capacity:
            self.plotPoints.popleft()
            self.plotPoints.append(plotPoint) 
            return

        self.plotPoints.append(plotPoint)
        
    def printPlotPoints(self):
        print('the current plots')
        print(list(self.plotPoints))
        return 
        for idx, point in enumerate(self.plotPoints()):
            print(idx + 1, ':', point)
        print('')
     
         

