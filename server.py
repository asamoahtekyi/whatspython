import gifecemailstaff, gifecemailrtp
import time


while True:
    try:
        gifecemailstaff.print_me()
        gifecemailstaff.run()
        gifecemailrtp.print_me()
        gifecemailrtp.run()
    except Exception as e:
        print(e)
    time.sleep(30)


#while True:
 #   try:
  #      gifecemail.send_email
   # except Exception as e:
    #    print(e)
    #time.sleep(60)