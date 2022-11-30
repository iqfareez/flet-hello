import flet as ft
import requests


def main(page: ft.Page):
    page.fonts = {
        'Architects Daughter': 'assets/ArchitectsDaughter-Regular.ttf',
    }
    page.padding = ft.Padding(20, 35, 20, 20)
    appbar = ft.AppBar(title=ft.Text(value="Flutter using Flet"),
                       bgcolor=ft.colors.BLUE,
                       color=ft.colors.WHITE)

    quote_text = ft.Text(value='""',
                         size=32,
                         color=ft.colors.BLACK,
                         weight=ft.FontWeight.BOLD,
                         font_family='Architects Daughter')
    quote_author = ft.Text(value="",
                           size=15,
                           color=ft.colors.BLACK87,
                           italic=True)

    def button_clicked(e):
        print('Button clicked')
        quote, author = getRandomQuotes()
        # print(quote, author)
        quote_text.value = f'"{quote}"'
        quote_author.value = author
        page.update()

    refreshButton = ft.ElevatedButton(text="Refresh", on_click=button_clicked)
    sizedBox = ft.Container(height=20)
    page.controls.append(appbar)
    page.controls.append(quote_text)
    page.controls.append(quote_author)
    page.controls.append(sizedBox)
    page.controls.append(refreshButton)
    page.update()


def getRandomQuotes():
    api_url = 'http://api.forismatic.com/api/1.0/?method=getQuote&key=837122&format=json&lang=en'
    response = requests.get(api_url)
    data = response.json()
    # print(data)
    return data['quoteText'], data['quoteAuthor']


ft.app(target=main, assets_dir='assets')