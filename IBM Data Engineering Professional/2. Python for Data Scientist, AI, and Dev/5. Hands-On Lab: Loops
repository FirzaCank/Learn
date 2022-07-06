# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

0 red     #output
1 yellow
2 green
3 purple
4 blue

--------------------------------------------------------------------------
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

1982    #output
1980
It took  2 repetitions to get out of loop.

# Figure explanantion While : https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/LoopsWlsNetwork/labs/Module%203/imageshile.gif

--------------------------------------------------------------------------
#While type 1 : Stop saat ngecek "oh ini <= 6", disitu dia ga lanjutin

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
rating = PlayListRatings[0]



while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i+1
    rating = PlayListRatings[i]

10          
9.5
10
8
7.5

--------------------------------------------------------------------------
#While type 2 : masih kebawa yang ga sesuai syaratnya

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
rating = PlayListRatings[0]



while(i < len(PlayListRatings) and rating >= 6):
    rating = PlayListRatings[i]
    print(rating)
    i = i+1

10
9.5
10
8
7.5
5
