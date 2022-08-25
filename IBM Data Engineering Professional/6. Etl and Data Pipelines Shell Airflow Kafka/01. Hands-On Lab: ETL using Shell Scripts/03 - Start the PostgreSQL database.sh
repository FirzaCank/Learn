#On the terminal run the following command to start the PostgreSQL database.
start_postgres
#output
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
d19f32bd9e41: Pull complete 
Digest: sha256:34fea4f31bf187bc915536831fd0afc9d214755bf700b5cdb1336c82516d154e
Status: Downloaded newer image for ubuntu:latest
Starting your Postgres database....
This process can take up to a minute.
      
Postgres database started, waiting for all services to be ready....
      
Your Postgres database is now ready to use and available with username: postgres password: MTc5Nzctcnphc2Fu

You can access your Postgres database via:
 • The Browser with pgadmin
   • URL: https://rzasandjaya-5050.theiadocker-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/browser/
   • Database Password: MTc5Nzctcnphc2Fu
 • CommandLine: psql --username=postgres --host=localhost
 

#Note down the access information presented towards the end of these messages, especially the CommandLine:.

#A sample commandline displayed looks as given below.
`psql --username=postgres --host=localhost`

