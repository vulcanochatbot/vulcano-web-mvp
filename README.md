# Vulcano Web MVP

O **Vulcano Web MVP** é uma plataforma web voltada para o apoio à contratação de mão de obra na construção civil, conectando **profissionais/candidatos** e **empresas/construtoras** em um fluxo simples, direto e funcional.

Este repositório concentra a versão principal do MVP do projeto **Vulcano**, desenvolvido em contexto acadêmico no curso de **Análise e Desenvolvimento de Sistemas (ADS)**, com proposta de caso real e foco em resolver um problema prático do setor.

---

## 1. Descrição geral

O Vulcano não foi concebido como apenas mais um site genérico de vagas.  
O projeto nasce da necessidade de tornar o processo de contratação na construção civil mais acessível, organizado e eficiente, especialmente em um cenário onde ainda existem dificuldades de comunicação, informalidade e baixa padronização das informações entre empresas e profissionais.

A proposta atual do projeto foi intencionalmente **enxugada** para viabilizar a entrega de um **MVP web funcional**, com escopo realista, implementação possível e foco na solução do problema principal.

---

## 2. Contexto e problema identificado

O processo de contratação na construção civil costuma apresentar obstáculos que impactam tanto empresas quanto trabalhadores. Entre os principais problemas observados estão:

- dificuldade de encontrar profissionais com rapidez
- comunicação desorganizada entre empresa e trabalhador
- triagem manual e lenta
- informalidade no processo de recrutamento
- desencontro entre oferta e demanda
- pouca padronização das informações dos candidatos
- barreiras digitais para parte do público
- necessidade de uma solução simples, clara e acessível

Nesse contexto, o Vulcano busca reduzir o atrito inicial da contratação, oferecendo uma plataforma digital enxuta que facilita o cadastro, a publicação de vagas, a candidatura e a orientação de uso do sistema.

---

## 3. Objetivo do produto

Desenvolver uma **plataforma web simples e funcional** para facilitar a conexão entre **empresas da construção civil** e **profissionais/candidatos**, permitindo um fluxo básico de contratação com apoio de um chatbot contextual integrado ao sistema.

---

## 4. Proposta da solução

A proposta do Vulcano Web MVP é oferecer um ambiente web em que:

- candidatos possam se cadastrar, fazer login, visualizar vagas e se candidatar
- empresas possam se cadastrar, fazer login, criar vagas e gerenciá-las
- o sistema mantenha os dados em um banco real
- o usuário tenha suporte inicial por meio de um assistente contextual da própria plataforma

A solução foi planejada para ser **coerente com a fase atual do projeto**, evitando complexidade desnecessária e priorizando o que é essencial para validar a proposta do produto.

---

## 5. Perfis de usuário do sistema

O MVP foi estruturado com dois perfis principais de uso:

### Candidato
Profissional da construção civil que deseja:

- criar conta na plataforma
- acessar vagas disponíveis
- visualizar detalhes de oportunidades
- realizar candidatura
- acompanhar informações básicas do próprio perfil/painel

### Empresa
Empresa, construtora ou responsável por recrutamento que deseja:

- cadastrar a organização no sistema
- acessar a área da empresa
- criar novas vagas
- visualizar e gerenciar vagas cadastradas
- utilizar a plataforma como apoio inicial ao recrutamento

---

## 6. Escopo do MVP

O escopo atual do **Vulcano Web MVP** contempla:

- cadastro de candidato
- login de candidato
- cadastro de empresa
- login de empresa
- criação de vagas
- visualização de vagas
- candidatura em vagas
- painel básico do candidato
- painel básico da empresa
- gerenciamento básico das vagas
- chatbot contextual integrado ao sistema
- banco de dados real
- interface web responsiva
- fluxo funcional ponta a ponta

Esse escopo representa a definição atual do projeto e orienta o desenvolvimento da versão principal apresentada neste repositório.

---

## 7. Funcionalidades principais

### Área do candidato
- cadastro de conta
- autenticação no sistema
- visualização de vagas
- candidatura em oportunidades
- acesso ao painel básico do usuário

### Área da empresa
- cadastro de conta empresarial
- autenticação no sistema
- criação de vagas
- listagem e gerenciamento básico das vagas publicadas
- acesso ao painel básico da empresa

### Núcleo do sistema
- persistência de dados com banco real
- separação de perfis de acesso
- rotas para candidatos, empresas, vagas e chatbot
- fluxo web funcional do início ao fim

---

## 8. Papel do chatbot no sistema

O chatbot do MVP **não é apresentado como uma IA genérica, autônoma ou super avançada**.

No escopo atual, ele atua como um **assistente contextual da plataforma**, com foco em:

- orientar usuários sobre cadastro
- explicar login e navegação
- ajudar candidatos e empresas a entenderem como usar o sistema
- responder dúvidas sobre vagas, perfis e candidaturas
- atuar dentro do contexto do próprio Vulcano

Seu papel no MVP é melhorar a experiência inicial do usuário, oferecendo suporte rápido e contextual durante o uso da plataforma.

---

## 9. O que está no MVP e o que fica para depois

### Está no MVP
- fluxo web funcional entre cadastro, login, vagas e candidatura
- perfis distintos para candidato e empresa
- chatbot contextual integrado
- persistência real de dados
- interface responsiva
- estrutura simples e executável localmente

### Pode ficar para evoluções futuras
- integração com WhatsApp
- inteligência artificial mais avançada
- filtros mais robustos de busca e triagem
- histórico mais completo de interações
- sistema de notificações
- upload de currículo e documentos
- painel administrativo mais amplo
- novas métricas e relatórios
- evolução para arquitetura mais escalável

---

## 10. Tecnologias utilizadas

A stack atual do MVP foi definida de forma objetiva para manter o projeto viável, compreensível e executável.

### Backend
- **Flask**

### Frontend
- **HTML**
- **CSS**
- **JavaScript**

### Banco de dados
- **SQLite**

### Chatbot
- **Assistente contextual integrado ao sistema**

### Estrutura principal da aplicação
- `app.py`
- `templates/`
- `static/`
- `instance/`

---

## 11. Estrutura do projeto

A organização principal do repositório segue uma estrutura simples e direta:

```bash
vulcano-web-mvp/
├── app.py
├── instance/
│   └── vulcano.db
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── main.js
│       └── chatbot.js
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── cadastro_candidato.html
│   ├── cadastro_empresa.html
│   ├── vagas.html
│   ├── detalhe_vaga.html
│   ├── painel_candidato.html
│   └── painel_empresa.html
└── README.md
