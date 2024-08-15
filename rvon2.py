import requests
from bs4 import BeautifulSoup
import pandas
import time
import gspread
import numpy as np
import datetime

# Set up time of running script 600 = 10 mins
seconds = 3000 

class getawayrvandmarine:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    creds = {
        "type": "service_account",
        "project_id": "crypto-messari",
        "private_key_id": "9cd2f9d784c4baaba89c4f5f8a565ac47d2b33ab",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCwQ2KpOgPnA7wv\nuBjzFYbkL8vmfuFlQ1e3j8IqG0Ikale7bWfc24E21cK4ZX1zeCbN5R4Rcb560q4L\nLTiLLvsfcZYyh+WCtdih//Jdg7LelwejNP8FemVy5eXvtaWJVLIVw7XDDLxA34dQ\nXrtTECiiT4cZ4S+m/Pt7m6h8e1f3ddrKbAjr91vq6gWlY0x5bIJwvjoc8jkcKzpj\ndQ6VBa6SHjQ2X4qUUEzxflpDh+qbgXm208VBr/sMfwtzueL+F9NmvJ3jSkF/Ahjl\nSNPuKXY6TbwqS+oaPf7mFQRsvXTJ0o7skVLqsoOEsAYd1DDV12usKZaQV35CUh/p\nmSvG9+k5AgMBAAECggEALQO4kaFIV9ojWEh6zrHDtkjimOX0aCkPoMhs/NXjSWuD\nJlGlgcjpMfjbdr4skK2xs0l9KVVUIQfm/OG6nAkOhxQ6GIOOQJhyT8UOv4UfzCrj\n/3FMY7jDadl+pH5OXUktBdPqenqpJSQw6XyX+Hma9wC6bwiMY+gdzY6OM+RILeEV\nc58YvulFxSHAwmb5voh5SEalnnC4G3dO3qOwBaMRzNmEpSs9OIDWQ4/BKCrvViyI\ntcpHgCt/d9AtiU61k1GxJzFiiJt/Pu5abmfnvQhZcLrhG9rkoO4dZ1zvbKKYUzgk\nZkw3Yt1Xk3y34S5rl42XsVOmNAeaRkIy/ZoqDTLZ9QKBgQDm5mWV3Awb5iJjj3C5\n/jigoxLWuBiHkBEQg7krjnStBaAOms1fIWBUP6mw5cBH+BM17uij8c1eqRT3HVwZ\n0j+qQKbd65erMtlmOYucUJSbWcX/kEXIfXEYP+hAmSTAuir8Eqgtu0V7jgpa5ffH\npweCn9Pf1lzckKwqhCT709IrxwKBgQDDbIdamsk85GgZcvaXuEYptg3sVTKsksuV\n7+hymV7sC2zDgegvdde3aFX1VwxlXPdvqJvdWPSWran2lI3Mz6eTPWMSlBPt+tLq\nXYNWSKzQ06WE+eVUmE61WDVw0x8+Jr5aubg8OA6DhdLI6IDqvFp7v4QNB0EvVPsu\nWCT6OgNC/wKBgAFfwZ8ArjnERtQc2Gji8GdUURpiAhNcch2NCx8NO/iDng44MZyt\nUCtwLYxV8az79vFNOKkxGS3FB9DopdGphKN4uwV7D23/YXfQQ9psSFYcVKdOrnug\n83lXeARaZPOYqATT/5g2ExXHJJyh3bWcctj+Jn6ggfD2E3A1VRsCia+lAoGACmUV\ndg5Rsfl8SA5Da6KTqNhUOUP25BMS3TDbrmzWDbw11thsH0onZUwZdmlg8WtWhgvz\n7nwy1mj6Z3FTcZeCFGTphi12Oexjl6/NsqM+/gSkA0S/nBZV6XN9tDimqsmoym6i\njCF3NCvEIIetg87tCTQQtBi0sO3WRorNvLmlPsUCgYAtSEFVqcTe6D6c6mNjyfhX\nrMJ2tR3l9q37C2k4GtXdx1LFeoNusEOyMU7GMTUL5gd7q571IW92mow5U04GmsXp\n2DfA41nVUT7sqnkVCoFt6LQDS+s/5v5KnxNZ23ZEul5Qbygfx9PQaZ/TuyaxZ6+S\nhJrcuKgiWaFyED4Lni/XsQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "pythoncryptomessariaccount@crypto-messari.iam.gserviceaccount.com",
        "client_id": "112559430258363988070",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pythoncryptomessariaccount%40crypto-messari.iam.gserviceaccount.com"
    }

    def __init__(self) -> None:
        #self.main_url = 'https://www.rvonedata.com/feed/export/data?accountId=543&token=7iSpt4FGgzhxwgCJ6egHGw&version=2&format=xml'
        self.main_url = 'https://www.rvonedata.com/feed/export/data?accountId=49&token=T9M1naRQ63lofhp9Mqsu2w&version=2&format=xml'
        self.save = []
        self.save2 = []
        self.count = 1

    def open_sheet(self):
        df = pandas.DataFrame(self.save)
        df = df.replace(np.NAN,'')
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        gc = gspread.service_account_from_dict(self.creds)
     
        spreed_sheet_id = '1JjMGLmpQ57Juefr0bxzEyjbgoP26psPo0XJj1ltc0Dk'
        sheet = gc.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('Sheet1')
        worksheet.batch_clear(["A1:EZ"])
        columns = df.columns.values.tolist()
        body = df.values.tolist()
        save = []
        save.append(columns)
        for item in body:
            #
            save.append(item)
        
        #pprint.pprint(save)
        worksheet.update(values=save, range_name='A1')
        print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(self.save)))
        
    def open_sheet2(self):
        df = pandas.DataFrame(self.save2)
        df = df.replace(np.NAN,'')
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        gc = gspread.service_account_from_dict(self.creds)
     
        spreed_sheet_id = '1vddgluqq8J4k2IW-dj6iLhL2ibypF8eaceBpScPDrME'
        sheet = gc.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('Sheet1')
        worksheet.batch_clear(["A1:EZ"])
        columns = df.columns.values.tolist()
        body = df.values.tolist()
        save = []
        save.append(columns)
        for item in body:
            #
            save.append(item)
        
        #pprint.pprint(save)
        worksheet.update(values=save, range_name='A1')
        print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(self.save)))
        

    def call_xml(self):

        while True:
            try:
                res = requests.get(self.main_url,timeout=15)
                if res.status_code == 200:
                    break
                print(res.status_code)
            except requests.exceptions.ConnectionError:
                print('ConnectionError')
                time.sleep(3)
                continue
            except requests.exceptions.Timeout:
                print('Timeout')
                time.sleep(3)
                continue
        

        soup = BeautifulSoup(res.text,'xml')

        try:
            locations = soup.find('locations').find_all('location')
        except:
            return None
        
        for locations_item in locations:
            location = locations_item.find('name').text
            unit = locations_item.find('units')
            units = unit.find_all('unit')
            
            for unit_item in units:
                dic = {}
                dic['title'] = unit_item.find('description').text
                try:
                    dic['description'] = unit_item.find('details').text.replace('<br /><br />','\n\n')
                    if '<p>' in dic['description']:
                        soup2 = BeautifulSoup(dic['description'],'lxml')
                        dic['description'] = soup2.find('p').get_text()
                    if '<div>' in dic['description']:
                        soup2 = BeautifulSoup(dic['description'],'lxml')
                        dic['description'] = soup2.find('div').get_text()

                except:
                    dic['description'] = ''
                
                tr = 0

                while True:
                    if tr == 6:
                        dic['custom_number_0'] = ''
                        break
                    try:
                        res2 = requests.get(unit_item.find('itemDetailUrl').text,headers=self.headers,timeout=15)
                        soup3 = BeautifulSoup(res2.text,'lxml')
                        payment_text = soup3.find(class_='payment-text')
                        if payment_text != None:
                            dic['custom_number_0'] = int(payment_text.text.split('/')[0].replace('$','').replace(',','').strip())
                        else:
                            dic['custom_number_0'] = 0
                        break
                    except:
                        tr += 1
                        time.sleep(2)
                        continue
                

                dic['price'] = unit_item.find('prices').find('msrp').text
                dic['sale_price'] = unit_item.find('prices').find('sales').text
                
                if '0.0000' == dic['price']:
                    dic['price'] = 0
                else:
                    dic['price'] = int(dic['price'].split('.')[0])

                if '0.0000' == dic['sale_price']:
                    dic['sale_price'] = 0
                else:
                    dic['sale_price'] = int(dic['sale_price'].split('.')[0])

                dic['link'] = unit_item.find('itemDetailUrl').text
                dic['custom_label_0'] = unit_item.find('productType').text
                dic['id'] = unit_item.find('stockNumber').text

                dic['custom_label_1'] = location
                dic['custom_label_2'] = unit_item.find('make').text
                dic['custom_label_3'] = unit_item.find('model').text
                dic['custom_number_1'] = unit_item.find('year').text
                dic['brand'] = unit_item.find('manufacturer').text

                dic['quantity_to_sell_on_facebook'] = "1"
                Condition = unit_item.find('isNew').text
                if Condition.lower() == 'true':
                    dic['condition'] = 'New'
                else:
                    dic['condition'] = 'Used'
                images = unit_item.find('assets').find_all('asset')
                url_imgs = ""
                for img in images:
                    try:
                        img_link = img.find('url').text
                        total_len_img = len(url_imgs) + len(img_link)
                        if total_len_img < 2000:
                            url_imgs += img_link + ','
                    except:
                        pass
                try:
                    dic['image_link'] = url_imgs.split(',')[0]
                    if url_imgs != "":
                        dic['additional_image_link'] = '{}'.format(url_imgs[:-1])
                    else:
                        dic['additional_image_link'] = ''
                except:
                    dic['image_link'] = ''
                    dic['additional_image_link'] = ''
                
                try:
                    avail = unit_item.find('status').text
                    if 'active' in avail.lower():
                        dic['availability'] = 'in stock'
                    else:
                        dic['availability'] = 'out of stock'
                except:
                    dic['availability'] = 'out of stock'

                google_product_category = ''
                custom = dic['custom_label_0'].lower()
                custom_list = ['toy','hauler','travel','trailer','wheel','destination']
                custom_list2 = ['pontoon','boat']
                custom_list3 = ['class','motorhome']

                for item_custom in custom_list:
                    if item_custom in custom:
                        google_product_category = 4243

                for item_custom2 in custom_list2:
                    if item_custom2 in custom:
                        google_product_category = 3095

                for item_custom3 in custom_list3:
                    if item_custom3 in custom:
                        google_product_category = 920
                    
                if google_product_category != '':
                    dic['google_product_category'] = str(google_product_category)
                else:
                    dic['google_product_category'] = "4243"
                
                if 'Used' in dic['condition'] and dic['price'] == 0:
                    dic['price'] = dic['sale_price']
                    dic['sale_price'] = 0
                
                if dic['price'] == 0 and dic['sale_price'] == 0:
                    continue

                order = ['id','title','description','availability','condition','sale_price','price','link','image_link','additional_image_link','brand','google_product_category','quantity_to_sell_on_facebook','custom_label_0','custom_label_1','custom_label_2','custom_label_3','custom_number_0','custom_number_1']
                dic2 = {}
                for order_item in order:
                    dic2[order_item] = dic[order_item]

                #dic['properties'] = properties
                print('name: ' + dic['title'] + '| count: ' + str(self.count))
                #pprint.pprint(dic)
                self.count += 1
                self.save.append(dic2)
                dic3 = {}
                dic3['Page URL'] = dic2['link']
                brand = dic['brand']
                con = dic['condition']
                label0 = dic['custom_label_0']
                label2 = dic['custom_label_2']
                label3 = dic['custom_label_3']
                cus_num0 = dic['custom_number_0']
                cus_num1 = dic['custom_number_1']
                dic3['Custom Label'] = f'vehicle_display_page;{brand};{con};{label0};{label2};{label3};{cus_num0};{cus_num1}'
                self.save2.append(dic3)



