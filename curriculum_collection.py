from selenium import webdriver
import re
import requests
import time
import xlwt

wb = xlwt.Workbook(encoding = 'ascii')
ws = wb.add_sheet('get')
browser = webdriver.Chrome()

line = 0


url = "http://jxgl.hdu.edu.cn/jxrwcx.aspx?tdsourcetag=s_pcqq_aiomsg"

browser.get(url)
input()


'''前十页情况特殊处理'''
for i in range(0, 10) :
    r = browser.page_source
    #匹配td标签的内容
    tdList = re.findall(r'<td[^>]*>(.*?)</td>', r)
    select = browser.find_elements_by_css_selector("td")
    Lis = []
    #查找是否有title属性，有就覆盖tdList
    for k in range(0, len(select)) :
        Lis.append(select[k].get_attribute("title"))
    
    for k in range(0, 180) :
        tem = k % 12
        if tem == 0 :
            line += 1
        if Lis[k] == '' :
            ws.write(line, tem, label = tdList[k])
        else :
            ws.write(line, tem, label = Lis[k])

    #lis = tdList[0:180]
    #print(lis)
    plt = browser.find_elements_by_css_selector("a")
    plt[i].click()
    #time.sleep(3)
    #input()
    
'''整数页搜索，最后几页人工复制（懒）'''
for j in range(0, 30) :
    for i in range(1, 11) :
        r = browser.page_source
        tdList = re.findall(r'<td[^>]*>(.*?)</td>', r)
        select = browser.find_elements_by_css_selector("td")
        Lis = []
        for k in range(0, len(select)) :
            Lis.append(select[k].get_attribute("title"))

        #按行写入数据,180为1页数据总数
        for k in range(0, 180) :
            tem = k % 12
            if tem == 0 :
                line += 1
            if Lis[k] == '' :
                ws.write(line, tem, label = tdList[k])
            else :
                ws.write(line, tem, label = Lis[k])

        #lis = tdList[0:180]
        #print(lis)
        '''模拟翻页操作'''
        plt = browser.find_elements_by_css_selector("a")
        plt[i].click()
        #input()

print("The excel has been finished.")
wb.save('save.xls')
