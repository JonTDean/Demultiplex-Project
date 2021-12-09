# Demultiplex - MT - Non-DeBruijn



## Description

To demultiplex is to convert a data source that is combined, and to split up the relations into unrelated unique data sets.

For this project I wanted to learn how to munge data, learn about BioPy, and to further my knowledge of Genomics/BioInformatics. Alot of the process was made up of learning Graduate level material in consideration to the Genomics / Biological Algorithms.

In order for the layman to understand the concepts, I've included a quick review as to the underlying processes.

[Let's Learn!]('/grokGenomics.md')

The [sequence file]('./munge/hawkins_pooled_sequences.fastq') has barcodes(an amino acid chain) that read for the symptoms associated with the clinical data of the [patients]('./munge/harrington_clinical_data.txt'). By comparing and contrasting the motifs for each patient we are able to distinguish between wild types (*type of mutation*) and the reference disease [dgorgon]('./munge/dgorgon_reference.fa').
