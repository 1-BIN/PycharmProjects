from datetime import datetime
import re
now = str(datetime.now())
onum = int(re.sub("[^0-9]+", '', now))
print(now)
print(onum)