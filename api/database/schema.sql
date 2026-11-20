-- Banco de questões (MySQL)

CREATE TABLE IF NOT EXISTS questao (
  idQuestao     INT AUTO_INCREMENT PRIMARY KEY,
  tipo          ENUM('D','V','M') NOT NULL,              -- Discursiva, Verdadeiro/Falso, Múltipla-escolha
  enunciado     TEXT NOT NULL,
  imagem        VARCHAR(255) NULL,                       -- caminho/URL
  alternativas  JSON NULL,                               -- para M e V
  materia       VARCHAR(100) NULL,
  ano           YEAR NULL,                               -- ano da prova
  banca         VARCHAR(100) NULL,                       -- ex.: FGV, CESPE, VUNESP
  instituicao   VARCHAR(150) NULL,                       -- órgão/universidade da prova
  dificuldade   ENUM('MF','F','M','D','MD') NULL,        -- Muito fácil, Fácil, Média, Difícil, Muito difícil
  data_criacao  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS resposta (
  idResposta INT AUTO_INCREMENT PRIMARY KEY,
  idQuestao  INT NOT NULL,
  tipo       ENUM('D','V','M') NOT NULL,                 -- Discursiva, Verdadeiro/Falso, Múltipla-escolha
  resposta   TEXT NOT NULL,
  FOREIGN KEY (idQuestao) REFERENCES questao(idQuestao) ON DELETE CASCADE
);
