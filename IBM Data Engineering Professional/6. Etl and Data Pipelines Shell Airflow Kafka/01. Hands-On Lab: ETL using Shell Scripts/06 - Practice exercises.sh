# cp-access-log.sh
# This script downloads the file 'web-server-access-log.txt.gz'
# from "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/".

# The script then extracts the .txt file using gunzip.

# The .txt file contains the timestamp, latitude, longitude 
# and visitor id apart from other data.

# Transforms the text delimeter from "#" to "," and saves to a csv file.
# Loads the data from the CSV file into the table 'access_log' in PostgreSQL database.



# Download the access log file
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz"


# Unzip the file to extract the .txt file
gunzip -f web-server-access-log.txt.gz
# The -f option of gunzip is to overwrite the file if it already exists.

#---------------------------------------------------------------------------------------------

# Extract phase
echo "Extracting data"

# Extract the columns 1 (timestamp), 2 (latitude), 3 (longitude) and 
# 4 (visitorid)
cut -d"#" -f1-4 web-server-access-log.txt > extracted-data.txt

#---------------------------------------------------------------------------------------------

# Transform phase
echo "Transforming data"

# read the extracted data and replace the colons with commas.
tr "#" "," < extracted-data.txt > transformed-data.csv

#---------------------------------------------------------------------------------------------

# Load phase
echo "Loading data"

# Send the instructions to connect to 'template1' and
# copy the file to the table 'access_log' through command pipeline.

echo "\c template1;\COPY access_log  FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV HEADER;" | psql --username=postgres --host=localhost








#Verify by querying the database.
#Run the ‘select’ statement through ‘psql’ with the help of command pipeline.
theia@theiadocker-rzasandjaya:/home/project$ echo '\c template1; \\SELECT * from access_log;' | psql --username=postgres --host=localhost

#ouput
You are now connected to database "template1" as user "postgres".
      timestamp      | latitude  | longitude  |              visitorid               
---------------------+-----------+------------+--------------------------------------
 2021-02-07 13:55:01 | -16.23949 | -132.90744 | EDB35D96-3B72-7765-BD21-E955A87675B2
 2020-07-16 15:36:41 | -34.19226 | -154.14365 | 7AEBC97C-7BD4-BA94-837A-8CDB3E880226
 2021-09-13 05:50:33 |  33.04489 |   41.19598 | 39712A91-BBC8-EF3E-F984-4BDBC47057E9
 2020-07-13 16:23:35 | -50.85272 | -108.75484 | 06A1B090-9696-2173-2A3B-D2C45AA069D6
 2022-02-11 02:09:34 | -61.60674 |   82.79596 | DE2D0452-0772-8F82-5E97-0B7354F84DEC
