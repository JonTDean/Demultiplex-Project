import pysam
import os
from lib.mungeFiles import dgorgonReference

# Globals
checkedSequence = {}
dgorgonSequence = [line for line in dgorgonReference.read().split("\n")][1]

# Iterate across all Sorted Bam files
def pileupSortedBam(bamFolder):
    for sortedBam in os.listdir(bamFolder):
        if sortedBam[sortedBam.index("."):] != ".sorted.bam.bai":
            checkedSequence[sortedBam[:sortedBam.index(".")]] = pileup(bamFolder + sortedBam)
        else:
            continue

def pileup(sortedBamFile):
    samfile = pysam.AlignmentFile(f"{sortedBamFile}", "rb")
    
    #use a dictionary to count up the bases at each position
    ntdict = {}

    #Since our reference only has a single sequence, we're going to pile up ALL of the reads. Usually you would do it in a specific region (such as chromosome 1, position 1023 to 1050 for example)
    for pileupcolumn in samfile.pileup():
        # Nucleotide frequency
        ntFreq = pileupcolumn.n
        # Nucleotide position 
        ntPos = pileupcolumn.pos
        
        for pileupread in pileupcolumn.pileups:
            # Sequence Name
            seqName = pileupread.alignment.query_name
            # Nucleotide Sequence
            ntSeq = pileupread.alignment.query_sequence
            # Nucleotide Base
            base = ntSeq[pileupread.query_position]

            # If the pileup is neither deleted nor skipped by reference
            if not pileupread.is_del and not pileupread.is_refskip:
                if not(base in ntdict):
                    ntdict[base] = {"count": 1, "frequency": 0, "isMutant": False, "mutantSequenceName": None, "mutantPosition": 0, "wildTypeBP": base}
                else:
                    ntdict[base]["count"] += 1
                    ntdict[base]["frequency"] = ntdict[base]["count"] / ntFreq
                    
                # Does comparison check against the first 
                # Mutation inside of the genetic sequence then
                # Populates ntdict with information for report
                if dgorgonSequence[ntPos] != base:
                    ntdict[base]["mutantSequenceName"] = seqName 
                    ntdict[base]["mutantPosition"] = ntPos
                    ntdict[base]["isMutant"] = True
                    ntdict[base]["wildTypeBP"] = dgorgonSequence[ntPos]

    samfile.close()
    return ntdict
