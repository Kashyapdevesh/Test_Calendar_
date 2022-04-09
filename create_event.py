from datetime import datetime, timedelta
from cal_setup import get_calendar_service

exam_name=["EM-1","EM-2","EM-3","DL-1","DL-2","COA-1","COA-2","CN-1","CN-2","TOC-1","TOC-2",
"OS-1","OS-2","ALGO-1","ALGO-2","DB-1","DB-2","CD","PDS-1","PDS-2","VA","QA","AA"] 

def create_event(service,start,end,test):
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": "Test "+str(test)+" : "+str(exam_name[test-1]),
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
           "colorId":"5",
       }
   ).execute()	
   return event_result
  
def test_gen(d,test,service):
	while True:
		if test == 24:
			print("calendar over")
			break
		else:
			next_test = datetime(d.year, d.month, d.day, 18)+timedelta(days=3)
			start = next_test.isoformat()
			end = (next_test + timedelta(hours=1)).isoformat()
			create_event(service,start,end,test)
			print("event created at "+str(next_test)+" for test " +str(test))
			d=next_test
			test+=1
   


if __name__ == '__main__':
	d = datetime.strptime('Apr 12 2022', '%b %d %Y')
	service = get_calendar_service()
	test_gen(d,1,service)
