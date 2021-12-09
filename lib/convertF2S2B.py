import os

# Convert FastQ Files to SAM Files
def convertToSAM(rootDir, samFolder, dgorgRef):

    # FastQ to SAM Conversion
    for fileFQ in os.listdir(rootDir):
        try:
            # Patient Name retrieval
            # Trim the <_trimmed.fastq> portion of
            patientName = fileFQ[:fileFQ.index("_")]

            # Index file and run FQ2S conversion 
            os.system(f"bwa index {dgorgRef} && bwa mem {dgorgRef} {rootDir}{patientName}_trimmed.fastq > {samFolder}{patientName}.sam")
        except:
            continue

# Convert SAM Files to BAM Files
def convertToBAM(samFolder, bamFolder, dgorgRef):
    
    # SAM to BAM Conversion
    for fileSAM in os.listdir(samFolder):
        try:
            # Patient Name retrieval
            # Trim the <.sam> portion of
            patientName = fileSAM[:fileSAM.index(".")]
            
            # Convert SAM to BAM
            # Converted BAM files are created in the BAM Folder
            os.system(f"samtools view -bS {samFolder}{patientName}.sam > {bamFolder}{patientName}.bam")

            # Convert SAM to Sorted BAM
            os.system(f"samtools sort -m 100M -o {bamFolder}{patientName}.sorted.bam {bamFolder}{patientName}.bam")
            
            # Convert Sorted BAM to Indexed Sorted BAM
            os.system(f"samtools index {bamFolder}{patientName}.sorted.bam")
        except:
            continue