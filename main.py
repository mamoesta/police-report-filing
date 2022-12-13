import transcripting as ts
import os
import sys

'''female_interviews = os.listdir('/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/female/int/')

male_interviews = os.listdir('/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/male/int/')

female_output = '/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/female/interview-results/'

male_output = '/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/male/interview-results/'
'''

with open(sys.argv[1]) as file:
    lines = [line.rstrip() for line in file]
input_full_path = ['./open-interviews/' + x for x in lines]
print(len(input_full_path))
output = sys.argv[2]

#print(input_full_path, output)
ts.generate_transcript(input_full_path, output)