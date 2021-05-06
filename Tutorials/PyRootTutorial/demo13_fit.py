# python3 -i demo13_fit.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file")

tree.Draw("gaussian >> h1")
h1 = ROOT.gROOT.FindObject("h1")

ftr_p = h1.Fit("gaus","S") # gaus, expo, pol0, pol1...polN are shortcuts.
# Fit normally returns an empty TFitResultPtr, option "S" makes it Store the results.
ftr = ftr_p.Get() # You have to Get the TFitResult from the pointer.  It's dumb.

central_value = ftr.Parameter(1)
width = ftr.Parameter(2)

# Reference: 
# https://root.cern.ch/doc/master/classTF1.html
# https://root.cern.ch/doc/master/classTGraph.html#a61269bcd47a57296f0f1d57ceff8feeb
# https://root.cern.ch/doc/master/classTGraph.html#aa978c8ee0162e661eae795f6f3a35589