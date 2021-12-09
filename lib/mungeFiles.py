import os
import shutil

# Demultiplex Direct File Path
demultiplexPath = f"{os.getcwd()}/Demultiplex"

# Get absolute path for munge Directory
mungePath = demultiplexPath + "/munge/"
# Get absolute path for FastQs Directory
fastQPath = demultiplexPath + "/fastqs/"
# Get absolute path for sam Directory
samPath = demultiplexPath + "/sam/"
# Get absolute path for bam Directory
bamPath = demultiplexPath + "/bam/"

# Store Parsed files in variable format
pooledSequences = open(f"{mungePath}hawkins_pooled_sequences.fastq")
clinicalData = open(f"{mungePath}harrington_clinical_data.txt")
dgorgonReference = open(f"{mungePath}dgorgon_reference.fa")

# Organizes pooled data into respective sequences
organizedPooledSequences = [' '.join(dat).split() for dat in 
    [sequence.split("\n") for sequence in pooledSequences.read().replace('+','').split("@")]
]

# Generate directory if it doesn't exist
def generateFolder(dirName):
    if (os.path.exists(f"{demultiplexPath}/{dirName}") == False):
        print(f"{dirName} Folder created.")
        os.mkdir(f"{demultiplexPath}/{dirName}")
    else: 
        print(f"{dirName} folder already exists.")

# Iterates across Target Directory <targetDir> and checks
# against File Type <fileType> for removal
def cleanUp(targetDir, fileType):        
    # Remove files at target directory   
    for files in os.listdir(targetDir):
        if files[files.index("."):] == fileType:
            print(f"Removing {files} at {targetDir}")
            os.remove(targetDir + files)
            
    # Remove empty directory        
    if len(os.listdir(targetDir)) == 0:
        shutil.rmtree(targetDir)

def cleanUpPrompt(targetDir, fileType):
 for i in range(1):
        print(f"\nWould you like to remove fileType {fileType}?")
        user_input = input("Type Yes to remove them, Type No to keep them.\n")
        
        # Remove files if prompted yes
        if user_input.lower() == "yes":
            print("Removing {fileType}")
            cleanUp(targetDir, fileType)
            break
    
        elif user_input.lower() == "no":
            print(f"{fileType} has not been deleted.")
            break
    
        else:
            print("Invalid response, please try again.")

