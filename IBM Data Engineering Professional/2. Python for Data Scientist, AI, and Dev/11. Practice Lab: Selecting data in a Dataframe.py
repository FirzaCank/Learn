#NOTE

# iloc ----> -1 kalo range
# loc -----> pas kalo range




# let us import the Pandas Library
import pandas as pd

# Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

#output
	Name	ID	Department	Salary
0	Rose	1	Architect Group	100000
1	John	2	Software Group	80000
2	Jane	3	Design Team	50000
3	Mary	4	Infrastructure	60000

-------------------------------------------------------------------------------------------------------------------------------------------------------
#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

#output
	ID
0	1
1	2
2	3
3	4

-------------------------------------------------------------------------------------------------------------------------------------------------------
#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z

#output
	Department	Salary	ID
0	Architect Group	100000	1
1	Software Group	80000	2
2	Design Team	50000	3
3	Infrastructure	60000	4

-------------------------------------------------------------------------------------------------------------------------------------------------------
# Access the value on the first row and the first column

df.iloc[0, 0]

-------------------------------------------------------------------------------------------------------------------------------------------------------
#set index column

df1=df
df1=df1.set_index("Name")

#To display the first 5 rows of new dataframe
df1.head()

#output
	ID	Department	Salary
Name			
Rose	1	Architect Group	100000
John	2	Software Group	80000
Jane	3	Design Team	50000
Mary	4	Infrastructure	60000



#Now, let us access the column using the name
df1.loc['Jane', 'Salary']

#output
50000

-------------------------------------------------------------------------------------------------------------------------------------------------------
# let us do the slicing using old dataframe df
# 	Name	ID	Department	Salary
# 0	Rose	1	Architect Group	100000
# 1	John	2	Software Group	80000
# 2	Jane	3	Design Team	50000
# 3	Mary	4	Infrastructure	60000


df.iloc[0:2, 0:3] -------> #-1 kalau range

#output
	Name	ID	Department
0	Rose	1	Architect Group
1	John	2	Software Group



#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department'] ---------> #sesuai kalau range

#output
	ID	Department
0	1	Architect Group
1	2	Software Group
2	3	Design Team



#let us do the slicing using loc() function on new dataframe df1 where index column is Name having labels: Rose, John and Jane
df1.loc['Rose':'Jane', 'ID':'Department']

#output
	ID	Department
Name		
Rose	1	Architect Group
John	2	Software Group
Jane	3	Design Team
