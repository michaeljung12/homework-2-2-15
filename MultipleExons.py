# open genomic_dna file and read the contents
genomic_dna = open("genomic_dna.txt").read()
# open the exon locations file
exon_locations = open("exons.txt")
# make a variable to hold the coding sequence that is formed from the the loop
coding_sequence = ""
# go through each line in the exon locations file
for line in exon_locations:
    # split the line using a comma
    positions = line.split(',')
    # define the start and stop positions
    start = int(positions[0])
    stop = int(positions[1])
    # extract the exon from the genomic dna
    exon = genomic_dna[start:stop]
    # add the exon to the end of the current coding sequence from the loop
    coding_sequence = coding_sequence + exon
# write the coding sequence to an output file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()



# Had to use help from the solution for this problem, I got stuck multiple times and did not know what to do
