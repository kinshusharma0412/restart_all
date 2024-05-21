import requests, os, time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
from pyrogram.methods.utilities.idle import idle


headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  'x-csrf-token': os.environ["xcsrftoken"],
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://share.streamlit.io",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://share.streamlit.io/",
  'accept-language': "en-IN,en;q=0.9,en-US;q=0.8,hi;q=0.7",
  'priority': "u=1, i",
  'Cookie': os.environ["cookies_header"]
}
def all_restart_hibernation(x):
	url = "https://share.streamlit.io/api/v1/apps"
	params = {
	  'workspace_name': "kinshusharma0412"
	}
	response = requests.get(url, params=params, headers=headers)
	app_=response.json()['apps']
	app_1=[]
	for x in app_:
		if x['appId']!='1e9c1a5d-3cb7-4434-aff7-5a3ab1b6c13c':
			if x['status'] not in [5,6]:
				app_1.append(x)
	for x in app_:
		if x['appId']=='1e9c1a5d-3cb7-4434-aff7-5a3ab1b6c13c':
			if x['status'] not in [5,6]:
				app_1.append(x)
	
	for app_id in app_1:
		url = "https://share.streamlit.io/api/v2/apps/"+str(app_id['appId'])+"/restart"
		response = requests.post(url, headers=headers)
		print(app_1)
		print(response.text)

def hibernation(x):
	url = "https://share.streamlit.io/api/v2/apps/"+str(x)+"/restart"
	response = requests.post(url, headers=headers)
	print(response.text)

print(scheduler.add_job(all_restart_hibernation, 'interval', minutes=5,args=("x",)))
def main():
	scheduler.start()
	idle()
if __name__ == '__main__':
    main()#