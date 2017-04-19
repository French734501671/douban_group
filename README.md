# douban_group
利用cookie登录豆瓣，然后抓取豆瓣上所有小组，总共8个大类67个小类，9w左右个小组。<br>
cookie_str2dict.py 用于将浏览器上的cookie字符串转化为字典键值对 <br>
使用scrapy框架，用CrawlSpider 进行爬取 <br>
使用mongodb 存储数据 <br>
