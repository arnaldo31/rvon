import requests
from bs4 import BeautifulSoup
import pprint
import gspread
import datetime
import pandas
import numpy


def open_sheet(save:list):
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
    
    df = pandas.DataFrame(save)
    df = df.replace(numpy.NAN,'')
    gc = gspread.service_account_from_dict(creds)
    spreed_sheet_id = '18TCdKt1U1DLQv4UHL-3HJzVca2DPikMZxFOGnThmSMk'
    sheet = gc.open_by_key(spreed_sheet_id)
    worksheet = sheet.worksheet('Sheet1')
    worksheet.batch_clear(["A1:EZ"])
    columns = df.columns.values.tolist()
    body = df.values.tolist()
    save = []
    save.append(columns)
    for item in body:
        save.append(item)
    worksheet.update(values=save, range_name='A1')
    print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(save)))
    

def open_sheet2(save:list):
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
    
    df = pandas.DataFrame(save)
    df = df.replace(numpy.NAN,'')
    gc = gspread.service_account_from_dict(creds)
    spreed_sheet_id = '1uDgehvU8zIi22rrAsWZIv_eQM1SCUvsfr3vcHdsqlG0'
    sheet = gc.open_by_key(spreed_sheet_id)
    worksheet = sheet.worksheet('Sheet1')
    worksheet.batch_clear(["A1:EZ"])
    columns = df.columns.values.tolist()
    body = df.values.tolist()
    save = []
    save.append(columns)
    for item in body:
        save.append(item)
    worksheet.update(values=save, range_name='A1')
    print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(save)))
        
        
def main(category:str):
    save = []
    save2 = []
    global count
    
    count = 1

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://www.venturarvconnection.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        's': 'true',
        'condition': category,
    }

    response = requests.get('https://www.venturarvconnection.com/rv-search', params=params,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    cards = soup.find_all(class_='unit-title-wrapper list-mode')
    if cards == []:
        return []
    
    def parse(unit):
        global count
        
        dic = {}
        title = unit.a.text 
        dic['title'] = title
        details = unit.parent.find(class_='unit-content-wrapper detailsContainer')
        image = details.get('data-img')
        msrp = details.get('data-msrp').replace('$','').replace(',','')
        if '.' in msrp:
            msrp = float(msrp)
        price = int(msrp)
        
        sale_price = details.get('data-saleprice')
        if sale_price != None:
            sale_price = sale_price.replace('$','').replace(',','')
            if '.' in sale_price:
                sale_price = float(sale_price)
            sale_price = int(sale_price)
            
        if sale_price == None:
            sale_price = 0
        
        if price == 0 and sale_price != 0:
            price = sale_price
            
        location = unit.find(class_='unit-location-text').get_text(strip=True)
        year = details.get('data-year')
        type = details.get('data-type')
        manufacturer = details.get('data-mfg')
        brand = details.get('data-brand')
        model = details.get('data-unitname')
        stockID = details.get('data-stocknumber')
        availability = 'in stock'
        if category == '1':
            condition = 'New'
        if category == '0':
            condition = 'Used'
        url = 'https://www.venturarvconnection.com' + unit.a.get('href')
        res = requests.get(url,headers=headers)
        soup2 = BeautifulSoup(res.text,'html.parser')
        description = ''
        desk = soup2.find(class_='UnitDescText-main')
        monthly = soup2.find(class_='payments-around-container')
        if monthly != None:
            try:
                monthly = int(monthly.find(class_='payment-text').text.split('/')[0].replace('$','').replace(',','').strip())
            except:
                monthly = 0
        else:
            monthly = 0
        if desk != None:
            text = ''
            for tag in desk.contents:
                if tag.name == 'p':
                    text += tag.get_text('\n',strip=True) + '\n'
                if tag.name == 'ul':
                    for li in tag.find_all('li'):
                        text += ' - ' + li.text + '\n'
            
            description = text
        
        images = soup2.find(class_='detailMediaPhotoPlayer')
        url_imgs = ""
        imgs_list = []
        if images != None:
            images = images.find_all('img',attrs={'llsrc':True})
            for img in images:
                try:
                    img_link = img.get('llsrc')
                    total_len_img = len(url_imgs) + len(img_link)
                    if total_len_img < 2000:
                        url_imgs += img_link + ','
                        imgs_list.append(img_link)
                except:
                    pass
        
        
        if imgs_list != []:
            image = imgs_list[0]
            imgs_list = ','.join(imgs_list)
        else:
            imgs_list = ''

        dic['description'] = description
        dic['custom_number_0'] = monthly
        dic['price'] = price
        dic['sale_price'] = sale_price
        dic['link'] = url
        dic['custom_label_0'] = type
        dic['id'] = stockID
        dic['custom_label_1'] = location
        dic['custom_label_2'] = manufacturer
        dic['custom_label_3'] = model
        dic['custom_number_1'] = year
        dic['brand'] = brand
        dic['quantity_to_sell_on_facebook'] = "1"
        dic['condition'] = condition
        dic['image_link'] = image
        dic['additional_image_link'] = imgs_list
        dic['availability'] = availability
        
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
            
        order = ['id','title','description','availability','condition','sale_price','price','link','image_link','additional_image_link','brand','google_product_category','quantity_to_sell_on_facebook','custom_label_0','custom_label_1','custom_label_2','custom_label_3','custom_number_0','custom_number_1']
        dic2 = {}
        for order_item in order:
            dic2[order_item] = dic[order_item]
        
        print('name: ' + dic['title'] + '| count: ' + str(count))
        count += 1
        save.append(dic2)
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
        save2.append(dic3)
    
    for unit in cards:
        try:
            parse(unit)
        except:
            pass
        
    return save,save2
        
    
if __name__ == '__main__':
    savefile = []
    savefile2 = []
    for cat in ['1','0']:
        save,save2 = main(category=cat)
        savefile.extend(save)
        savefile2.extend(save2)
        
    open_sheet(save=savefile)
    open_sheet2(save=savefile2)
