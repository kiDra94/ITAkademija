from ftplib import FTP
ftp = FTP('speedtest4.tele2.net')
ftp.login('anonymous','')                     
ftp.dir()
ftp.cwd('upload')
print('Content of folder: upload')
ftp.dir()
ftp.close()