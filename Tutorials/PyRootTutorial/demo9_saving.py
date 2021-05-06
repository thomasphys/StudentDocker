# python3 -i demo9_saving.py
import ROOT

infilename = "demo_data_file.root"
infile = ROOT.TFile(infilename,"READ")
treename = infilename.replace(".root","")
tree = infile.Get(treename)

# Create a TCanvas.  New canvases are automatically set to the active one.
c1 = ROOT.TCanvas("c1")

# Draw your thing.
tree.Draw("gaussian:time") 
c1.SaveAs("plots/demo9_binomial.png") # png makes lightweight figures, but scale badly.
c1.SaveAs("plots/demo9_binomial.pdf") # scales well, but can be huge with lots of points.
c1.SaveAs("plots/demo9_binomial.tex") # Figure for inclusion in a LaTeX document.
c1.SaveAs("plots/demo9_binomial.C")   # Useful format to re-load into ROOT later.

