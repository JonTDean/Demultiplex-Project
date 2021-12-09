from lib.mthasinGetMutations import checkedSequence as patientData
from lib.mungeFiles import demultiplexPath
import os

def generateReport(clinData):
    count = None
    frequency = None
    im = None
    msn = None
    mp = None
    wtbp = None
    
    # patientName is name for each patientData key
    for patientName in patientData:
        moldColor = clinData["Color"][clinData["Name"].index(patientName)]
        # print base pair for each patient
        # Then loop through specific base pair data
        # Store data into empty variables 
        # and then log a report of them
        for basePair in patientData[patientName]:
            if patientData[patientName][basePair]["isMutant"] == True:
                count = patientData[patientName][basePair]["count"]
                frequency = patientData[patientName][basePair]["frequency"]
                mSN = patientData[patientName][basePair]["mutantSequenceName"]
                mP = patientData[patientName][basePair]["mutantPosition"]
                wTBP = patientData[patientName][basePair]["wildTypeBP"]
                for line in moldReport(patientName, moldColor, frequency, mSN, count, wTBP, basePair, mP): 
                    writeToReportTxt(line)
                for line in staticReport(patientName, moldColor, frequency, mSN, count, wTBP, basePair, mP): 
                    writeToReportTxt(line)
                    
    print(f"Finished, observe Report.txt located at {demultiplexPath}/report.txt")
    
    return exit
                
def moldReport(patientName, color, ntFreq, mutantSequenceName, count, wildTypeBP, basePair, mutantPos):
    return [
        f"\nSample {patientName} has a `{color} Mold` which is caused by a mutation in `position {mutantPos}` occuring at a frequency of `{ntFreq}%` in sequence `{mutantSequenceName}` over the course of `{count} reads`.", 
        f"* The wild type nucleotide is {wildTypeBP} and the mutation type nucleotide is {basePair}."
    ]
    
def staticReport(patientName, color, ntFreq, mutantSequenceName, count, wildTypeBP, basePair, mutantPos):
    return [
        f"\ti) Patient Name: {patientName}",
        f"\tii) {color} Mold is Mutant-Type",
        f"\tiii) Mutant Nucleotide: {basePair} at Position: {mutantPos} Sequence: {mutantSequenceName} occuring at a frequency of {ntFreq}% at {count} reads",
        f"\tiv) Wild Type: {wildTypeBP} point mutated at Position-{mutantPos} to Mutant Type: {basePair}"
    ]

def writeToReportTxt(lineData):
    reportTxt = open(f"{demultiplexPath}/report.txt", 'a')
    return reportTxt.write(lineData + "\n")
