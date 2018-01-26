# Newspaper Reporting Tool
This tool is used to generate information for internal use only. This tool summarizes three pieces of data: top three most popular articles, authors by popularity, days in which more than 1% of http requests led to an error.

## Getting Started/Installation Information
**Before proceeding, please confirm that you have properly installed [Virtual Box](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/), and that you have access to the file `newsdata.sql` unzipped from `newsdata.zip`.

Instructions for running this tool using the Terminal:
* Navigate to the directory where Vagrant is installed.
* Enter the command `vagrant up`
* Enter the command `vagrant ssh`
* At this point, you may be prompted to enter `cd /vagrant` to enter the shared file directory. Do so now.
* Once inside the shared directory, enter `psql news` to open the database.
* In order to run the reporting tool, the following views must be created: 
`create view error_count as select date(time) as date, count(status) as error from log where status != '200 OK' group by date order by date;`
`create view total_status as select date(time) as day, count(status) as all_logs from log group by day order by day;`
`create view errors_in_status as SELECT error, all_logs from error_count join total_status on error_count.date = total_status.day;`
`create view date_and_ratio as select to_char(day, 'Month DD, YYYY') as date, (round(errors_in_status.error)/errors_in_status.all_logs * 100) as ratio from total_status join errors_in_status on errors_in_status.all_logs = total_status.all_logs order by date;`
* Run the reporting tool using the command `python analysis.py`

