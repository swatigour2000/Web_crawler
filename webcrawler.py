import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    def crawl():
        url="https://www.healthline.com/health/skin-disorders"
        sources=requests.get(url)
        cleared_sources=sources.text
        soup=BeautifulSoup(cleared_sources,features="lxml")
        d=0
        l1=[]
        l2=[]
        l3=[]
        obj=soup.find('div',{'class':'css-0'})
        for link in obj.findAll('h3'):
            name=link.get_text()
            print(name)
            l1.append(name)
    
        for data in obj.findAll('ul'):
            about=data.get_text()
            print(about+'\n\n')
            l2.append(about)

        for link in obj.findAll('a',{'class':'content-link css-5r4717'}):
            href=link.get('href')
            href="https://www.healthline.com/health/skin-disorders"+href
            print(href)
            l3.append(href)
        i=0
        write_file=open('link.csv','w')
        while i<len(l1):
            row=str(l1[i])+","+str(l2[i])+","+str(l3[i])
            write_file.write(row+"\n")
            i+=1


crawl()







