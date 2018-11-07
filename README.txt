# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________

## About
This project uses SQL commands to get useful information about a web app's usage, authors, and articles


## Prerequisites
1. Make sure that python version 2 or 3 is installed: https://www.python.org/downloads/
2. Install VirtualBox VM: https://www.virtualbox.org/wiki/Downloads
3. Install Vagrant: https://www.vagrantup.com/downloads.html
4. Download the newsdata.sql here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5. Unzip the newsdata.sql file, and place it into your vagrant directory.
6. Setup your vagrant VM using the command "vagrant up"
7. Once the VM is up, login using the command "vagrant ssh"
8. From there, type "cd /vagrant/" to log into the vagrant main directory.
9. Load the data inside the vagrant directed, created by newsdata.sql by running the following command:
   psql -d news -f newsdata.sql
10. Copy my newsdata.py file into the same directory (within /vagrant)


# Testing
* In the vagrant command line, simply run the following command:

vagrant@vagrant:/vagrant$ python newsdata.py

# Output
You should see a result that looks like this:

1. What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views


2. Who are the most popular article authors of all time?

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views


3. On which days did more than 1% of requests lead to errors?

July 7, 2016 -- 2.26% errors