import urllib.request as urq
import urllib.parse as uParse
import datetime
import json

class naverSearch(object):
    def __init__(self):
        print('Naver Search API 생성')
    
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', 'yKF9rEswoZYk_TNFiMLJ')
        req.add_header('X-Naver-Client-Secret', 'IYqDP_uprs')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: #ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
            else:
                print('fail')
        except Exception as e:
            print(e)
            return None


    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uParse.quote(search_word))
        url = base + node + param 
        returnData = self.getRequestUrl(url)
        if returnData == None:
            return None
        else:
            return json.loads(returnData)


    def getPostData(self, post, jsonResult):
        title = post['title']
        desc = post['description']
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S')
    