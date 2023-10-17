import flet as ft
import os

# Dicionario style
data_table_style: dict = {
    'main': {
        'expand': True,
        'bgcolor': '#fdfdfe',

    },
    'data_table': {
        'heading_row_color': '#e3e4ea',
        'expand': True,
        'heading_row_height': 35,
        'data_row_max_height': 40,
    },
}

form_style: dict= {
    'main': {
        'expand': 2,
        'bgcolor': '#fdfdfe',
        'padding': ft.padding.only(left=35, right=35),
    },
    'input': {
        'height': 38,
        'border_color': '#aeaeb3',
        'focused_border_color': 'black',
        'border_radius': '5',
        'cursor_color': 'black',
        'content_padding': 10,
        'border_width': 1.5,
        'text_size':12,
    },
}


# Classe do dataframe
class DataTable(ft.Container):
    def __int__(self):
        super().__init__(**data_table_style['main'])

        self.table= ft.DataTable(
            **data_table_style['data_table'],
        )

        headers: list = [
            'Nome Completo',
            'Email',
            'Numero'
        ]

        self.table.columns = [
            ft.DataColumn(ft.Text(title, weight='w600',
                                  size=12)) for title in headers
        ]

        self.content = ft.Column(
            scroll='hidden', controls=[ft.Row(controls=[self.table])]
        )

# Classe de formulario
class Form(ft.Container):
    def __int__(self, table: ft.DataTable):
        super().__init__(**form_style['main'])
        self.table = table

        # Inputs
        self.name = ft.TextField(**form_style['input'])
        self.email = ft.TextField(**form_style['input'])
        self.numero = ft.TextField(**form_style['input'])

        # Logica e loops
        data: list = ['Nome Completo', 'Email', 'Numero']
        fields: list =[self.name, self.email, self.numero]

        # compressão de lista para criar os inputs fields e titulos
        items: list = [
            ft.Column(
                expand=True, spacing=4,
                controls=[
                    ft.Text(title, size=12, weight='w500'),
                    fields[index]
                ]
            )
            for index, title in enumerate(data)
        ]

        # Botao para salvar
        self.add = ft.ElevatedButton(
            text='Salvar',
            color='white',
            bgcolor='blue600',
            height=40,
            style=ft.ButtonStyle(shape={'': ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data,
        )

        # self.content e ft.Container propietarios
        self.content = ft.Column(
            controls=[
                ft.Divider(height=10, color='transparent'),
                ft.Text('Gravado', size=28, weight='w900'),
                ft.Divider(height=30, color='transparent'),
                ft.Row(spacing=20, expand=True, controls=items),
                ft.Divider(height=10, color='transparent'),
                ft.Row(alignment='end', controls=[self.add], expand=True),
            ]
        )

        def create_data_row(self, values: list):
            data = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(values[0], size=12, weight='600')),
                    ft.DataCell(ft.Text(values[1], size=12, weight='600')),
                    ft.DataCell(ft.Text(values[2], size=12, weight='600'))
                ]
            )

        def update_data_table(self, data: ft.DataRow):
            self.table.rows.append(data)
            self.table.update()

        def save_data(self, event):
            values: list = [self.name.value, self.email.value, self.numero]
            #verificação
            if all(values):
                # primeira criar o df e linha e retonar
                data: Any = self.create_data()
                self.update_data_table

        def write_data_to_csv():
            # Loop iniciado para o df para escrever no arquivo
            csv_rows: list = []
            # Iterando sobre as linhas da tabela
            for row in self.table.rows[:]:
                # Criando um arq temporario
                temp_list: list = []
                # Agora interando sobre a lista pela linha (row = list)
                for control in row.cells[:]:
                    temp_list.append(control.content.value)

                csv_rows.append(temp_list)

                #p

            with open('data.csv', 'w') as file:
                csvwriter = csv.writer(file)
                # !! note a diferença b.w linha em linhas no csvwriter
                csvwriter.writerow(['Nome Completo','Email', 'Numero'])
                csvwriter.writerow(csv_rows)


        def check_if_csv_exists(self):
            # Verifica se existe csv caso não cria

            # Verificando se o arquivo está no diretorio
            if 'data.csv' not in os.listdir('.'):
                # se já estiver ok
                with open('data.csv', 'a'):
                    pass
            else:
                self.write_data_to_csv()
                pass






# Entradas para o apps
def main(page : ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    dataTable : ft.Container = DataTable()
    # passando a variavel df para o DF do form
    form: ft.Container = Form(table=dataTable.table)


    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Column(expand=5, controls=[form, dataTable])
            ]
        )
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main)