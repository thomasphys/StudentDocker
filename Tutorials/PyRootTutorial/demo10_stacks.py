# python3 -i demo10_stacks.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file")

c1 = ROOT.TCanvas()
tree.Draw("gaussian >> h1")
h1 = ROOT.gROOT.FindObject("h1")
tree.Draw("gaussian/(1.0*binomial) >> h2")
h2 = ROOT.gROOT.FindObject("h2")
h2.SetLineColor(ROOT.kRed)

hs = ROOT.THStack("hs","THStack")
hs.Add(h1)
hs.Add(h2)
hs.Draw("NOSTACK") # Default draw stacks 'em vertically, so we need NOSTACK.

# 2D coordinates go X1,Y1,X2,Y2, (0,0) is at bottom left, (1,1) is at top right.
# NDC means Normalized Device Coordinates
tl = ROOT.TLegend(0.6,0.6,0.9,0.9,"Header Text","NDC")
tl.AddEntry(h1,"Gaussian")
tl.AddEntry(h2,"Gaus/Binom")
tl.Draw()

# Reference:
# https://root.cern.ch/doc/master/classTHStack.html
# https://root.cern.ch/doc/master/classTLegend.html