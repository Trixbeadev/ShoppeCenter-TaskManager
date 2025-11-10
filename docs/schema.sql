CREATE DATABASE IF NOT EXISTS shoppecenter;
USE shoppecenter;

CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    setor VARCHAR(50) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    responsavel VARCHAR(100) NOT NULL,
    prazo_entrega DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);