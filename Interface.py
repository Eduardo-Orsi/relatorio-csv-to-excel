import PySimpleGUI as sg
import os
from ValidaCurso import comparativo

diretorio = os.getcwd()

class Interface():

    def __init__(self) -> None:
        
        layout = [
            [sg.Text('Nome empresa'), sg.Input(key="nome_empresa", do_not_clear=False)],
            [sg.Text("CSV do Curso Antigo"),sg.InputText(key="path_csv_curso_antigo", do_not_clear=False), sg.FileBrowse(initial_folder=diretorio, file_types=[("CSV Files", "*.csv")])],
            [sg.Text("CSV do Curso Novo"),sg.InputText(key="path_csv_curso_novo", do_not_clear=False), sg.FileBrowse(initial_folder=diretorio, file_types=[("CSV Files", "*.csv")])],
            [sg.Text("Pasta de Destino"), sg.InputText(key="path_pasta_destino", do_not_clear=False), sg.FolderBrowse()],
            [sg.Button("Criar Relatório"), sg.Exit()]
        ]

        self.janela = sg.Window("Facilitador Relatório Capacitação").layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome_empresa = self.values["nome_empresa"]
            path_csv_curso_antigo = self.values["path_csv_curso_antigo"]
            path_csv_curso_novo = self.values["path_csv_curso_novo"]
            path_pasta_destino = self.values["path_pasta_destino"]
            if self.button == sg.WIN_CLOSED or self.button == 'Exit':
                break
            comparativo(nome_empresa, path_csv_curso_antigo, path_csv_curso_novo, path_pasta_destino)
        self.janela.close()

tela = Interface()
tela.iniciar()