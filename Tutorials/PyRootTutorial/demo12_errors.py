# python3 -i demo12_errors.py
import ROOT, array

x = array.array("d",range(10))
y = array.array("d",[xi**2 for xi in x])
x_errors = ROOT.nullptr # Use ROOT.nullptr where you'd otherwise send 0 or NULL.

y_errors = array.array("d",[0]*len(y))
for i,yi in enumerate(y):
    y_errors[i] = ROOT.TMath.Sqrt(yi)

g = ROOT.TGraphErrors(len(x), x, y, x_errors, y_errors)
g.Draw("AP")

# Reference: https://root.cern.ch/doc/master/classTGraphErrors.html
#            https://root.cern.ch/doc/master/classTGraphAsymmErrors.html