# 🚀 Guia de Instalação e Configuração - SmartFarmIrrigation

---

## 📚 Navegação da Documentação

| **Documento** | **Descrição** | **Link** |
|---------------|---------------|----------|
| 📖 **README Principal** | Documentação completa do projeto | **[README.md](./README.md)** |
| 🚀 **Guia de Instalação** | Setup rápido e resolução de problemas | *[Você está aqui]* |
| 🧪 **Relatório de Testes** | Testes completos e validação do sistema | **[COMPREHENSIVE_TEST_REPORT.md](./COMPREHENSIVE_TEST_REPORT.md)** |

---

Este guia rápido irá ajudá-lo a configurar e executar o projeto SmartFarmIrrigation.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Git (para clonar o repositório)
- PlatformIO (para compilação do código ESP32)

## 🔧 Instalação

### 1. Clone o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd SmartFarmIrrigation
```

### 2. Configure o Ambiente Python
```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
cd scripts
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente
```bash
# Copie o arquivo .env de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave da API OpenWeather
# Obtenha uma chave gratuita em: https://openweathermap.org/
```

### 4. Configure o Banco de Dados
```bash
# Execute o script de inicialização do banco
python database.py

# Popule com dados de exemplo (opcional)
python populate_db.py
```

### 5. Treine o Modelo de Machine Learning
```bash
python train_model.py
```

## 🚀 Execução

### Dashboard Streamlit
```bash
streamlit run dashboard.py
```

### Verificar Integração com Weather API
```bash
python weather_integration.py
```

### Testes Automatizados
```bash
# Instale dependências de desenvolvimento
pip install -r requirements-dev.txt

# Execute os testes
pytest
```

## 📱 Simulação ESP32 (Wokwi)

1. Acesse [Wokwi.com](https://wokwi.com)
2. Importe o arquivo `diagram.json`
3. Carregue o código de `src/prog1.ino`
4. Execute a simulação

## 🔧 Resolução de Problemas

### Erro: "Model file not found"
```bash
# Execute o treinamento do modelo
python train_model.py
```

### Erro: "Database not found"
```bash
# Recrie o banco de dados
python database.py
```

### Erro: "API Key not configured"
```bash
# Verifique se o arquivo .env está configurado corretamente
# Certifique-se de que OPENWEATHER_API_KEY está definida
```

## 📚 Estrutura de Arquivos

```
SmartFarmIrrigation/
├── scripts/
│   ├── dashboard.py          # Interface Streamlit
│   ├── train_model.py        # Treinamento ML
│   ├── database.py           # Operações DB
│   ├── weather_integration.py # API OpenWeather
│   ├── utils.py              # Funções utilitárias
│   └── requirements.txt      # Dependências Python
├── src/
│   ├── prog1.ino             # Código ESP32
│   └── config.h              # Configurações
├── tests/
│   └── test_utils.py         # Testes automatizados
├── .env                      # Variáveis de ambiente
├── diagram.json              # Circuito Wokwi
└── README.md                 # Documentação principal
```

## 🎯 Próximos Passos

1. Configure sua chave da API OpenWeather
2. Execute o dashboard: `streamlit run dashboard.py`
3. Teste as predições de IA
4. Explore a documentação completa no README.md

## 🆘 Suporte

Se encontrar problemas, verifique:
1. Versões corretas do Python e dependências
2. Configuração do arquivo .env
3. Execução dos scripts na ordem correta

Para mais detalhes, consulte o `README.md` principal e o `COMPREHENSIVE_TEST_REPORT.md`.
