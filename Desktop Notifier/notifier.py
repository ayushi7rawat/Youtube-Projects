'''
Desktop Notifier in Python
Author: Ayushi Rawat
'''

#import the necessary module!
from plyer import notification


#specify the parameters
title = 'Hello Amazing people!'

message= 'Thankyou for reading! Take care!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)