import datetime

timestamp = 133156044005003774
time_offset = datetime.datetime(1601, 1, 1)
time_delta = datetime.timedelta(seconds=timestamp/10000000)

result = time_offset + time_delta

print(result.strftime('%Y-%m-%d %H:%M:%S'))

