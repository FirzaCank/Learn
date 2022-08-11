#Extract
#Reading data from CSV in Python
import piplite
await piplite.install(['seaborn', 'lxml', 'openpyxl'])

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)

df

#output
	0	1	2	3	4	5
0	John	Doe	120 jefferson st.	Riverside	NJ	8075
1	Jack	McGinnis	220 hobo Av.	Phila	PA	9119
2	John "Da Man"	Repici	120 Jefferson St.	Riverside	NJ	8075
3	Stephen	Tyler	7452 Terrace "At the Plaza" road	SomeTown	SD	91234
4	NaN	Blankman	NaN	SomeTown	SD	298
5	Joan "the bone", Anne	Jet	9th, at Terrace plc	Desert City	CO	123


#Adding column name to the DataFrame

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
df

#output
	First Name	Last Name	Location	City	State	Area Code
0	John	Doe	120 jefferson st.	Riverside	NJ	8075
1	Jack	McGinnis	220 hobo Av.	Phila	PA	9119
2	John "Da Man"	Repici	120 Jefferson St.	Riverside	NJ	8075
3	Stephen	Tyler	7452 Terrace "At the Plaza" road	SomeTown	SD	91234
4	NaN	Blankman	NaN	SomeTown	SD	298


# Select single column
df["First Name"]

#Select multiple column
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df

#Selecting rows using .iloc and .loc
# To select the first row
df.loc[0]

#output
First Name                 John
Last Name                   Doe
Location      120 jefferson st.
City                  Riverside
State                        NJ
Area Code                  8075


## To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

#output
0             John
1             Jack
2    John "Da Man"

---------------------------------------------------------------------
#Transform Function in Pandas

#import library
import pandas as pd
import numpy as np
#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df

	a	b	c
0	1	2	3
1	4	5	6
2	7	8	9



#Let’s say we want to add 10 to each element in a dataframe:
#applying the transform function
df = df.transform(func = lambda x : x + 10)

#Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
