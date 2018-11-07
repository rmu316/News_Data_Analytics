#!/usr/bin/env python3
import datetime
import psycopg2

DBNAME = "news"


def getMostPopArticles():
    print "1. What are the most popular three articles of all time?\n"
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    query = '''\
        select title, Results.views
        from articles,
          (select path, count(*) as views
            from
              (select *
              from log
              where status=%s
              and path!=%s)
              as ActualViews
              group by path
              order by 2 desc
              limit 3)
            as Results
          where articles.slug=substring(Results.path from 10)
        order by 2 desc
        '''
    cursor.execute(query, ('200 OK', '/'))
    results = cursor.fetchall()
    conn.close()
    for title, count in results:
        print "\"" + str(title) + "\" -- " + str(count) + " views"
    print "\n"


def getMostPopAuthors():
    print "2. Who are the most popular article authors of all time?\n"
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    query = '''\
        select name, PopAuthorsById.a_views
        from
            (select author_id as a_id, sum(ArticlesAndAuthors.views) as a_views
            from
                (select articles.author as author_id, PopArticles.views
                as views
                from articles,
                    (select path, count(*) as views
                        from
                           (select * from log
                           where status='200 OK'
                           and path!='//')
                           as ActualViews
                           group by path
                           order by 2 desc)
                           as PopArticles
                    where articles.slug=substring(PopArticles.path from 10)
                    order by 2 desc)
                as ArticlesAndAuthors
            group by 1
            order by 2 desc)
        as PopAuthorsById, authors
        where PopAuthorsById.a_id=authors.id
        '''
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    for author_name, views in results:
        print author_name + " -- " + str(views) + " views"
    print "\n"


def getAllDaysErrors():
    print "3. On which days did more than 1% of requests lead to errors?\n"
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    query = '''\
        select TotalRequestsPerDay.theDay, TotalRequestsPerDay.nReqs,
        FailedRequestsPerDay.nFail
        from
            (select date(time) as theDay, count(*) as nReqs
            from log
            group by 1
            order by 1)
            as TotalRequestsPerDay,
            (select date(time) as theDay, count(*) as nFail
            from log
            where status!='200 OK'
            group by 1
            order by 1)
            as FailedRequestsPerDay
        where TotalRequestsPerDay.theDay=FailedRequestsPerDay.theDay
        and FailedRequestsPerDay.nFail*100 > TotalRequestsPerDay.nReqs
        order by 1
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    for date, nReqs, nFail in results:
        print date.strftime('%B %-m, %Y') + " -- " + \
            str(round(nFail*100/float(nReqs), 2)) + "% errors"
    print "\n"


getMostPopArticles()
getMostPopAuthors()
getAllDaysErrors()
