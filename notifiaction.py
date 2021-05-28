from notify_run import Notify 

notify = Notify()
def Send_notification_Android(msg):
    print("sending notification as -"+msg)
    notify.send(msg) 
    