### 运行环境
- Python 3.7.6
- Scrapy 1.8.0

### 已完成的网站
- 网易新闻

### 运行
#### 运行某个爬虫
```
git clone https://github.com/zouyi9807/News-spider.git
cd News-spider/
pip install -r requirements.txt
scrapy crawl 163news
```
#### 运行脚本
或者你也可以通过运行爬虫项目目录下的 run.sh 或者 run.py 来启动所有爬虫，爬取的数据存储在该目录下
```
pip install -r requirements.txt
python run.py / sh run.sh
```
