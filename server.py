import gifecemail
import time


while True:
    try:
        gifecemail.print_me()
        gifecemail.run()
    except Exception as e:
        print(e)
    time.sleep(30)


#while True:
 #   try:
  #      gifecemail.send_email
   # except Exception as e:
    #    print(e)
    #time.sleep(60)