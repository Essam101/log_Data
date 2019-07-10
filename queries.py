#!/user/bin/env pyhton3
# -*- coding: utf-8 -*-
import psycopg2
import pycodestyle


one = """
        SELECT title,count(title)
        as views_one
	FROM articles,log
	where log.path
	like '/%/'||articles.slug
	group by title
	order by views_one
	desc limit 3 ;
	"""
two = """
	SELECT authors.name,
	count(articles.author)
	as pop
	from articles,log ,authors
	where log.path
	like '/%/'||articles.slug
	and articles.author=authors.id
	group by authors.name
	order by pop
	desc ;
"""
three = """
	SELECT *from Calc_error
	where error_prc > 1 ;

"""


def query_one(one):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(one)
    equal = c.fetchall()
    db.close()
    print('query_one:-')
    for x in equal:
        print(format(x[0]) + "||" + format(x[1]))


def query_two(two):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(two)
    equal = c.fetchall()
    db.close()
    print('query_two:-')
    for x in equal:
        print(format(x[0]) + "||" + format(x[1]))


def query_three(three):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(three)
    equal = c.fetchall()
    db.close()
    print('query_three:-')
    for x in equal:
        print(format(x[0]) + "||" + format(x[1]) + " %")


if __name__ == '__main__':
    query_one(one)
    query_two(two)
    query_three(three)
