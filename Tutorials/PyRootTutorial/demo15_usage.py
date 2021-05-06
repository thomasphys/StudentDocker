# python -i demo15_usage.py
import ROOT

ROOT.gROOT.ProcessLine(".L demo15_cpp_extension.C+") # Normal ROOT command.

def py_power(x, a):
    result = 1
    for i in range(a):
        result *= x
    return result

x, a = 23.48, 21
value_ext = ROOT.ext_power(x, a)
value_py  = py_power(x, a)
