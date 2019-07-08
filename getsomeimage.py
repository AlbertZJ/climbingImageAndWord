'''
Created on 2019年3月15日

@author: AlbertZJ
'''
import re
import urllib.request
 
# ------ 获取网页内所有图片链接的方法 ------
def get_img(html):
    reg = r'src="(http\S*.jpg)"'
    imgre = re.compile(reg);
    imagelist = re.findall(imgre, html)
    return imagelist

def main():
    page = urllib.request.urlopen(r'https://sh.qihoo.com/9c840ec8012e0e457?djsource=ZF90WY&refer_scene=0&scene=1&sign=360dh&tj_url=9c840ec8012e0e457&uid=f455e4410d8f067da17ae1df56524a0c')
    html = page.read()
    html = html.decode('UTF-8')
    imageList = get_img(html)    
    for imagePath in imageList:
        path = 'F://image//' + imagePath.split('/')[-1]
        f = open(path, 'wb')  #可写，二进制      
        try:
            page = urllib.request.urlopen(imagePath)
            data = page.read()          
            f.write(data)
            print("下载的图片地址为："+imagePath)             
        except Exception as e:             
            print(imagePath+" 错误！不能得到正确的图片")            
        finally:
            print("图片存放在f:\\image\\下")
            f.close()        
    print("下载完成!")   
     
if __name__=="__main__":
    main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 