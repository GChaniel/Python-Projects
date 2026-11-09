
from datetime import datetime, timedelta

current_time = datetime.now()
one_day_ago = current_time - timedelta(hours=24)

print(current_time)
print(one_day_ago)
