from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(len(query_channel_list))
query_channel_list = [...]
# pool.map(function, (argment_list)) 
pool.map(grab_news_for_one_channel, (query_channel_list))
pool.close()
pool.join()

def grab_news_for_one_channel(channel_id):
    pass
