from django.shortcuts import render
import psycopg2
# Create your views here.


def index(request):
    conn = 0
    result = ''
    try:
        conn = psycopg2.connect(
            database = 'formationdjango',
            host = 'localhost',
            user = 'djangouser',
            password = 'secret',
        )
        curr = conn.cursor()
        curr.execute(
            """CREATE TABLE IF NOT EXISTS ex00_movies (
            episode_nb serial PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
            );
            """
        )
        conn.commit()
        conn.close()
    except psycopg2.DatabaseError as e:
        result = e
    finally:
        if conn is not None:
            result = 'OK'
    return render(request, 'ex00/create_table.html', {'result': result})
    # return HttpResponse("Hello, world")
