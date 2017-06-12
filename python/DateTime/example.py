def str2datetime(date_str, date_format='%Y-%m-%d %H:%M'):
    try:
        return datetime.datetime.strptime(date_str, date_format)
    except ValueError:
        return None

def time_to_str(t):
    return t.strftime('%Y-%m-%d %H:%M')

