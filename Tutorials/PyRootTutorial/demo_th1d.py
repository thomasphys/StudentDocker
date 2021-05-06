# python3 -i demo_th1d.py
import ROOT

rng = ROOT.TRandom3(1234) # Random number generator object
# Parameters are: Number of bins, lowest edge, highest edge
h = ROOT.TH1D("h","Histogram Title", 10, 0, 10) 
for i in range(500):
    value = rng.Gaus(5,1)
    h.Fill(value)
h.Draw()
# https://root.cern.ch/doc/master/classTH1.html       TH1* Documentation
# https://root.cern/doc/master/classTHistPainter.html TH1* Draw Options
# https://root.cern.ch/doc/master/classTRandom3.html  TRandom3 Documentation