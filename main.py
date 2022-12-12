import transcripting as ts
import os
import sys

'''female_interviews = os.listdir('/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/female/int/')

male_interviews = os.listdir('/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/male/int/')

female_output = '/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/female/interview-results/'

male_output = '/Users/martymoesta/Documents/git.nosync/police-report-filing/aussies/male/interview-results/'
'''
input = os.listdir(sys.argv[1])
input_full_path = [sys.argv[1] + x for x in input]
output = sys.argv[2]
#print(input_full_path, output)
ts.generate_transcript(input_full_path, output)