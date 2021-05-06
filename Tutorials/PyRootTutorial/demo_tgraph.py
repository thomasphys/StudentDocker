# python3 -i demo_tgraph.py
import ROOT, array

x = array.array("d",range(10)) # "d" for double-precision floating-point.
y = array.array("d",[0]*len(x))# array of ten zeros.

for i,xi in enumerate(x):
    y[i] = xi**2

g = ROOT.TGraph(len(x),x,y)
g.Draw("AL")

# https://docs.python.org/3/library/array.html            Python array module
# https://root.cern.ch/doc/master/classTGraph.html        TGraph Documentation
# https://root.cern.ch/doc/master/classTGraphPainter.html TGraph Draw Options
# https://root.cern.ch/doc/master/classTMath.html         TMath Documentation