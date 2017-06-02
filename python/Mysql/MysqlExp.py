sql = "select * from mp_news_update_record where recom_time > '%s' and " \
      "recom_time < '%s' and channel_id < 45 order by channel_id asc"

def openDB():
    global recommend_record_db, cursor
    conn = MySQLdb.connect("*.*.*.*", "username", "password", "database")
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    recommend_record_db = conn

def query():
    cursor.execute(sql % (startDate, endDate))
    results = cursor.fetchall()
    for row in results:
        print row

