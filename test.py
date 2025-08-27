import httpx
import pytz

from datetime import datetime, timedelta
def check_exist(id):
    headers = {"Content-Type": "application/json"}
    url = 'https://elr1c.ru/api/inbounds_list'

    params = {
        "id": id
    }

    response = httpx.get(url, params=params, headers=headers)

    print(response.status_code)
    try:
        return {"exist_status":response.json()['result'][0]['feedback'], 'expiryTime':response.json()['result'][0]['clients'][0]['expiryTime']}
    except Exception:
        return {"exist_status": response.json()['result'][0]['feedback']}

print(check_exist(7026677811))

def get_timestamp_week_ahead():
    tehran_tz = pytz.timezone("Asia/Tehran")
    expirytimedate = 0
    current_date_tehran = datetime.now(tehran_tz)
    new_date_tehran = current_date_tehran + timedelta(days=expirytimedate)
    return int(new_date_tehran.timestamp() * 1000)
print(get_timestamp_week_ahead())