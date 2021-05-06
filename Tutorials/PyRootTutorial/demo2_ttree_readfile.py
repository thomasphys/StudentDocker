# python3 demo2_ttree_readfile.py
import ROOT

infilename  = "demo_data_file.csv"
outfilename = infilename.replace(".csv",".root")
treename    = infilename.replace(".csv","") # Give the tree the same name as the file.

# Create the ROOT TFile.
outfile = ROOT.TFile(outfilename,"RECREATE") # Erases any existing file.

# Create the tree. New TTrees are automatically added to the current TFile, if any.
t = ROOT.TTree(treename,treename)
# Define branches of a TTree
# The syntax is branchname/typecode:branchname/typecode...
branches = "time/D:binomial/L:gaussian/D" # L for integers, D for floats

t.ReadFile(infilename,branches)

# Write the data from the TFile to the actual file on disk.
outfile.Write()
outfile.Close()
# References:
# https://root.cern.ch/doc/master/classTFile.html
# https://root.cern.ch/doc/master/classTTree.html#a9c8da1fbc68221b31c21e55bddf72ce7
