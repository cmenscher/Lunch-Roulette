import smtplib
import os, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def write_file(dir, filename, from_addr, data):
  if(os.path.isdir(dir) == 0):
    os.mkdir(dir)
  os.chdir(dir)
  fd = open(filename, "w")  
  fd.write(data)
  fd.close()

def error(reason):
  sys.stderr.write('%s\n' % reason)
  sys.exit(1)

#sendMail("smtp.gmail.com", "lunchroul@gmail.com", "betawork$", 587, ["lunchroul@gmail.com"], lunchroul@gmail.com, subj, body,["/path/to/file/include"])
def sendMail(smtpserver, smtpuser, smtppass, port, to, fro, subject, text="", html="", files=""):
    assert type(to)==list
    
    msg = MIMEMultipart('alternative')
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    
    if(html == ""):
        msg.attach( MIMEText(text) )
        part = MIMEBase('application', "octet-stream")
        #part.set_payload( open(filename,"rb").read() )
        #Encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filetitle))
        if(files != ""):
            try:
                filename = str(files["filename"]).strip()
                filetitle = str(files["title"]).strip()
                if(filetitle == ""):
                  filetitle = os.path.basename(filename)
                filetitle = filetitle + "." + str(files["type"]).lower()
                print "ACTION: Preparing attachment filename=\"" + str(filename) + "\" filetitle=\"" + filetitle + "\""
                part.set_payload( open(filename,"rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % filetitle)
                msg.attach(part)
            except:
                part.set_payload( open(file,"rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
                msg.attach(part)
        
    else: #not gonna deal with file attachments in an HTML email...
        if text == "":
            text = html #if we didn't pass a text version just punt and make it html, too
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)

    smtp = smtplib.SMTP(smtpserver, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(smtpuser, smtppass)
    smtp.sendmail(fro, to, msg.as_string() )
    smtp.close()
    return 1
