# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.append("El Paso")

# counties.insert(2, "El Paso")
# counties.remove("El Paso")
# counties.pop(3)
# counties[2] = "El Paso"
# counties_tuple = ("Arapahoe", "Denver", "Jefferson")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# voting_data = []
# voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
# voting_data.append({"county": "Denver", "registered_voters": 463353})
# voting_data.append({"county": "Jefferson", "registered_voters": 432438})
# voting_data.insert(2, {"county": "El Paso", "registered_voters": 461149})
# voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
# voting_data.remove({"county": "Denver", "registered_voters": 463353})
# voting_data.insert(2, {"county": "Denver", "registered_voters": 463353})
# voting_data.append({"county": "Arapahoe", "registered_voters": 422829})


# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes) + "% of the total votes.")

#Same code using f-string
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county, voters in counties_dict.items():
#     print(county + " county has", str(voters) + " registered voters.")

#Same code using f-string
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")


# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

# for counties_dict in voting_data:
#     print(counties_dict["registered_voters"])

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

# dir({"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438})
# print(dir({"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}))

print(dir(float))