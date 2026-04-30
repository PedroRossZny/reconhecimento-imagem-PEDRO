# Reconhecimento de Imagem

Este projeto é uma aplicação web para reconhecimento de imagens utilizando a Teachable Machine do Google. A aplicação permite treinar um modelo de machine learning com imagens capturadas pela webcam e realizar predições em tempo real.

## Funcionalidades

- **Captura de Imagem**: Utiliza a webcam do dispositivo para capturar imagens em tempo real.
- **Treinamento de Modelo**: Integração com Teachable Machine para treinar modelos de classificação de imagens.
- **Predição**: Realiza predições ao vivo com base no modelo treinado.
- **Interface Amigável**: Interface responsiva construída com Bootstrap.

## Estrutura do Projeto

```
reconhecimento-imagem-PEDRO/
├── index.html                 # Página principal da aplicação web
├── my_model/                  # Pasta contendo o modelo treinado (model.json, metadata.json, etc.)
└── teste-assistent-code/      # Exemplos de código Python para testes e aprendizado
    ├── debug.py               # Exemplo de código com bugs para depuração
    ├── explicacao-debug.md    # Explicação do código de debug
    ├── explicacao_num_primo.md # Explicação do algoritmo de números primos
    ├── explicacao-refatoracao.md # Explicação da refatoração de código
    ├── num_primos.py          # Implementação de verificação de números primos
    └── refatoracao.py         # Exemplo de código refatorado para cálculo de estatísticas
```

## Instalação

### Pré-requisitos

- Um navegador web moderno com suporte a JavaScript e acesso à webcam.
- Para os exemplos Python: Python 3.6 ou superior instalado no sistema.

### Passos para Instalação

1. Clone ou baixe este repositório.
2. Abra o arquivo `index.html` em um navegador web.
3. Para executar os exemplos Python, navegue até a pasta `teste-assistent-code` e execute os scripts com Python.

## Uso

### Aplicação Web de Reconhecimento de Imagem

1. Abra `index.html` no navegador.
2. Clique em "Ativar Câmera" para permitir acesso à webcam.
3. O modelo carregado da pasta `my_model/` será usado para predições.
4. As predições aparecerão em tempo real na tela.

**Nota**: Certifique-se de que a pasta `my_model/` contenha um modelo válido treinado com Teachable Machine. Se não existir, você precisará treinar um modelo primeiro no site da Teachable Machine e exportá-lo para esta pasta.

### Exemplos de Código Python

#### Verificação de Números Primos (`num_primos.py`)

Execute o script para verificar se uma lista de números são primos:

```bash
python num_primos.py
```

#### Exemplo de Depuração (`debug.py`)

Este script simula um sistema de cálculo de compras com imposto e desconto. Execute para ver o cálculo:

```bash
python debug.py
```

#### Exemplo de Refatoração (`refatoracao.py`)

Calcula estatísticas básicas de uma lista de números:

```bash
python refatoracao.py
```

## Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Machine Learning**: TensorFlow.js, Teachable Machine Image
- **Python**: Exemplos puros em Python 3 (sem dependências externas)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## Autor

Pedro Henrique Rodrigues

---

Para mais informações sobre Teachable Machine, visite: [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/)</content>
<parameter name="filePath">c:\Users\PEDROHENRIQUERODRIGU\Desktop\reconhecimento-imagem-PEDRO\README.md