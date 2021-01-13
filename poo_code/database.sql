create database poobanck;
use poobanck;

CREATE TABLE Clientes (
    cpf VARCHAR(11)NOT NULL,
    nome VARCHAR(255)NOT NULL,
    PRIMARY KEY (cpf)
);

CREATE TABLE Carros(
    placa VARCHAR(8) UNIQUE NOT NULL,
    modelo VARCHAR(255) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    PRIMARY KEY (placa)
);

CREATE TABLE Aluguel(
    pagamento VARCHAR(20),
	data_lancamento TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
    cpfcliente VARCHAR(11)NOT NULL,
    placaVeiculo VARCHAR(8) UNIQUE NOT NULL,
    FOREIGN KEY (cpfcliente) REFERENCES Clientes(cpf) ON DELETE CASCADE
ON UPDATE CASCADE,
    FOREIGN KEY (placaveiculo) references Carros(placa) ON DELETE CASCADE
 ON UPDATE CASCADE
);




