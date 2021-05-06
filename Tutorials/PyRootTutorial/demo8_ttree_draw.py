# python3 -i demo8_ttree_draw.py
import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")
tree = infile.Get("demo_data_file")

tree.Draw("binomial") # ROOT has an algorithm to guess decent histogram boundaries.
htemp = ROOT.gROOT.FindObject("htemp") # Temporary histograms are called "htemp"
# NOTE: a failed FindObject returns <cppyy.gbl.TObject object at 0x(nil)>
h1 = htemp.Clone("h1") # Clone to make sure it doesn't get deleted.
input("Press Enter to continue.")

# You can give your histogram an explicit name and binning:
tree.Draw("binomial >> h2(10,0,15)")
h2 = ROOT.gROOT.FindObject("h2")  # Bring "h2" over to the python side.
input("Press Enter to continue.") # NOTE: click on the canvas to force an update.

tree.Draw("gaussian:time") # Unbinned 2D scatter plot TGraphs are made with y:x
g1 = ROOT.gROOT.FindObject("Graph").Clone("g1") # Temporary is called "Graph"
# NOTE: if you use the >>name notation, it instead makes a BINNED TH2*!
g1.Draw("AP")       # Remember to draw the clone before working on it further.
g1.SetTitle("Noise")

# References:
# https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45