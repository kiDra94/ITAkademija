from ftplib import FTP
ftp = FTP('speedtest4.tele2.net')
ftp.login('anonymous','')                     
ftp.cwd('upload')
to_upload = open('ftpexample.py','rb') # file to send
ftp.storbinary('STOR ftpexample.py', to_upload) # send the file
to_upload.close()
ftp.close()