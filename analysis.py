import psycopg2
import datetime


def top_three_articles():
    DB = psycopg2.connect(dbname="news")
    c = DB.cursor()
    run_query = "SELECT title, count(path) as popularity \
    FROM articles \
    JOIN log \
    ON log.path = concat('/article/', slug) \
    group by title \
    order by popularity desc limit 3;"
    c.execute(run_query)
    results = c.fetchall()
    print "  Query 1: What are the most popular three articles of all time?"
    for data in results:
        print data[0] + " -- " + str(data[1]) + " views"
    print "\n"
    DB.close()


def authors_by_popularity():
    DB = psycopg2.connect(dbname="news")
    c = DB.cursor()
    run_query = "SELECT name, count(path) as popularity \
    FROM articles JOIN log ON log.path = concat('/article/', slug) \
    JOIN authors \
    ON articles.author=authors.id \
    group by name \
    order by popularity desc;"
    c.execute(run_query)
    results = c.fetchall()
    print "  Query 2: Who are the most popular article authors of all time?"
    for data in results:
        print data[0] + " -- " + str(data[1]) + " views"
    print "\n"
    DB.close()


def error_log():
    DB = psycopg2.connect(dbname="news")
    c = DB.cursor()
    run_query = "SELECT date, round(ratio::numeric, 1) \
    FROM date_and_ratio \
    WHERE ratio > 1;"
    c.execute(run_query)
    results = c.fetchall()
    print "  Query 3: On which days did more than 1% of \
    requests lead to errors?"
    for data in results:
        print data[0] + " -- " + str(data[1]) + " % errors"
    print "\n"
    DB.close()


top_three_articles()
authors_by_popularity()
error_log()
