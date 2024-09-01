import time
from datetime import datetime, timedelta
import pytz
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Maksim:oThorOn3ytRWcJG6@cluster0.ypb3r.mongodb.net/myFirstDatabase?retryWrites=true&authSource=the_database&authMechanism=SCRAM-SHA-1")
db = cluster["basa"] #котегрия
vks = db["vks"] #роздел
adm = db["adm"] #роздел
tovar = db["tovar"] #роздел
users = db['users'] #роздел
oplata = db['oplata'] #
now = datetime.now() 

moscw_time = datetime.now(pytz.timezone('Europe/Moscow'))
curren_time = moscw_time.strftime("%d-%m-%Y %H:%M")
print(curren_time)

tomorrow_date = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y %H:%M")
print(tomorrow_date)



#Запускаем цикл для проверки времени
while True:
  moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
  current_time = moscow_time.strftime("%H:%M")
  time.sleep(5)
  print(current_time)
  if current_time == '00:00':
#8484847847474848

      ck = 0
      for i in users.find():
          ck += 1

      nehj = adm.find_one({"ik": 33})["prosh"]
      print(ck)
      jok = ck - nehj
      adm.update_one({"ik": 33}, {"$set": {"denpol": jok}})
      adm.update_one({"ik": 33}, {"$set": {"prosh": ck}})
#7773737377474747
      jk = adm.find_one({"ik": 33})["vsegotov"] + adm.find_one({"ik": 33})["dentov"]
      adm.update_one({"ik": 33}, {"$set": {"vsegotov": jk}})

#78777777777
      jg = adm.find_one({"ik": 33})["vsegoprib"] + adm.find_one({"ik": 33})["denprib"]
      adm.update_one({"ik": 33}, {"$set": {"vsegoprib": jg}})

#7767(-+)
      moscw_time = datetime.now(pytz.timezone('Europe/Moscow'))
      curren_time = moscw_time.strftime("%d-%m-%Y %H:%M")
      adm.update_one({"ik": 33}, {"$set": {"obnovaposled": curren_time}})
    #75766776


      jlk = adm.find_one({"ik": 33})["nedtov"] + adm.find_one({"ik": 33})["dentov"]
      adm.update_one({"ik": 33}, {"$set": {"nedtov": jlk}})
      adm.update_one({"ik": 33}, {"$set": {"dentov": 0}})
    #848484884
      jlkg = adm.find_one({"ik": 33})["nedpol"] + adm.find_one({"ik": 33})["denpol"]
      adm.update_one({"ik": 33}, {"$set": {"nedpol": jlkg}})
      adm.update_one({"ik": 33}, {"$set": {"denpol": 0}})
#78777777777
      jgl = adm.find_one({"ik": 33})["nedprib"] + adm.find_one({"ik": 33})["denprib"]
      adm.update_one({"ik": 33}, {"$set": {"nedprib": jgl}})
      adm.update_one({"ik": 33}, {"$set": {"denprib": 0}})

      time.sleep(60)

  elif moscow_time.strftime("%d-%m-%Y %H:%M") == adm.find_one({"ik": 33})["nekstmned"]:
      obnk = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y %H:%M")
      adm.update_one({"ik": 33}, {"$set": {"nekstmned": obnk}})

      adm.update_one({"ik": 33}, {"$set": {"nedtov": 0}})

      adm.update_one({"ik": 33}, {"$set": {"nedpol": 0}})

      adm.update_one({"ik": 33}, {"$set": {"nedprib": 0}})



  else:
      print("+")

