import pymongo
from pymongo import *

raw_click_info_collection = None
def init_mongo():
    global raw_click_info_collection
    # client = MongoClient('hostname', port)
    client = MongoClient('127.0.0.1', 27017)
    # client.database_name.authenticate('username', 'passport')
    client.mp_recom_stat.authenticate('username', 'passport')
    # use mp_recom_stat
    mp_recom_stat_db = client['mp_recom_stat']
    # colletion=table
    raw_click_info_collection = mp_recom_stat_db['raw_click_info']


def get_click_info(mp_id, start_time, end_time, pre='', category='all'):
    if raw_click_info_collection == None:
        init_mongo()
    start_time_int = Tool.changeTimeToInt(start_time)
    end_time_int = Tool.changeTimeToInt(end_time)
    # data = [dict1, dict2...]
    data = raw_click_info_collection.find({
        'news_id': int(mp_id),
        'mark_time': {
            "$gte": start_time_int,
            "$lt": end_time_int
        }
    })
    pv = 0
    ev = 0
    if category == 'all':
        for row in data:
            pv += row['pv']
            ev += row['ev']
    else:
        for row in data:
            pv += row[category]['pc_pv']
            ev += row[category]['pc_ev']
    mp_info = {}
    mp_info[pre + 'pv'] = pv
    mp_info[pre + 'ev'] = ev
    return mp_info
