import requests,time,json,os

class BaiduImgs(object):
	url  = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11097506508378431796&ipn=rj&ct=201326592&is=&fp=result&q" \
		   "ueryWord=%E7%82%B8%E9%B8%A1%E8%85%BF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={word}=&se=&tab=&width=&height=&face=&" \
		   "istype=&qc=&nc=1&fr=&expermode=&force=&".format(word='美女')
	pn = 30
	rn = 30
	param = "pn={pn}&rn={rn}".format(pn=pn,rn=rn)
	headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
	filePath = '/Users/zxg/Desktop/baiduImgs/'


	def run(self):
		self.start_requests()


	def get_url(self):
		self.param="pn={pn}&rn={rn}".format(pn=self.pn,rn=self.rn)
		url = self.url + self.param
		return url

	def start_requests(self):
		resp = requests.get(self.get_url(),headers=self.headers,allow_redirects=False)
		json_data = json.loads(resp.text)['data']
		self.parse_data(json_data)

	def parse_data(self,data):
		for img_data in data:
			try:
				print(img_data['thumbURL'])
				print(img_data['fromPageTitle'].replace('<strong>','').replace('</strong>',''))
				self.save_img(img_data['thumbURL'],img_data['fromPageTitle'].replace('<strong>','').replace('</strong>','')+'.jpg')
				time.sleep(1)
			except:
				pass
		self.pn+=30
		self.rn+=30
		self.start_requests()

	def save_img(self,url,fileName):
		resp = requests.get(url,headers=self.headers,allow_redirects=False)
		# print(resp.text)


		savePath =os.path.join(self.filePath,fileName)
		with open(savePath,'wb') as f:
			f.write(resp.content)
		print('######save done#########')





if __name__ == '__main__':
	a = BaiduImgs()
	a.run()
