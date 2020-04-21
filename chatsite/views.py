from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import os
from django.conf import settings


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# from .bot import agent

def home_view(request):
	return render(request, 'index.html')


@csrf_exempt
def webhook(request):
	print(request.POST)
	return JsonResponse({"status": "OK"})


#@csrf_exempt
#def handle_response(request, *args, **kwargs):
   # if request.method == "POST":
     #   try:
        #    print(request)
 	 #   print(request.POST.get('user_input'))
         #   message = request.POST.get('user_input')
         #  responses = agent.handle_message(message)		
         #   print(responses)
 	 #   bot_data = {
 	#		'status': 'OK',
 	#		'responses': responses[0]['text']
 	#		}
 	  # # return JsonResponse(bot_data)
 	#except Exception as e:
 	#    return JsonResponse({'status': 'FAILED'})

@csrf_exempt
def GetUPNAccountDetails(request,id):
	if request.method == "GET":
	   id=id

	   con = sqlite3.connect(os.path.join(settings.BASE_DIR, './rasachat/upnchat.db'))
	   cursorObj = con.cursor()
	   cursorObj.execute("SELECT * FROM UPN_account_information where id="+str(id))
	   row = dictfetchall(cursorObj)
	   con.commit()
	return render(request, "UPNAccounts.html",{"list":row[0]})
	

