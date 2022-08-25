#very first step :
start_postgres

#In this exercise we will create a table called ‘users‘ in the PostgreSQL database. This table will hold the user account information.

#The table ‘users’ will have the following columns:
#uname
#uid
#home




#Step 1: Connect to the database server
  #Use the connection string saved in the previous exercise to connect to the PostgreSQL server.
  #Run the command below to login to PostgreSQL server.
  
  psql --username=postgres --host=localhost
  
  #You will get the psql prompt: ‘postgres=#’
  #output
    psql (14.5 (Ubuntu 14.5-1.pgdg18.04+1), server 13.2)
    Type "help" for help.

    postgres=#





#Step 2: Connect to a database.
  #We will use a database called template1 which is already available by default.
  #To connect to this database, run the following command at the ‘postgres=#’ prompt.
  
  \c template1
  
  #output :
    psql (14.5 (Ubuntu 14.5-1.pgdg18.04+1), server 13.2)
    Type "help" for help.

    postgres=# \c template1
    psql (14.5 (Ubuntu 14.5-1.pgdg18.04+1), server 13.2)
    You are now connected to database "template1" as user "postgres".
    template1=#
    
    
    
    
    
    
#Step 3: Create the table
  #Run the following statement at the ‘template1=#’ prompt:
  
  create table users(username varchar(50),userid int,homedirectory varchar(100));
  
  #If the table is created successfully, you will get the message below.

  CREATE TABLE





#Step 4: Quit the psql client
  #To exit the psql client and come back to the Linux shell, run the following command:
  \q
