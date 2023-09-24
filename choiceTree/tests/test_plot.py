import sys
sys.path.append('..')
from plot import *

class plotTester():
    def testPlots(self):
        self.short_sentences = [
            "The sun is shining.",
            "I love ice cream.",
            "Dogs are loyal pets.",
            "Coding is fun.",
            "The sky is blue.",
            "Birds sing in the morning.",
            "Flowers bloom in spring.",
            "Reading books is relaxing.",
            "Coffee smells great.",
            "Music soothes the soul."
        ]


    def test_plots(self):
        self.testPlots()
        plot = plotPoints(3)
        plot.addPlotPoint(self.short_sentences[0])
        assert (len(plot.plotPoints) == 1)
        plot.addPlotPoint(self.short_sentences[1])
        assert (len(plot.plotPoints) == 2)
        plot.addPlotPoint(self.short_sentences[2])
        assert (len(plot.plotPoints) == 3)
        
        for idx in range(3, len(self.short_sentences)):
            plot.addPlotPoint(self.short_sentences[idx])
            assert (len(plot.plotPoints) == 3)
        
        print('assertions passed')
plotTester().test_plots()
