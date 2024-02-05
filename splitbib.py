###########################################
# Split a .bib file in individual entries #
###########################################

import sys
import os
import argparse

if __name__=='__main__':

    # read input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfiles', nargs='+')
    parser.add_argument('-o', '--outputdir')
    args = parser.parse_args()

    # make output directory
    if not os.path.exists(args.outputdir): os.makedirs(args.outputdir)

    # loop over input files
    for inputfile in args.inputfiles:
        # open the file and read the lines
        with open(inputfile, 'r') as f:
            lines = f.readlines()
        # strip whitespaces characters
        lines = [line.strip(' \t') for line in lines]
        # remove comments
        lines = [line for line in lines if not line.startswith('%')]
        # find entry starts
        starts = [idx for idx in range(len(lines)) if lines[idx].startswith('@')]
        # write output files
        for i in range(len(starts)):
            start = starts[i]
            finish = len(lines)+1 if i==len(starts)-1 else starts[i+1]
            thislines = lines[start:finish]
            outputfile = lines[start].split('{')[-1].strip(',')
            outputfile = os.path.join(args.outputdir, outputfile+'.bib')
            with open(outputfile, 'w') as f:
                for line in thislines: f.write(line)

