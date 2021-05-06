# python3 -i demo4_python_file.py
infilename = "demo_data_file.csv"
with open(infilename,"r") as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        data = line.split(",")
        time, binomial, gaussian = float(data[0]), data(row[1]), data(row[2])
# Reference:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files