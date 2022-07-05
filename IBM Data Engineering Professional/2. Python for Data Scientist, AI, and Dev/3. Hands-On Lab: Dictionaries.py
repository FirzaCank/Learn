# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

{'key1': 1,           #output
 'key2': '2',
 'key3': [3, 3, 3],
 'key4': (4, 4, 4),
 'key5': 5,
 (0, 1): 6}

-----------------------------------------------------------------------------------------------------
# Access to the value by the key

Dict["key1"]
Dict[(0, 1)]

1 #output
6

-----------------------------------------------------------------------------------------------------
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

{'Thriller': '1982',
 'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977'}

-----------------------------------------------------------------------------------------------------
# Get value by keys

release_year_dict['Thriller'] 

1982

-----------------------------------------------------------------------------------------------------
# Get all the keys and values in dictionary

release_year_dict.keys()
release_year_dict.values()

#output
dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])
dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

-----------------------------------------------------------------------------------------------------
# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict

{'Thriller': '1982',                    #output
 'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977',
 'Graduation': '2007'}

-----------------------------------------------------------------------------------------------------
# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

{'Back in Black': '1980',                 #output
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977'}

-----------------------------------------------------------------------------------------------------
# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict

True #output
