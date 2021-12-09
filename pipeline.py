from lib.clinicalData import generateBarcodeDict, generateClinicalFastq, populateClinicalFastq
from lib.mungeFiles import fastQPath, samPath, bamPath, clinicalData, dgorgonReference, organizedPooledSequences, generateFolder, cleanUp
from lib.convertF2S2B import convertToSAM, convertToBAM
from lib.mthasinGetMutations import pileupSortedBam
from lib.report import generateReport

# Dgorgon data set as absolute filepath name
dgorgonReferenceName = dgorgonReference.name
# Generate a Dictionary from the Clinical Data file
clinDatDict = generateBarcodeDict(clinicalData)

# Creates fastQs folder if it doesn't exist
generateFolder("fastqs")
# Creates bam folder if it doesn't exist
generateFolder("bam")
# Creates sam folder if it doesn't exist
generateFolder("sam")

# Create FastQ file tree
generateClinicalFastq(clinDatDict)

# Populate data into FastQ file tree
populateClinicalFastq(organizedPooledSequences, clinDatDict)

# Convert FastQ file tree into SAM files
convertToSAM(fastQPath, samPath, dgorgonReferenceName)

# Convert SAM into BAM files
# Then convert Bam to Ordered BAM Files
convertToBAM(samPath, bamPath, dgorgonReferenceName)

# Delete SAM files
cleanUp(samPath, ".sam")
# Delete non-sorted BAM files
cleanUp(bamPath, ".bam")

# Pysam the files
pileupSortedBam(bamPath)

# Generate report.txt
generateReport(clinDatDict)