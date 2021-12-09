# 1A. 
# # Removes the Sequence Header based on the
# # index located at "-"
def trimHeader(seqHeader):
    return seqHeader[:seqHeader.index("-")]

# # Removes the Barcode based on the index
# # located at the 5th index of the DNA Sequence
def trimBarcode(seqDNA):
    return seqDNA[5:]

# 1B. 
# # Removes reoccuring occurences in the sequence DNA and the sequence IDF
# # Based on the reoccuring instance of D and F inside of the sequence IDF
def trimTail(seqDNA, seqIDF):
    for index in range(0, len(seqIDF) + 1):
        # count sequences of d and f
        # will break if d or f are at last index
        if (seqIDF[index] == "D" or seqIDF[index] == "F") and (seqIDF[index + 1] == "D" or seqIDF[index + 1] == "F"):
            return [seqDNA[:index], seqIDF[:index]]