with open('testout.txt', 'w') as ols:
    with open('test.txt', 'r') as fls:
        for line in fls:
            line=line.strip()       
            ols.write(line)
            ols.write('\n')
