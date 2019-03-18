import psycopg2
import uuid
import psycopg2.extras
'''
from celery_task import insert_newpost_to_celery
robject = redis.Redis(host='localhost', port=6379, db=0)
robject.set('insert_table', 0)
robject.set('post_feed', 0)
robject.set('get_post', 0)
robject.set('delete_post', 0)
robject.set('update_post', 0)
'''
conn = psycopg2.connect(database='Negi', user='postgres', password='welcome@123', host="127.0.0.1", port="5432")
conn.autocommit = True
print("CONNECTION MADE")


def insertion_into_psql(username, name, email):
    xtoken=uuid.uuid4()
    suuid=str(xtoken)
    cur = conn.cursor()
    cur.execute("insert into signup(username,name,email,x_api_key) values('{}','{}','{}','{}')".format(username, name, email,suuid))
    #robject.incr('insert_table')
    return "success"


def post_new(user_id, descreption):
    insert_newpost_to_celery(user_id, descreption)
    #robject.incr('post_feed')
    return "success"


def get_feed():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from fb_feed;")
    results = cur.fetchall()
    #robject.incr('get_post')
    return results


def del_post(postno):
    cur = conn.cursor()
    cur.execute("delete from fb_feed where post_id ={}".format(postno))
    #robject.incr('delete_post')
    return "successfully deleted"


def update(postno, descreption):
    cur = conn.cursor()
    cur.execute("update fb_feed set descreption='{}' where post_id ={}".format(descreption,postno))
    #robject.incr('update_post')
    return "successfully updated"
