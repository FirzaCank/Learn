# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and 
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.



# Extract Phase
echo "Extracting data"
# Extract the columns 1 (user name), 2 (user id) and 
# 6 (home directory path) from /etc/passwd
cut -d":" -f1,3,6 /etc/passwd > extracted-data.txt



# Transform phase
echo "Transforming data"
# read the extracted data
tr ":" "," < extracted-data.txt > transformed-data.csv



# Load phase
echo "Loading data"
# Send the instructions to connect to 'template1' and
# copy the file to the table 'users' through command pipeline.

echo "\c template1;\COPY users  FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=localhost

-----------------------------------------------------------------------

theia@theiadocker-rzasandjaya:/home/project$ bash csv2db.sh
#output
Extracting data
Transforming data
Loading data
You are now connected to database "template1" as user "postgres".
COPY 25


theia@theiadocker-rzasandjaya:/home/project$ cat extracted-data.txt
#output
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin


theia@theiadocker-rzasandjaya:/home/project$ cat transformed-data.csv
#output
root,0,/root
daemon,1,/usr/sbin
bin,2,/bin


theia@theiadocker-rzasandjaya:/home/project$ echo '\c template1; \\SELECT * from users;' | psql --username=postgres --host=localhost
#output
You are now connected to database "template1" as user "postgres".
  username  | userid |    homedirectory    
------------+--------+---------------------
 root       |      0 | /root
 daemon     |      1 | /usr/sbin
 bin        |      2 | /bin
 sys        |      3 | /dev
 sync       |      4 | /bin
 games      |      5 | /usr/games
 man        |      6 | /var/cache/man
 lp         |      7 | /var/spool/lpd
 mail       |      8 | /var/mail
 news       |      9 | /var/spool/news
 uucp       |     10 | /var/spool/uucp
 proxy      |     13 | /bin
 www-data   |     33 | /var/www
 backup     |     34 | /var/backups
 list       |     38 | /var/list
 irc        |     39 | /var/run/ircd
 gnats      |     41 | /var/lib/gnats
 nobody     |  65534 | /nonexistent
 _apt       |    100 | /nonexistent
 messagebus |    101 | /nonexistent
 theia      |   1000 | /home/theia
 mongodb    |    102 | /var/lib/mongodb
 ntp        |    103 | /nonexistent
 cassandra  |    104 | /var/lib/cassandra
 postgres   |    105 | /var/lib/postgresql
(25 rows)
