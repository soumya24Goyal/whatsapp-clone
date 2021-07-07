
from pyrebase import pyrebase
from .views import *
Config = {
    "apiKey": "apikey",
    "authDomain": "chatapp",
    "projectId": "project-id",
    "databaseURL":"databaseurl",
    "storageBucket": "storageBucket",
    "messagingSenderId": "senderid",
    "appId": "appid",
    "measurementId": "id"
}

firebase = pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()

def Createchat(cn,usr,chatid):
    chat1=db.child("List").child(cn.id).get()
    chat2=db.child("List").child(usr.id).get()
    if (chat1.val()) is None:
        db.child("List").child(cn.id).set({chatid[0]:{'Name':usr.username ,
                                                       'Last message':'you are connected'
                                                        }})
    else:
        db.child("List").child(cn.id).update({chatid[0]:{"Name":usr.username,
                                                         "Last message":'you are connected'
                                                         }})

    if(chat2.val()) is None:
        db.child("List").child(usr.id).set({chatid[0]:{'Name':cn.username ,
                                                       'Last message':'you are connected'
                                                        }})
    else:
        db.child("List").child(usr.id).update({chatid[0]:{"Name":cn.username,
                                                         "Last message":'you can now chat'
                                                         }})




















    
    
    
 
 