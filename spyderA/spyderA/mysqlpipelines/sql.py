import mysql.connector
from spyderA import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:

    @classmethod
    def insert_title_author(cls, title, author):
        sql = 'INSERT INTO title_author (`title`, `author`) VALUES (%(title)s, %(author)s)'
        value = {
            'title': title,
            'author': author
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_title(cls, title):
        sql = "SELECT EXISTS(SELECT 1 FROM title_author WHERE title=%(title)s)"
        value = {
            'title': title
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

