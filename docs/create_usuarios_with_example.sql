-- create_usuarios_with_example.sql
-- Cria o banco (se necessário), cria a tabela 'usuarios' e insere um usuário de exemplo.

CREATE DATABASE IF NOT EXISTS shoppecenter;
USE shoppecenter;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT de exemplo (email: usuario@exemplo.com, senha: Senha123!)
-- A senha já está no formato hashed (scrypt). Se você quiser outro usuário, substitua email/nome/hash abaixo.
INSERT INTO usuarios (email, senha, nome)
VALUES ('usuario@exemplo.com', 'scrypt:32768:8:1$iwutnQQBk5ZS4NkZ$a294090d5524f5338c1f41a10275257e588b098e27e5f52c7e3ab4de2a4b738af066135ddf2e79a20b0381d76f3ec38d06d790f488abcdf90877a1f8de620180', 'Usuário Exemplo');
