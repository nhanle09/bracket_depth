# declare variables
ignore = False
block_comment = False
line_comment = False
quote_comment = False
bracket_counter = 0

# open input.txt files for reading
sample_file = open("input.txt", "r")
read_file = sample_file.readlines()

#iterate through each character of each line
for line in read_file:
    line_comment = False #line_comment reset
    for i in range(0, len(line)):
        # condition for line comments
        if line[i] == '/' and line[i-1] == '/':
            line_comment = True
        # ignore everything within quote comments
        elif line[i] == '"' and quote_comment == False:
            quote_comment = True
        elif line[i] == '"' and quote_comment == True:
            quote_comment = False
        # ignore everything within block comments
        elif line[i] == '/' and line[i+1] == '*' and block_comment == False:
            block_comment = True
        elif line[i] == '*' and line[i+1] == '/' and block_comment == True:
            block_comment = False
        # set global ignore condition for all 3 types of comments
        if line_comment == True or block_comment == True or quote_comment == True:
            ignore = True
        else:
            ignore = False
        # increment bracket counter if not within any comments lines/blocks
        if line[i] == '{' and ignore == False and ignore == False:
            bracket_counter += 1
        if line[i] == '}' and ignore == False and ignore == False:
            bracket_counter -= 1
    # print out bracket counter + each line of code
    print(str(bracket_counter) + line, end='')