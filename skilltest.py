import urllib
import csv
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text 	  import MIMEText
from email.MIMEImage 	  import MIMEImage

# We start as usual, retrieving a file with urllib
openSite = urllib.urlretrieve("https://docs.google.com/spreadsheets/d/1ePmQ_yWo1hpDZ9yHH9IXlMPS4Lf9Y1y-wEQt0ZuLjAg/export?format=csv&id", "/home/erick/supply.csv")

me           = "supplies@somecompany"
you          = "employee@somecompany.com"
emptyVals 	 = ['0', 'None', 'none', 'out', 'zero', 'Zero']
resupplyList = list()
commentsList = list()

with open('supply.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[1] == row[2] or row[1] in emptyVals:
			resupplyList.append(row[0])
			if row[4] != '':
				commentsList.append(row[4])

resupplyString = '<br />'.join( supply  for supply  in resupplyList)
commentsString = '<br />'.join( comment for comment in commentsList)

msg = MIMEMultipart('alternative')
msg['Subject'] = "Supply report"
msg['From']    = me
msg['To']      = you

text = "Hi!\nHow are you?\nHere is the supply list you wanted:\n\n" + resupplyString
html = """\
<html>
	<head>
		<title>Supplies</title>
	</head>
	<body style='margin: 0; padding: 0;'>
		<table border = '0' cellpadding='0' cellspacing='0' width='100%%'>
			<tr>
				<td style='padding: 20px 0 30px 0;'>
					<table align='center' border = '0' cellpadding='0' cellspacing='0' width='600' style='border-collapse: collapse; border: 1px solid #cccccc;'>
						<tr>
							<td align='center' bgcolor='#FD6A4C' style='padding: 40px 0 30px 0;'> 
								<img src='cid:image1' width='300' height='150' style='display: block;' />
							</td>
						</tr>
						<tr>
							<td bgcolor='#ffffff' style='padding: 40px 30px 40px 30px;'>
	 							<table border='0' cellpadding='0' cellspacing='0' width='100%%'>
	  								<tr>
	   									<td style='color: #153643; font-family: Arial, sans-serif; font-size: 24px;'>
								    		<b>Here is your weekly supplies report!</b>
								  		</td>
									</tr>
									<tr>
								   		<td style='padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;'>
								    		Hey! This is your weekly supplies report. If there is any trouble with it please let erick@thetemplateofdoom.com know! He <em>might</em> be able to fix it.  
								   		</td>
								  	</tr>
								  	<tr>
								   		<td style='padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;'>
								    		<table border='0' cellpadding='0' cellspacing='0' width='100%%'>
											 <tr>
											  <td width='260' valign='top'>
											   <table border='0' cellpadding='0' cellspacing='0' width='100%%'>
											    <tr>
											     <td>
											      <img src='cid:image2' width='75' height='75' style='display: block;' border='0'/>
											     </td>
											    </tr>
											    <tr>
											     <td style='padding: 25px 0 0 0;'>
											      %s
											     </td>
											    </tr>
											   </table>
											  </td>
											  <td style='font-size: 0; line-height: 0;' width='20'>
											   &nbsp;
											  </td>
											  <td width='260' valign='top'>
											   <table border='0' cellpadding='0' cellspacing='0' width='100%%'>
											    <tr>
											     <td>
											      <img src='cid:image3' width='75' height='75' style='display: block;' border='0'/>
											     </td>
											    </tr>
											    <tr>
											     <td style='padding: 25px 0 0 0;'>
											      %s
											     </td>
											    </tr>
											   </table>
											  </td>
											 </tr>
											</table>
								   		</td>
								  	</tr>
								 </table>
							</td>
						</tr>
						<tr>
							<td align='center' bgcolor='#64BDAE' style='padding: 30px 30px 30px 30px;'>
								<table border='0' cellpadding='0' cellspacing='0' width='100%%'>
									<tr>
								  		<td width='75%%' style='color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;'>
								   			Social media links for fun!
								  		</td>
								  		<td align='right'>
								   			<table border='0' cellpadding='0' cellspacing='0'>
											  	<tr>
											   		<td>
											    		<a href='http://www.twitter.com/'>
											     			<img src='cid:image4' alt='Twitter' width='38' height='38' style='display: block;' border='0' />
											    		</a>
											   		</td>
											   		<td style='font-size: 0; line-height: 0;' width='20'>&nbsp;</td>
											   		<td>
											    		<a href='http://www.twitter.com/'>
											     			<img src='cid:image5' alt='Facebook' width='38' height='38' style='display: block;' border='0' />
											    		</a>
											   		</td>
											  	</tr>
											</table>
								  		</td>
								 	</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
		</table>
	</body>
</html>
""" % (resupplyString, commentsString)

fp = open('neslogo.gif', 		 'rb')
msgImage1 = MIMEImage(fp.read())
fp.close()

fp = file('paperclip.png', 		 'rb')
msgImage2 = MIMEImage(fp.read())
fp.close()

fp = file('idea.png', 			 'rb')
msgImage3 = MIMEImage(fp.read())
fp.close()

fp = file('social-twitter.png',  'rb')
msgImage4 = MIMEImage(fp.read())
fp.close()

fp = file('social-facebook.png', 'rb')
msgImage5 = MIMEImage(fp.read())
fp.close()

msgImage1.add_header('Content-ID', '<image1>')
msg.attach(msgImage1)

msgImage2.add_header('Content-ID', '<image2>')
msg.attach(msgImage2)

msgImage3.add_header('Content-ID', '<image3>')
msg.attach(msgImage3)

msgImage4.add_header('Content-ID', '<image4>')
msg.attach(msgImage4)

msgImage5.add_header('Content-ID', '<image5>')
msg.attach(msgImage5)

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html' )

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(me, you, msg.as_string())
s.quit()
