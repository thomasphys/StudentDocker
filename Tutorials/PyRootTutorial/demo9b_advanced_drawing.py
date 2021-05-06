# python3 -i demo9b_advanced_drawing.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file")

tree.GetEntry(0)
t0 = tree.time  # Get t0 so we can plot with relative time.
drawstring = "TMath::Power(time/(1.0*Entry$)-500,2):((time-%g)/1e3)" % t0
tree.Draw(drawstring)

g1 = ROOT.gROOT.FindObject("Graph").Clone("g1")
g1.Draw("ALP")
g1.GetXaxis().SetRangeUser(0,1000) # "User" coordinates means in the graph units.
g1.SetMaximum(2500) # Setting the range in Y is different than in X.
g1.SetMinimum(0)

# Arbitrary C++-style expressions are allowed with the names in the TTree.
# The C++ ternary operator (A ? B : C) is available, so you can do anything!
# Special names are also available: Entry$, Entries$, Sum$, etc.
# Also functions from ROOT.TMath:: and the C++ std::cmath modules. NOTE: "::"
# Reference: https://root.cern.ch/doc/master/classTFormula.html
#            https://root.cern.ch/doc/master/namespaceTMath.html
#            https://www.cplusplus.com/reference/cmath/
# https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45
# https://root.cern.ch/root/htmldoc/guides/users-guide/ROOTUsersGuide.html Sec. 9.3.3