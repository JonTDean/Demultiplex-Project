from lib.mungeFiles import demultiplexPath, fastQPath
from lib.trimData import trimBarcode, trimHeader, trimTail
# Clinical Data Cleanup
def generateBarcodeDict(clinDat):
    """
        Generates a dictionary from the barcodes supplied from harrington_clinical_data.txt
    """
    clinicalDataDict = {}

    # Split tsv into organized array
    clinicalDataArray = [row.split("\t") for row in clinDat.read().split('\n') if row != '']

    # Set the 0th Headers/First Row-Column Values
    # for the Dictionary to respective Keys
    # Each Key has a Value of an empty Array
    try:
        for header in clinicalDataArray[0]:
            clinicalDataDict[header] = []
    except:
        print("Unkown Error for Header creation")

    # Set the data to respective columns
    try:
        for data in clinicalDataArray[1:]:
            clinicalDataDict['Name'].append(data[0])
            clinicalDataDict['Color'].append(data[1])
            clinicalDataDict['Barcode'].append(data[2])
    except:
        print("Unkown Error for Populate Columns")

    return clinicalDataDict

# Generate Clinical FastQ Files
def generateClinicalFastq(organizedClinData):
    """
        Generates FastQ file structure based on Harrington Clinical Data
    """
    # Creates FastQ file for each Patient
    for patient in organizedClinData["Name"]: 
        try:
            open(f"{demultiplexPath}/fastqs/{patient}_trimmed.fastq", "x+")        
            print(f"File Created - {patient}_trimmed.fastq")
        except:
            print(f"File already exists for {patient}")

# Fill Clinical FastQ files with matching pooled sequences
def populateClinicalFastq(incSequences, patients):
    """
        Populate the Fastq files via patients dictionary
    """

    # Iterate across all of the Patient Data
    for id in range(0, 50):
        if len(open(fastQPath + patients["Name"][id] + "_trimmed.fastq", 'r').readlines()) < 3:
            print("Patient Data Generated for", patients["Name"][id]," - Barcode:", patients["Barcode"][id])
            writeToPatientFile(incSequences, patients["Name"][id], patients["Barcode"][id])
        else:
            print("Patient Data exists for:", patients["Name"][id])
            continue


def writeToPatientFile(incSequences, pName, pBarcode):
    """
        Write Patient Data to file based on conditional of DNA Sequence match
    """

    # Expensive operation to check and populate all
    # Sequences in list and populate based on 
    # the First 5 nucleotides
    for seqIndex in range(1, len(incSequences) + 1):
        try:
            # Destructure into readable tuple
            sHeader = f"@{trimHeader(incSequences[seqIndex][0])}\n"
            (sDNA, sIDF) = trimTail(incSequences[seqIndex][1], incSequences[seqIndex][2])

            # Matches barcode based on first 5 of DNA Sequence
            if sDNA[0:5] == pBarcode:
                # Opens Generated File
                patientFile = open(f"{fastQPath}{pName}_trimmed.fastq", "a")
                
                # Writes the following data to the specified patient file
                patientFile.writelines([sHeader, f"{trimBarcode(sDNA)}\n", f"{sIDF}\n"])
                
                # Close the file when done
                patientFile.close()
        except:
            continue