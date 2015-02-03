# open input.txt
file = open("input.txt")
# open and write in the output file
output = open("trimmed.txt", "w")
# in the input file, go through each line
for dna in file:
    # trim the dna so it starts after the 14th character
    trimmed_dna = dna[14:]
    # write the trimmed sequence in output file
    output.write(trimmed_dna)
    # print the length and trimmed sequence
    print("the processed sequence and its length: " + trimmed_dna + str(len(trimmed_dna)))

