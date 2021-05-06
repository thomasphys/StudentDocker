import ROOT, array, csv # python3 demo6_ttree_manual.py

infilename  = "demo_data_file.csv"
outfilename = infilename.replace(".csv",".root")
treename    = infilename.replace(".csv","")
outfile = ROOT.TFile(outfilename,"RECREATE") # Erases any existing file.

# Create a one-element python array to hold the value (could also use numpy).
time_arr     = array.array("d",[0])
binomial_arr = array.array("l",[0]) # And so on for every variable...

# Create the tree and the branch manually. 
t = ROOT.TTree(treename,"tree title")
t.Branch("time",     time_arr,     "time/D")     # D for doubles
t.Branch("binomial", binomial_arr, "binomial/L") # L for integers

# Now loop over the file manually:
with open(infilename,"r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0].startswith("#"): # skip comment lines
            continue
        time_arr[0]     = float(row[0]) # Important: change the CONTENT of the arrays.
        binomial_arr[0] = int(row[1])
        t.Fill()

# Write the data from the TFile to the actual file on disk.
outfile.Write()
outfile.Close()

# Reference: https://root.cern.ch/doc/master/classTTree.html (Ctrl+F for PyROOT)
#            https://docs.python.org/3/library/array.html