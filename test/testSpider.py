from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3
from urllib import parse
from lxml import etree
'''
[['CARD9的巨噬细胞极化效应在慢性胰腺炎癌转化中的作用机制研究', '81960452', '2019', '消化系统肿瘤（H1617）', '钟晓鸣', '江西省肿瘤医院', '34万元', '地区科学基金项目', '2020年01月01日 至 2023年12月31日'],
'''

def main():
    savepath = 'CountryNature.xls'
    datalist = getData()
    saveData(datalist,savepath)
def askURL(url):
    head = {        #模拟浏览器头部信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.83Safari / 537.36"
    }

            #用户代理
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response =  urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)

        if hasattr(e,"reason"):
            print(e.reason)

    return  html

def getLink(html):
    linklist = []
    selector = etree.HTML(html)
    links = selector.xpath('//*[@id="jj_html"]/div/div[2]/div/div[2]/div/div/ul//a/@href')
    for s in links:
        linklist.append('http://fund.keyanzhiku.com/'+s)

    return linklist
def getData():
    datalist = []
    for j in range(1,10135):
        url = "http://fund.keyanzhiku.com/Index/index/start_year/0/end_year/0/xmid/0/search/1/px_year/desc/p/"+str(j)+".html"
        html = askURL(url)
        links = getLink(html)
        for i in links:
            nh = askURL(i)
            s1 = etree.HTML(nh)
            data = []
            try:
                projects = s1.xpath('/html/body/div[3]/div/div[2]/div/h2/text()')[0]
                data.append(projects)
                pnumber = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/text()')[0]  # [4:]
                data.append(pnumber[4:])
                pyear = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/text()')[0]  # [5:]
                data.append(pyear[5:])
                psort = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/text()')[0]  # [5:]
                data.append(psort[5:])
                pmaster = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]/div/text()')[0]  # [6:]
                data.append(pmaster[6:])
                plocation = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/text()')[0]  # [5:]
                data.append(plocation[5:])
                pmoney = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[3]/td[1]/div/text()')[0]  # [5:]
                data.append(pmoney[5:])
                pclass = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[3]/td[2]/div/text()')[0]  # [5:]
                data.append(pclass[5:])
                ptime = s1.xpath('/html/body/div[3]/div/div[2]/div/div/div/table/tbody/tr[3]/td[3]/div/text()')[0]  # [5:]
                data.append(ptime[5:])
                datalist.append(data)
            except  Exception as e:
                print(i)
                print(e)
                continue

    # print(datalist)
    return datalist
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建book对象
    sheet = book.add_sheet('CountryNature',cell_overwrite_ok=True)  # 创建工作表
    col = ('项目名','批准号','批准年度','学科分类','项目负责人','依托单位','资助金额','项目类别','研究期限')
    for i in range(0,9):
        sheet.write(0,i,col[i]) #列名
    for i in range(len(datalist)):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,9):
            sheet.write(i+1,j,data[j])
        book.save(savepath)


if __name__ == '__main__':
    main()