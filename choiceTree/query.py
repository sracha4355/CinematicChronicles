from plot import *

class QueryBuilder():
    def __init__(self, choices):
        self.start = ["Here is what happened"]
        self.points = plotPoints(choices)
        self.choices = choices

    def query(self):
        query = ["Here is what happened"]
        for idx in range(len(self.points)):
            query.append(self.points[idx])
        query.append(f"Generate {self.choices} choices for happens next in a numbered list format")
        
        return "\n".join(query)
    
    def extractChoices(self, prompts):
        prompts = prompts.split('\n')
        ans = []
        for prompt in prompts:
            if prompt == "":
                continue
            idx = 0
            while "." != prompt[idx]:
                idx += 1
            idx += 1
            ans.append(prompt[idx + 1::])

        return ans

    def addChosenChoice(self,prompts, choice):
        self.points.addPlotPoint(prompts[choice])

    




