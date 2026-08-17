import datetime

print (datetime.datetime.now())

def days_since_epoch():
    current = datetime.datetime.now()
    epoch = datetime.datetime(1970, 1, 1)

    days = (current - epoch).days
    return days

print ((days_since_epoch()) , "days since the epoch")
