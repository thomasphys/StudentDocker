# python3 -i demo14_fit2.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file")

c1 = ROOT.TCanvas()
# The first empty "" is a TCut string the second is a draw option. 
tree.Draw("sin(time/1000.0):time/1000.0","","",100,0) # Draw 100 entries starting at 0.
g1 = ROOT.gROOT.FindObject("Graph").Clone("g1")
g1.Draw("ALP")
input("Press Enter to continue.") # Pause

f1 = ROOT.TF1("f1","[0]*sin(x/[1] + [2]) + [3]",0,50) # Generic sine function.
f1.SetParNames("scale","period","phase","offset") # Optional.
f1.SetParameters(1,1,0,0) # Set initial parameter guesses/
f1.SetNpx(600) # Increase the number of points in X.
# f1.Draw("same") # To see if our initial guess is close.
ftr_p = g1.Fit(f1,"S")
ROOT.gPad.Modified(); ROOT.gPad.Update() # This magic forces a canvas refresh.

# Reference: 
# https://root.cern.ch/doc/master/classTF1.html
# https://root.cern.ch/doc/master/classTGraph.html#a61269bcd47a57296f0f1d57ceff8feeb
# https://root.cern.ch/doc/master/classTGraph.html#aa978c8ee0162e661eae795f6f3a35589