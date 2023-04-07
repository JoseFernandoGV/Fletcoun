import flet
from flet import Page, Row, Text, TextField, ElevatedButton



def main(page:Page):
    name = TextField(label = 'Digite su nombre')
    text_saludo = Text()

    def saludar(event):
        text_saludo.value = name.value
        page.update()

        print(name.value)
    
    row = Row(
        [name, ElevatedButton("Saludar", on_click=saludar),text_saludo
        ]
    )

    page.add(row)
    

flet.app(main, view=flet.WEB_BROWSER)