#2.1. Translate from one character set to another

#tr is a filter command used to translate, squeeze, and/or delete characters.

echo "Shell Scripting" | tr "[a-z]" "[A-Z]" 
#output
SHELL SCRIPTING

echo "Shell Scripting" | tr "[:lower:]" "[:upper:]" 
#output
SHELL SCRIPTING

echo "Shell Scripting" | tr  "[A-Z]" "[a-z]"
#output
shell scripting

------------------------------------------------
#2.2. Squeeze repeating occurrences of characters

#The -s option replaces a sequence of a repeated characters with a single occurrence of that character.
#The command below replaces repeat occurrences of ‘space’ in the output of ps command with one ‘space’.

theia@theiadocker-rzasandjaya:/home/project$ ps
#output
   PID TTY          TIME CMD
   648 pts/2    00:00:01 bash
  1016 pts/2    00:00:00 ps

ps | tr -s " "
#output
 PID TTY TIME CMD
 648 pts/2 00:00:01 bash
 1008 pts/2 00:00:00 ps
 1009 pts/2 00:00:00 tr
 
-----------------------------------------------
#2.3. Delete characters

#We can delete specified characters using the -d  option.
#The command below deletes all digits.

echo "My login pin is 5634" | tr -d "[:digit:]"
#output
My login pin is 

