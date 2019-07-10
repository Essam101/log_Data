LOG ANALYSIS PROJECT

you should setup:
-install vagrant and virtualbox
-Download repositroy from here https://github.com/udacity/fullstack-nanodegree-vm
-get newsdata.sql in our vagrant directory

Used: 
-postgersql 
-python3 
-vitual machine NM vagrant 


How to run:
- change directory to vagrant directory
-vagrant up (run the vagrant on vm)
-vagrant ssh (login into vm)
-change directory to vagrant
-use  psql -d news -f newsdata.sql to load database
	-use psql news to acces to database
	-use \d to see relatoins in DB
	-use \dt to see table
	-use \q to exit to database
-use python3 to run the script
--
*Project Requirements 
-what are the most popular three articles of all time?
-who are the most popular article authors af all time?
-on which days did more the 1% of requests lead to errors?
--
Create Views 
-i created this views in order to facilitate the task and make the queries smpile
________________________________________________________________
frist View (view requests)
--
CREATE view requests as select time::date as day, count(*)
        from log group by time::date
        order by time::date;
 _________________________________________________________________
seconed view (view error_not_found)
--
CREATE VIEW error_not_found as select time::date as day, count(*)
        from log
        where status = '404 NOT FOUND'
        group by time::date
        order by time::date;
__________________________________________________________________
third view (view Calc_error)
--
CREATE VIEW Calc_error as SELECT requests.day, round(error_not_found.count*1.00 / requests.count*1.00 * 100,2)
        as error_prc
        from requests, error_not_found
        where requests.day = error_not_found.day;
