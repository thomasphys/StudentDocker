# python3 -i demo3_numpy_loadtxt.py
import numpy

infilename = "demo_data_file.csv"
data = numpy.loadtxt(infilename, delimiter = ",", unpack=True)

# data[0] is the time, data[1] the binomial, data[2] the gaussian

# Reference: 
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html