import pysam

infile = pysam.AlignmentFile("-", "rb")
outfile = pysam.AlignmentFile("-", "w", template=infile)
for s in infile:
    outfile.write(s)