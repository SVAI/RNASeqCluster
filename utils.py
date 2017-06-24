import pysam
import pandas as pd
import datetime

read_attrs = ["query_name", "flag", "reference_id", "reference_start", "mapping_quality", "cigarstring", "next_reference_id", "next_reference_start", "query_alignment_length", "query_sequence", "query_qualities", "tags"]

def alignedSegmentToDataFrame(samfile, maxreads=None):
     listOfReads = []
     counter = 0
     for row in samfile:
        readDict = {}
        for attr in read_attrs:
            value = getattr(row, attr)
            readDict[attr] = value
        listOfReads.append(readDict)
        if maxreads is not None:
            counter += 1
            if counter > maxreads:
                break

     df = pd.DataFrame(listOfReads)
     print(df)

if __name__ == "__main__":
    # Load .bam file
    start = datetime.datetime.now()
    samfile = pysam.AlignmentFile("test.bam", "rb")
    end = datetime.datetime.now()

    print("Time to load .sam file: {}".format(end - start))

    # Convert Alignment to Data Frame, time how long it takes
    start = datetime.datetime.now()
    alignedSegmentToDataFrame(samfile, None)
    end = datetime.datetime.now()

    print((end - start))
