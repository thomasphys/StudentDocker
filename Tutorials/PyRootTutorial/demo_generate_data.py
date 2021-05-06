# python3 demo_generate_data.py
import ROOT, csv

outfilename = "demo_data_file.csv"
n_lines = 10000
random_seed = 1337               # Fixed seed for reproducibility
rng = ROOT.TRandom3(random_seed) # Random number generator object
t, tau = 0, 500 # Average time interval for simulated Poisson process.

outfile = open(outfilename,"w") # "write" mode.
outfile.write("# Generated using ROOT.TRandom3 with seed %d\r\n" % random_seed)
outfile.write("# tau = %d\r\n" % tau)
outfile.write("# time, binomial, gaussian\r\n")
writer = csv.writer(outfile)

for i in range(n_lines):
    t   += rng.Exp(tau)           # Exponential distribution with tau
    var2 = rng.Binomial(20,0.2) # 20 trials, 0.2 chance of success
    var3 = rng.Gaus(0,1)        # central value 0, width 1
    writer.writerow([t,var2,var3])
outfile.close()

# References
# https://root.cern.ch/doc/master/classTRandom3.html
# https://docs.python.org/3/library/csv.html