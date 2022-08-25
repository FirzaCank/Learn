theia@theiadocker-rzasandjaya:/home/project$ cat /etc/passwd

#output
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
theia:x:1000:1000:,,,:/home/theia:/bin/bash
mongodb:x:102:106::/var/lib/mongodb:/usr/sbin/nologin
ntp:x:103:107::/nonexistent:/usr/sbin/nologin
cassandra:x:104:108:Cassandra database,,,:/var/lib/cassandra:/usr/sbin/nologin
postgres:x:105:109:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash

-----------------------------------------------------------------------------------------

theia@theiadocker-rzasandjaya:/home/project$ cut -d":" -f1,3,6 /etc/passwd
#-d for delimiter
#-f for field/column

#output
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin
sys:3:/dev
sync:4:/bin
games:5:/usr/games
man:6:/var/cache/man
lp:7:/var/spool/lpd
mail:8:/var/mail
news:9:/var/spool/news
uucp:10:/var/spool/uucp
proxy:13:/bin
www-data:33:/var/www
backup:34:/var/backups
list:38:/var/list
irc:39:/var/run/ircd
gnats:41:/var/lib/gnats
nobody:65534:/nonexistent
_apt:100:/nonexistent
messagebus:101:/nonexistent
theia:1000:/home/theia
mongodb:102:/var/lib/mongodb
ntp:103:/nonexistent
cassandra:104:/var/lib/cassandra
postgres:105:/var/lib/postgresql
