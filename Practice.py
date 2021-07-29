
counties_dict = {}
counties_dict["Arapahoe"] = 42289
counties_dict["Denver"] = 46353
counties_dict["Jefferson"] = 432438
counties_dict
#len(counties_dict)
#print(len(counties_dict))

#print(counties_dict)

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)
