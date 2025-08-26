# Mini Projeto: API com Swagger e Testes

Este projeto é uma **API simples em Flask** que realiza operações matemáticas básicas (soma, subtração, multiplicação e divisão), 
documentada com **Swagger** e validada com **testes automatizados** usando PyTest.

## 🚀 Tecnologias utilizadas
- **Python 3.13.5**
- **Flask** → criação da API
- **Flasgger (Swagger UI)** → documentação interativa
- **PyTest** → testes automatizados
- **Mermaid (C4 Model)** → diagramas de arquitetura

## ​⚙️​ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Diogo-Freire/API-MATEMATICA.git
   cd API-MATEMATICA```

2. Crie um ambiente virtual(opcional):
   ```bash
   python -m venv venv
   venv\Scripts\activate```
   
3. Instale o arquivo de dependências:
   ```bash
   pip install -r ==requirements.txt==```

4. Rode a API
   ```bash
   python app.py```

5. Abra a API no navegador
   👉 *http://127.0.0.1:5000*

6. Documentação Swagger disponível em:
   A documentação interativa pode ser acessada em /apidocs após rodar o projeto
  👉 *http://127.0.0.1:5000/apidocs*


## 🕹️ Exemplos de uso 🕹️
 ```bash
   GET /soma?a=2&b=3
   Resposta: { "resultado": 5 }```

```bash
   GET /subtracao?a=10&b=3
   Resposta: { "resultado": 7 }```

```bash
   GET /multiplicacao?a=5&b=5
   Resposta: { "resultado": 25 }```

```bash
   GET /divisao?a=4&b=2
   Resposta: { "resultado": 2 }```

##🧪Testes automatizados
Para rodar os testes use:

```bash
   def test_soma(client):
       response = client.get("/soma?a=2&b=3")
       assert response.json["resultado"] == 5```

Exemplo de teste implementado:

```bash
   def test_soma(client):
    response = client.get("/soma?a=2&b=3")
    assert response.json["resultado"] == 5```

## 📓 Modelo C4

 ☑️ **Nível Contexto**
 ```mermaid
   graph TD
    Usuario[👤 Usuário] -->|Requisições HTTP| API[📦 API de Operações Matemáticas]
    API -->|Documentação| SwaggerUI[📖 Swagger UI]
 ```












