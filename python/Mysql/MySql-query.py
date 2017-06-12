mysql_database_name = None
cursor = None

def init_mysql(database):
    global cursor
    conn = None
    if database == 'localhost':
        conn = MySQLdb.connect("127.0.0.1", "username", "passport", "database-name", charset='utf8')
    elif database == 'host1':
        conn = MySQLdb.connect("host1", "username", "passport", "database-name", charset='utf8')
    elif database == 'host2':
        conn = MySQLdb.connect("host2", "username", "passport", "database-name", charset='utf8')
    if conn is not None:
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    else:
        raise Exception("no database set", database)


def get_data_from_db(sql, multi=True, database='localhost'):
    global mysql_database_name
    if cursor is None or (mysql_database_name is not None and mysql_database_name != database):
        mysql_database_name = database
        init_mysql(database)
    try:
        cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
        init_mysql(database)
        cursor.execute(sql)
    if multi:
        # results = [dict1, dict2...]
        results = cursor.fetchall()
    else:
        # results = dict2
        results = cursor.fetchone()
    return results
