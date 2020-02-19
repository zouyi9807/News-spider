import datetime
from scrapy import cmdline

date = str(datetime.date.today())
command = "scrapy crawl 163news -o 网易新闻" + date + ".csv"
print(command)
cmdline.execute(command.split())
