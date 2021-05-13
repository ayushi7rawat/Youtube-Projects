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

#converting into mbps
download = download/1000000
upload = upload/1000000

#display the result
print("Your Download speed is", round(download, 3), 'Mbps')
print("Your Upload speed is", round(upload, 3), 'Mbps')

#fetch the ping
st.get_servers([])

ping = st.results.ping

#display the result
print("Your Ping is", ping) 
