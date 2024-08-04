# from bs4 import BeautifulSoup as BS
# import requests
# from multiprocessing import Pool
# from openpyxl import Workbook


# def get_html(url):
#     headers = {
#         'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     return None


# def get_link(html):
#     links = []
#     soup = BS(html, 'html.parser')
#     content = soup.find('div', class_='wrapper')
#     posts = content.find_all('div', class_='col-sm-4 col-xs-6')
#     for p in posts:
#         block = p.find('div', class_='block-content')
#         title = block.find('div', class_='title').text.strip()
#         link = block.find('a').get('href')
#         full_link = 'https://www.myphone.kg' + link
#         links.append(full_link)
#         # print(title)

#     return links

#     # for p in block:
#     #     title = block.find('div', class_='title')
#     #     link = title.find('a').get('href')

#     # return links


# def get_data(html):
#     soup = BS(html, 'html.parser')
#     content = soup.find('div', class_='wrapper')
#     right_block = content.find('div', class_='col-md-3 col-xs-12 item-info')
#     main_title = content.find('h1', class_='item-title').text.strip()
#     color = right_block.find('div', class_='color').text.strip()
#     price = right_block.find('div', class_='price').text.strip()
#     standart_delivery = right_block.find(
#         'div', class_='delivery-block').text.strip()
#     free_delivery = right_block.find(
#         'div', class_='delivery-block red-block').text.strip()
#     price_onCredit = right_block.find(
#         'div', class_='col-xs-12 no-ras kr').text.strip()
#     down_block = content.find('div', class_='cont').text.strip()
#     down_block_2 = content.find('div', class_='cont product-spec').text.strip()
#     options = content.find('ul', class_='tab')
#     if options is not None:
#         options_text = options.text.strip()  # Теперь безопасно получать text
#         print(options_text)
#     else:
#         print("NO OPTIONS")

#     # print(main_title)
#     # print(down_block)
#     # print(down_block_2)
#     # print(color)
#     # print(price)
#     # print(standart_delivery)
#     # print(free_delivery)
#     # print(price_onCredit)

#     data = {
#         'title': main_title,
#         'color': color,
#         'price': price,
#         'delivery': standart_delivery,
#         'free delivery': free_delivery,
#         'credit price': price_onCredit,
#         'description title': options,
#         'description info':  down_block,
#         'tech. description info': down_block_2
#     }
#     return data


# def save_to_exel(data):
#     workbook = Workbook()
#     sheet = workbook.active
#     sheet['A1'] = 'Название'
#     sheet['B1'] = 'Цвет'
#     sheet['C1'] = 'Цена'
#     sheet['D1'] = 'Стандартная доставка'
#     sheet['E1'] = 'Бесплатная доставка'
#     sheet['F1'] = 'Цена в кредит'
#     sheet['G1'] = 'Характеристики, Технические характеристики'
#     sheet['H1'] = 'Описание характеристик'
#     sheet['I1'] = 'Описание технических характеристик'
 
#     for i, item in enumerate(data, 2):
#         sheet[f'A{i}'] = item['main_title']
#         sheet[f'B{i}'] = item['color']
#         sheet[f'C{i}'] = item['price']
#         sheet[f'D{i}'] = item['standart_delivery']
#         sheet[f'E{i}'] = item['free_delivery']
#         sheet[f'F{i}'] = item['price_onCredit']
#         sheet[f'G{i}'] = item['descr_text']
#         sheet[f'H{i}'] = item['tech_descr_text']
#         sheet[f'I{i}'] = item['down_block']
#         sheet[f'J{i}'] = item['down_block_2']
 
 
#     workbook.save('mobilephone.kg.xlsx')


# def main():
#     URL = 'https://www.myphone.kg/ru/catalog/cell/'
#     html = get_html(url=URL)
#     links = get_link(html=html)
#     for link in links:
#         posts_links = get_html(url=link)
#         get_data(html=posts_links)
 
# if __name__ == '__main__':
#     main()
from bs4 import BeautifulSoup as BS
import requests
from openpyxl import Workbook

def get_html(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def get_link(html):
    links = []
    soup = BS(html, 'html.parser')
    content = soup.find('div', class_='wrapper')
    posts = content.find_all('div', class_='col-sm-4 col-xs-6')
    for p in posts:
        block = p.find('div', class_='block-content')
        title = block.find('div', class_='title').text.strip()
        link = block.find('a').get('href')
        full_link = 'https://www.myphone.kg' + link
        links.append(full_link)
    return links

def get_data(html):
    soup = BS(html, 'html.parser')
    content = soup.find('div', class_='wrapper')
    right_block = content.find('div', class_='col-md-3 col-xs-12 item-info')
    
    # Извлечение данных
    main_title = content.find('h1', class_='item-title').text.strip()
    color = right_block.find('div', class_='color').text.strip() if right_block.find('div', class_='color') else None
    price = right_block.find('div', class_='price').text.strip() if right_block.find('div', class_='price') else None
    standart_delivery = right_block.find('div', class_='delivery-block').text.strip() if right_block.find('div', class_='delivery-block') else None
    free_delivery = right_block.find('div', class_='delivery-block red-block').text.strip() if right_block.find('div', class_='delivery-block red-block') else None
    price_onCredit = right_block.find('div', class_='col-xs-12 no-ras kr').text.strip() if right_block.find('div', class_='col-xs-12 no-ras kr') else None
    
    down_block = content.find('div', class_='cont').text.strip() if content.find('div', class_='cont') else None
    down_block_2 = content.find('div', class_='cont product-spec').text.strip() if content.find('div', class_='cont product-spec') else None
    
    options = content.find('ul', class_='tab')
    options_text = options.text.strip() if options else "NO OPTIONS"

    data = {
        'main_title': main_title,
        'color': color,
        'price': price,
        'standart_delivery': standart_delivery,
        'free_delivery': free_delivery,
        'price_onCredit': price_onCredit,
        'descr_text': options_text,
        'down_block': down_block,
        'down_block_2': down_block_2
    }
    return data

def save_to_exel(data):
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Название'
    sheet['B1'] = 'Цвет'
    sheet['C1'] = 'Цена'
    sheet['D1'] = 'Стандартная доставка'
    sheet['E1'] = 'Бесплатная доставка'
    sheet['F1'] = 'Цена в кредит'
    sheet['G1'] = 'Характеристики'
    sheet['H1'] = 'Описание характеристик'
    sheet['I1'] = 'Описание технических характеристик'

    for i, item in enumerate(data, 2):
        sheet[f'A{i}'] = item['main_title']
        sheet[f'B{i}'] = item['color']
        sheet[f'C{i}'] = item['price']
        sheet[f'D{i}'] = item['standart_delivery']
        sheet[f'E{i}'] = item['free_delivery']
        sheet[f'F{i}'] = item['price_onCredit']
        sheet[f'G{i}'] = item['descr_text']
        sheet[f'H{i}'] = item['down_block']
        sheet[f'I{i}'] = item['down_block_2']

    workbook.save('mobilephone.kg.xlsx')

def main():
    URL = 'https://www.myphone.kg/ru/catalog/cell/'
    html = get_html(url=URL)
    links = get_link(html=html)

    all_data = []  # Список для хранения всех данных
    for link in links:
        posts_links = get_html(url=link)
        if posts_links:  # Проверяем, успешно ли получен HTML
            data = get_data(html=posts_links)
            all_data.append(data)  # Добавляем данные в список

    save_to_exel(all_data)  # Сохраняем все данные в Excel

if __name__ == '__main__':
    main()