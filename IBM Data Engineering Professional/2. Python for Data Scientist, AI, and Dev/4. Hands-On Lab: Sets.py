SET not provide duplicate item and automatically do ordered ascending



# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1

{'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'} #output

---------------------------------------------------------------------------------
# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

{'00:42:19',        #output
 10.0,
 1982,
 '30-Nov-82',
 46.0,
 65,
 'Michael Jackson',
 None,
 'Pop, Rock, R&B',
 'Thriller'}

---------------------------------------------------------------------------------
# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

{'R&B',               #output
 'disco',
 'folk rock',
 'hard rock',
 'pop',
 'progressive rock',
 'rock',
 'soft rock',
 'soul'}

---------------------------------------------------------------------------------
# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A

{'AC/DC', 'Back in Black', 'Thriller'} #output

---------------------------------------------------------------------------------
# Add element to set using .add()

A.add("NSYNC")
A

{'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'} #output

---------------------------------------------------------------------------------
# Remove the element from set

A.remove("NSYNC")
A

{'AC/DC', 'Back in Black', 'Thriller'} #output

---------------------------------------------------------------------------------
# Verify if the element is in the set using "IN"

"AC/DC" in A
True #output







---------------------------------------------------------------------------------
# SET LOGIC OPERATIONS
# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

({'AC/DC', 'Back in Black', 'Thriller'},
 {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'})

---------------------------------------------------------------------------------
# Find the intersections

intersection = album_set1 & album_set2
intersection

{'AC/DC', 'Back in Black'} #OUTPUT

---------------------------------------------------------------------------------
# Find the difference in set1 but not set2 and otherwise

album_set1.difference(album_set2)
{'Thriller'} #output

album_set2.difference(album_set1)  
{'The Dark Side of the Moon'} #output

---------------------------------------------------------------------------------
# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)
{'AC/DC', 'Back in Black'} #output

---------------------------------------------------------------------------------
# Find the union of two sets

album_set1.union(album_set2)
{'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'} #output

---------------------------------------------------------------------------------
# Check a set is a superset or subset of another set, respectively,

set(album_set1).issuperset(album_set2)
False #output

set(album_set2).issubset(album_set1)     (HIMPUNAN BAGIAN DARI)
False #output

---------------------------------------------------------------------------------
# Check if subset (HIMPUNAN BAGIAN)

set({"Back in Black", "AC/DC"}).issubset(album_set1)
True #output

# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})
True #output
