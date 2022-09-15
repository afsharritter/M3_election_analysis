# Add dependencies
import csv
import os

# Assign a variable to load a file from a a path
path = "M3_PyPoll\M3_election_analysis\Resources\election_results.csv"
file_to_load = os.path.join(path)
#assign a variable to save a file to a path
file_to_save = os.path.join("M3_PyPoll\M3_election_analysis\Resources\election_analysis.txt")
outfile = open(file_to_save, "w")

# open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    # print the header row
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
    #     print(row)

# Total number of votes cast
# a complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# Open the file
# import os
# file_to_load = os.path.join("election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data) 

# # create a filename variable to a direct or indirect path to the file
# path = "M3_PyPoll\M3_election_analysis\Resources\election_results.csv"
# file_to_load = os.path.join(path)
# with open(file_to_load) as election_data:
#     print(election_data)

# file_to_save = os.path.join("M3_PyPoll\M3_election_analysis\Resources\election_analysis.txt")
# outfile = open(file_to_save, "w")
# outfile.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# outfile.close()