
# Python 3.8.0
import imaplib
import email
import traceback
import datetime
import requests
from bs4 import BeautifulSoup
import time
import rvon
import rvon2
#from keep_alive import keep_alive

#keep_alive()

headers = {
    'authority': 'airhub.airstream.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
}

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
#ORG_EMAIL = "@gmail.com"
#FROM_EMAIL = "Ryan@airstreamcharlotte.com" + ORG_EMAIL
#kaduray03@gmail.com -- isbqknvpl
FROM_EMAIL = "Ryan@airstreamcharlotte.com"
FROM_PWD = "kxjteqegjeqlvhyq"
SMTP_SERVER = "imap.gmail.com"

#FROM_EMAIL = "kaduray02@gmail.com"
#FROM_PWD = "piuhpuiwjchunsht"
SMTP_SERVER = "imap.gmail.com"


SMTP_PORT = 993

success_found = 0
def parse(text,lead):
    global success_found
    soup = BeautifulSoup(text,'html.parser')
    dismis = soup.find(class_='alert alert-danger alert-dismissible flash-message')
    succes = soup.find(class_='alert alert-success alert-dismissible flash-message')

    if dismis != None:
        dismis = dismis.text.replace('\n','').strip()
    else:
        dismis = ''

    if succes != None:
        succes = succes.text.replace('\n','').strip()
        success_found += 1
    else:
        succes = ''

    print('Lead : ' + lead[:81])
    print('Dismiss : ' + dismis)
    print('Success : ' + succes)
    #print('------------------------------------------------------------------------------------------------')


def read_email_from_gmail():

    test = 0
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

         # Calculate the date for 24 hours ago from the current date
        last_24h_date = (datetime.datetime.now() - datetime.timedelta(hours=48)).strftime("%d-%b-%Y")
        #print(last_24h_date)

        data = mail.search(None, f'(SINCE "{last_24h_date}")')
        #data = mail.search(None,  'ALL')
        mail_ids = data[1]

        id_list = mail_ids[0].split()

        if not id_list:
            #print("No unseen emails in the last 24 hours.")
            return

        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1], 'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    lead = ''

                    print('------------------------------------------------------------------------------------------------')
                    #print('New Website Lead - 2023-07-22 11:23:11')
                    print('From : ' + email_from)
                    print('Subject : ' + email_subject)

                    #user = input('>')
                    #user = 'y'
                    #if user == 'y':
                        #try:
                        #    driver.close()
                        #except:
                    #    pass
                    #else:
                    #    continue

                    # Check if the email contains a text/html part
                    if msg.is_multipart():
                        for part in msg.walk():
                            string = part.as_string()

                            if 'Accept Lead' in string:
                                string = str(string.replace('=\n',''))
                                soup = BeautifulSoup(string,'html.parser')
                                #print(soup.prettify())
                                a_tags = soup.find_all('a')

                                for tag in a_tags:

                                    try:
                                        a_text = tag.text
                                    except:
                                        continue

                                    if 'Accept Lead' in a_text:

                                        try:
                                            lead = tag.get('href')
                                            lead = lead.replace('3D"','').replace('"','')
                                            lead = lead.replace('=3D','=')
                                        except:
                                            pass

                                        break

                                break


                    if 'New Website Lead' in email_subject and 'AirHub' in email_from and lead != '':

                        trial = 0

                        while True:

                            if trial == 10:
                                break

                            try:
                                print(lead)
                                res = requests.Session().get(lead,headers=headers,timeout=10)
                                print(res.status_code)
                                if res.status_code == 200:
                                    parse(res.text,lead)
                                    break
                                
                                
                                trial += 1

                                time.sleep(1)

                            except Exception as E:
                                time.sleep(1)
                                trial += 1
                                continue

                        #mail.store(str(i), '+FLAGS', '\\Seen')
                        test += 1

                        #print('---------------------------------------------')

    except Exception as e:
        traceback.print_exc()
        print(str(e))


# Rest of your code...
if __name__ == '__main__':
    read_email_from_gmail()
    print('-------------------------------------------------------------------------------------')
    print('Total Success : ' + str(success_found))
    print('-------------------------------------------------------------------------------------')
    print('scrape rvon')
    getawayrvandmarine_class = rvon.getawayrvandmarine()
    getawayrvandmarine_class.call_xml()
    #getawayrvandmarine_class.saving()
    getawayrvandmarine_class.open_sheet()
    print('-------------------------------------------------------------------------------------')
    print('Total Success : ' + str(success_found))
    print('-------------------------------------------------------------------------------------')
    print('scrape rvon2')
    getawayrvandmarine_class = rvon2.getawayrvandmarine()
    getawayrvandmarine_class.call_xml()
    #getawayrvandmarine_class.saving()
    getawayrvandmarine_class.open_sheet()
    getawayrvandmarine_class.open_sheet2()
