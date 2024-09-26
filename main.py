import requests,re,json, os, time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
import asyncio



def all_restart_hibernation(x):
	r=requests.session()
	url = "https://share.streamlit.io/api/v1/apps"
	params = {
	  'workspace_name': "kinshusharma0412"
	}
	r.headers.update({
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
  'Content-Type': "application/json",})
	r.cookies.update({"streamlit_session":os.environ["cookies_header"]})
	response = r.get(url, params=params)
	if "x-csrf-token" in response.headers:
		r.headers.update({"x-csrf-token":response.headers["x-csrf-token"]})
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
		response = r.post(url)
		print(app_1)
		print(response.text)

def hibernation(x):
	url = "https://share.streamlit.io/api/v2/apps/"+str(x)+"/restart"
	response = requests.post(url, headers=headers)
	print(response.status_code)

print(scheduler.add_job(all_restart_hibernation, 'interval', minutes=5,args=("x",)))

async def main():
    scheduler.start()
    while True:
        #await asyncio.create_task(bar())
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    loop.run_forever()
