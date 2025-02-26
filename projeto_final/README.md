# API de Anotações em Python

## Sobre a API
Esta API permite armazenar, gerenciar e excluir anotações usando Python com FastAPI.

Ela suporta operações básicas como:
- Criar uma anotação
- Listar todas as anotações
- Obter uma anotação específica
- Atualizar uma anotação
- Excluir uma anotação

## Como usar essa API

### 1. Instalando as Dependências

Instale os pacotes necessários:
```bash
pip install fastapi uvicorn
```

### 2. De start no Servidor

```bash
uvicorn notes_api:app --reload
```

Isso iniciará o servidor e ele estará pronto para receber requisições!

## Endpoints da API

### Criar uma Anotação
**Método:** `POST /notes`

**Exemplo de Corpo da Requisição:**
```json
{
    "title": "Minha Nota",
    "content": "Este é o conteúdo da minha nota."
}
```
**Resposta:**
```json
{
    "id": "1234-5678",
    "title": "Minha Nota",
    "content": "Este é o conteúdo da minha nota."
}
```

---
### Listar Todas as Anotações
**Método:** `GET /notes`

**Resposta:**
```json
[
    {
        "id": "1234-5678",
        "title": "Minha Nota",
        "content": "Este é o conteúdo da minha nota."
    }
]
```

---
### Obter uma Anotação Específica
**Método:** `GET /notes/{id}`

**Exemplo de Resposta:**
```json
{
    "id": "1234-5678",
    "title": "Minha Nota",
    "content": "Este é o conteúdo da minha nota."
}
```

Se a anotação não existir, retorna:
```json
{
    "message": "Anotação não encontrada."
}
```

---
### Atualizar uma Anotação
**Método:** `PUT /notes/{id}`

**Corpo da Requisição:**
```json
{
    "title": "Novo Título",
    "content": "Novo conteúdo da anotação."
}
```
**Resposta:**
```json
{
    "id": "1234-5678",
    "title": "Novo Título",
    "content": "Novo conteúdo da anotação."
}
```

---
### Excluir uma Anotação
**Método:** `DELETE /notes/{id}`

**Resposta:**
```json
{
    "message": "Anotação excluída com sucesso."
}
```

## Interface Web
Criamos uma página HTML simples que interage com a API. Para usá-la:
1. Certifique-se de que o servidor está rodando.
2. Abra a página `public/index.html` no navegador.
3. Use os botões para criar, editar ou excluir anotações.