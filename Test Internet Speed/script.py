'''
Test Internet Speed with Python
Author: Ayushi Rawat
            
'''

#import the necessary module!
import speedtest 

st = speedtest.Speedtest() 

#fetch the download speed
download = st.download()

#fetch the upload speed 
upload = st.upload()

#display the result
print("Your Download speed is", download) 
print("Your Upload speed is", upload) 

#fetch the ping
st.get_servers([])

ping = st.results.ping

#display the result
print("Your Ping is", ping) 
