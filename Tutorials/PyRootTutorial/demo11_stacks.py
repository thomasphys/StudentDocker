# python3 -i demo11_stacks.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file") 

c1 = ROOT.TCanvas()
tree.Draw("gaussian:time")
g1 = ROOT.gROOT.FindObject("Graph").Clone("g1")
tree.Draw("gaussian/binomial:time")
g2 = ROOT.gROOT.FindObject("Graph").Clone("g2")
g2.SetLineColor(ROOT.kRed)

mg = ROOT.TMultiGraph("mg","TMultiGraph")
mg.Add(g1)
mg.Add(g2)
mg.Draw("AL") # Don't need NOSTACK for TMultiGraph (blame ROOT)

# 2D coordinates go X1,Y1,X2,Y2, (0,0) is at bottom left, (1,1) is at top right.
tl = ROOT.TLegend(0.6,0.1,0.9,0.3,"","NDC")
tl.AddEntry(g1,"Gaussian")
tl.AddEntry(g2,"Gaus/Binom")
tl.Draw()

# Reference:
# https://root.cern.ch/doc/master/classTMultiGraph.html
# https://root.cern.ch/doc/master/classTLegend.html