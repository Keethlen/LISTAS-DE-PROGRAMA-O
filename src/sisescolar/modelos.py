from dataclasses import dataclass


#Anotações: @alguma-coisa
#Classes iniciam com letras maiusculas

@dataclass
class Data:
    dia: int
    mes: int
    ano: int

@dataclass
class Aluno:
    matricula: str
    nome: str
    sexo: str
    datanast: Data
