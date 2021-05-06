import ROOT

infile = ROOT.TFile("demo_data_file.root","READ")

# Check the contents of the file
infile.ls()

# Get the tree out of the file
tree = infile.Get("demo_data_file")
# NOTE: a failed "Get" returns <cppyy.gbl.TObject object at 0x(nil)>

# Show the contents of the 0th entry and number of entries
tree.Show(0)
N = tree.GetEntries()
print(N)

# Shows a summary of the contents of the whole tree.
tree.Print()

# You can also get the list of branches programmatically:
for b in tree.GetListOfBranches():
    print("branch:",b.GetName())

# Once "got", each branch can be accessed as a data member of the tree.
for i in range(5):
    tree.GetEntry(i)
    print(tree.time,tree.gaussian)