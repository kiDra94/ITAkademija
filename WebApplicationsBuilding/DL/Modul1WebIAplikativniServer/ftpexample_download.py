from ftplib import FTP
ftp = FTP('speedtest4.tele2.net')
ftp.login('anonymous','')                     
local_filename = open('1KB.zip', "wb")
ftp.retrbinary("RETR {}".format('1KB.zip'), local_filename.write)
local_filename.close()
ftp.close()