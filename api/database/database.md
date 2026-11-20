# Banco de Dados 

O banco de dados utilizado será um MySQL padrão com tabelas simples. Não precisa de autenticação por enquanto porque será apenas um banco de questões, o foco torna-se mais as questões, ou seja, as principais informações serão adicionadas nas seguintes tabelas: 

* questao 
    - idQuestao
    - tipo (D - Discursiva, V - Verdadeiro/Falso e M - Multipla-escolha)
    - enunciado
    - imagem (caminho/URL, opcional)
    - alternativas (JSON, para M e V)
    - materia
    - ano (ano da prova, se houver)
    - banca (se houver)
    - instituicao (se houver)
    - dificuldade (MF - Muito fácil, F - Fácil, M - Média, D - Difícil, MD - Muito difícil)
    - data_criacao
* resposta 
    - idResposta
    - idQuestao
    - tipo (D - Discursiva, V - Verdadeiro/Falso e M - Multipla-escolha)
    - resposta

O script de criação das tabelas está em `schema.sql`.
