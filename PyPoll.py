# Add dependencies
import csv
import os

# Assign a variable to load a file from a a path
path = "M3_PyPoll\M3_election_analysis\Resources\election_results.csv"
file_to_load = os.path.join(path)

#assign a variable to save a file to a path
file_to_save = os.path.join("M3_PyPoll\M3_election_analysis\Resources\election_analysis.txt")

# initalize the vote counter
total_votes = 0

#candidate options
candidate_options = []

#candidate votes
candidate_votes = {}

# winning candidate and winning count tracker
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
 
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
 
    # print the header row
    headers = next(file_reader)
    print(headers)
 
    # add to the total vote count for each row of data
    for row in file_reader:
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #need to use an if statement so that we dont keep adding duplicate names for every row
        if candidate_name not in candidate_options:
   
            # Append the candidate name to list of candidates options
            candidate_options.append(candidate_name)
   
            # start tracking votes per candidates
            candidate_votes[candidate_name] = 0
        # count votes
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
       
    # save the final vote count to the text file
    txt_file.write(election_results)
 
    # Retrieve vote count and percentage 
    #1. iterate through the candidate list
    for candidate_name in candidate_votes:

        # 2 retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # 3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # print to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # save to txt file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # 2. if true then set winning_count = votes and winning_percent =
            # vote_percentage
            winning_count = votes 
            winning_percentage = vote_percentage

            # set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        
        
    # The winner of the election based on popular vote
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    
    # save the winning candidate's result to txt
    txt_file.write(winning_candidate_summary)

