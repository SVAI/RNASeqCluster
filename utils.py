import os
import datetime

import pandas as pd
import pysam

data_dir = "data"
merged_file = os.path.join(data_dir, "data.pickle")
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

def preprocess_file(file):
    experiment_name = os.path.split(file)[-1].split("_")[0]
    label = os.path.split(file)[-1].split("_")[1].split(".")[0]

    data = pd.read_csv(file, delimiter="\t")
    data = data.set_index("Gene")
    data = data.transpose()
    data = data.rename(index={"Count": experiment_name})
    data["label"] = pd.Series(label, index=data.index)
    return data

def merge_experiments(filepath=merged_file):
    if os.path.isfile(filepath):
        return pd.read_pickle(filepath)
    # Get experiment file names
    files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if "counts" in f]
    results = pd.concat([preprocess_file(f) for f in files])
    meta = ["__alignment_not_unique", "__ambiguous", "__no_feature", "__not_aligned", "__too_low_aQual"]
    results = results.drop(meta, axis=1)
    results = results.fillna(0)
    pd.to_pickle(results, filepath)
    results.to_csv(filepath.split(".")[0] + ".csv", index=False)
    return results

if __name__ == "__main__":
    # Load .bam file
    # samfile = pysam.AlignmentFile("test.bam", "rb")
    df = merge_experiments()
