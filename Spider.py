from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3
from urllib import parse
from lxml import etree
# 页面搜索路径：https://search.51job.com/list/010000,000000,0000,00,9,99,Java,2,1.html

# kw = input("请输入你要搜索的关键字：")
# kw = input('输入想要选择的职位：')
# keyword = parse.quote(parse.quote(kw))
# pageNum = 1

def main():
    kw = input('输入想要选择的职位：')
    keyword = parse.quote(parse.quote(kw))
    # savepath = 'java.xls'

    datalist = getData(keyword)
    # saveData(datalist,savepath)
    dbpath = "51job2.db"
    saveData2DB(datalist,dbpath)


def getLink(html):
    linklist = []
    # html = open(nhtml, "r")
    bs = BeautifulSoup(html, "html.parser")
    scr = str(bs.find_all('script'))
    # print(scr)
    findLink = re.compile(r'"job_href":"(.*?)",')
    links = re.findall(findLink, scr)
    for link in links:
        link = link.replace('\\', '')
        linklist.append(link)
        # print(link)

    return linklist
def askURL(url):
    head = {        #模拟浏览器头部信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.83Safari / 537.36"
    }

            #用户代理，告诉豆瓣服务器，我们是什么类型的机器，告诉浏览器我们可以接收什么水平的浏览器
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response =  urllib.request.urlopen(request)
        html = response.read().decode("gbk","ignore")
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)

        if hasattr(e,"reason"):
            print(e.reason)

    return  html

def getData(keyword):
    datalist = []
    for i in range(1,16):
        url = "https://search.51job.com/list/010000,000000,0000,00,9,99," + keyword + ",2," + str(i) + ".html"
        html = askURL(url)
        linklist = getLink(html)
        for s in linklist:
            # if s == 'http://h3c.51job.com/jobdes.html?jobid=120663783':
            #     continue
            # print(s)
            try:
                html = askURL(s)
                bs = BeautifulSoup(html, "html.parser")
                data = []
                jobName = bs.select("div.cn > h1")[0]['title']
                data.append(jobName)
                salary = bs.select('div.cn > strong')[0].text
                data.append(salary)
                location = bs.select('div.cn > p.cname > a.catn')[0]['title']
                data.append(location)
                if len(data) < 3:
                    data.append('暂无')
                datalist.append(data)
            except:
                print(s,'大概率是调到公司官网了所以定位不到元素')
            else:
                print(s,'正常捕获')
            # except:
            #     print('数组越界！!')



    print('数组长度为：',len(datalist))
    return datalist


def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建book对象
    sheet = book.add_sheet('51Job',cell_overwrite_ok=True)  # 创建工作表
    col = ('职位名称',"薪水","公司名称")
    for i in range(0,3):
        sheet.write(0,i,col[i]) #列名
    for i in range(len(datalist)):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,3):
            sheet.write(i+1,j,data[j])

        book.save(savepath)
def init_db(dbpath):
    sql = '''
        create table bigdata
        (
        id integer primary key autoincrement,
        jobname text,
        salary text,
        company text
        )
    '''    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
def saveData2DB(datalist,dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            # if index == 4 or index == 5:
            #     continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into bigdata (
                jobname,salary,company)
                values (%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()
if __name__ == "__main__":
    main()
    print("爬取完毕")
    # init_db('51job2.db')
    # askURL("https://jobs.51job.com/beijing-hdq/112159887.html?s=01&t=0")