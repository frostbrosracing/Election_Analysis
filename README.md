# An Election Audit of a U.S. Congressional Precinct in the State of Colorado

## Project Overview of the Election Audit
#### The purpose of this audit was to determine the benefit of using Python code to automate the reporting process of an election.  The code was written and developed within Microsoft Visual Studio Code.  
In order to assist the ***Colorado Board of Elections*** determine the outcome of a congressional election, a code script was written in which the recorded tabulated results were processed with the following outcomes:
  1.  The total number of votes cast
  2.  The total number of votes for each candidate
  3.  The percentage of votes for each candidate
  4.  The winner of the election based on popular vote
  5.  The county with the greatest voter turnout
  6.  The total number of votes cast within each county
  7.  The percentage of the total number of votes cast within each county
#### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.54.3

## Election-Audit Results
The code that was written to evaluate the tabulated election results output the results of the script to a text file.  That text file is shown below.

![VS_Code_election_results_Text_File.png](https://github.com/frostbrosracing/Election_Analysis/blob/main/Resources/VS_Code_election_results_Text_File.png)

Shown below is a screen shot of the terminal view within ***Microsoft Visual Studio Code*** of the executed code.  ***Microsoft Visual Studio Code*** is the *Integrated Development Environment*, or *IDE*, used for writing the **Python** code for this audit.

![VS_Code_Terminal_election_results.png](https://github.com/frostbrosracing/Election_Analysis/blob/main/Resources/VS_Code_Terminal_election_results.png)

Shown below is a screen shot of the ***GitBash*** view of the executed code:

![GitBash_election_results.png](https://github.com/frostbrosracing/Election_Analysis/blob/main/Resources/GitBash_election_results.png)

Shown below is a screen shot of the ***Command Line*** view of the executed code:

![Command_prompt_election_results.png](https://github.com/frostbrosracing/Election_Analysis/blob/main/Resources/Command_prompt_election_results.png)

*Note* - All three of these images show the result of the same code being run with the exception of line spacing adjustments for consistency of formatting.  This formatting adjustment had absolutely no impact on the calculated outcomes, and was simply done for comparison purposes.

### The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The counties in the precinct including their percentage of the total vote and the number of votes cast were:
   - Jefferson representing 10.5% of the vote with 38,855 votes cast.
   - Denver representing 82.8% of the vote with 306,055 votes cast.
   - Arapahoe representing 6.7% of the vote with 24,801 votes cast.

- **Denver** had the largest number of votes.
   
- The candidates along with the results of the election were:
   - Charles Casper Stockham, who received 23.0% of the vote and 85,213 votes.
   - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
   - Raymon Anthony Doane, who received 3.1% of the vote and 11,606 votes.

- The winner of the election was:
   - **Diana DeGette**, who received **73.8%** of the vote and **272,892** votes.

## Election-Audit Summary
The **Python** code that was written to analyze the outcome of this election can easily be applied to other elections; whether in other congressional districts, senatorial districts, or local elections.  By using this code for future elections, the election commission will have a valuable tool for reporting those election results.  Depending on the specific use case there will likely be some very minor adjustments to the code.  These adjustments could be made in just a matter of a few keystrokes.

1. The user of the code simply needs to direct the path to the appropriate file to be read in the analysis, and then to the appropriate file for the output to be recorded.  Below is an image of the portion of the code that needs to be modified for use in other elections.  The values circled in yellow represent the tabulated **.csv election results** file, and the text file that records the ouput.  By making a copy of the code and adjusting this text, the code can be run on any **.csv** file in which the results are formatted with the same column configuration.
2. If the same column configuration isn't used, the code can be modified to pull the values from the appropriate column to be calculated, and appropriately output to the text file.

![PyPoll_Challenge_Screenshot.png](https://github.com/frostbrosracing/Election_Analysis/blob/main/Resources/PyPoll_Challenge_Screenshot.png)

    
