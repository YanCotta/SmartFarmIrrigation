# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# SmartFarmIrrigation

## Nome do grupo

## 👨‍🎓 Integrantes

- [Yan Cotta](https://www.linkedin.com/in/yan-cotta/)

## 👩‍🏫 Professores

### Tutor(a)

- Lucas Gomes Moreira

### Coordenador(a)

- André Godoi Chiovato

## 📝 Sobre o Projeto

O **SmartFarmIrrigation** é um sistema inteligente de irrigação desenvolvido para a FarmTech Solutions como parte do curso de Inteligência Artificial e Machine Learning da FIAP. Este projeto simula um sistema IoT que utiliza um ESP32 no Wokwi para coletar dados de sensores (umidade do solo, pH, fósforo e potássio) e controlar um relé para irrigação com base em condições ambientais e climáticas.

Os dados são armazenados em um banco **SQLite**, visualizados em um dashboard interativo com **Streamlit** e ajustados pela integração com a **API OpenWeather**, que considera chuvas recentes.

O objetivo é otimizar o uso da água em fazendas, irrigando apenas quando necessário (umidade < 50%, pH entre 6–7, presença de nutrientes e chuva < 1mm). Desenvolvido com **C++ (ESP32)**, **Python** (processamento, visualização e integração de APIs) e **SQL** (armazenamento), o projeto cumpre os requisitos do curso e inclui os desafios "Ir Além" com um dashboard interativo e integração com API pública. A modelagem de dados segue o MER simplificado da Fase 2, utilizando uma única tabela `irrigation_data` para eficiência.

---

## 📸 Visualizações

*(Imagens localizadas na pasta `assets`)*

---

## 📁 Estrutura de Pastas

```
.github/                 # Configurações do GitHub
assets/                 # Imagens (logo FIAP, capturas de tela)
document/               # Documentação (ai_project_document_fiap.md)
scripts/                # Scripts Python
├── database.py         # Criação e gerenciamento do SQLite
├── dashboard.py        # Dashboard Streamlit
├── weather_integration.py  # Integração OpenWeather
├── verify_db.py        # Verificador de banco
├── requirements.txt    # Dependências
src/                    # Código C++ para ESP32
.pio/build/             # Build PlatformIO (ignorado)
.vscode/                # Configurações VS Code
diagram.json            # Configuração circuito Wokwi
platformio.ini          # Configuração PlatformIO
wokwi.toml              # Configuração Wokwi
.gitignore, .gitattributes
README.md               # Este arquivo
```

---

## 🔧 Como Executar o Código

### Pré-requisitos

- **IDE**: Visual Studio Code com extensões PlatformIO e Wokwi Simulator
- **Conta OpenWeather**: https://openweathermap.org/
- **Bibliotecas C++**: Arduino, DHT (via PlatformIO)
- **Bibliotecas Python**: Streamlit, Pandas, Matplotlib, Requests
- **Versões recomendadas**:
  - Python 3.9+
  - PlatformIO 6.0+
  - Wokwi CLI (opcional)

---

### Passos para Instalação e Execução

#### 1. Clonar o Repositório
```bash
git clone https://github.com/YanCotta/SmartFarmIrrigation.git
cd SmartFarmIrrigation
```

#### 2. Configurar o Ambiente Python
```bash
pip install -r scripts/requirements.txt
streamlit --version  # Verifique a instalação
```

#### 3. Configurar a Chave da API OpenWeather

Edite `scripts/weather_integration.py`:
```python
API_KEY = "YOUR_API_KEY_HERE"
```

#### 4. Executar o Banco de Dados
```bash
python scripts/database.py
python scripts/verify_db.py
```

#### 5. Simular o ESP32 no Wokwi
- Abrir no VS Code com PlatformIO
- Compilar `src/prog1.ino`:
```bash
pio run
```
- Executar simulação Wokwi:
  - Umidade: < 50% (ex: 45%)
  - LDR: pH 6–7 (~50% slider)
  - Fósforo (D18), Potássio (D19): pressionar
- Monitor Serial: 
  - `Humidity: 45% | Phosphorus: 1 | Potassium: 1 | pH: 6.5 | Pump: 1`

#### 6. Executar o Dashboard Streamlit
```bash
streamlit run scripts/dashboard.py
```
Acesse: [http://localhost:8501](http://localhost:8501)

#### 7. Executar a Integração Climática
```bash
python scripts/weather_integration.py
```
Saída: `Irrigate? Yes` (se chuva < 1mm)

#### 8. Testar o Fluxo Completo
- Simular dados no Wokwi
- Inserir no banco via `database.py`
- Visualizar no dashboard
- Ajustar irrigação com `weather_integration.py`

---

## 🗃 Histórico de Lançamentos

- **1.0.0**: Projeto finalizado (simulação Wokwi, SQLite, dashboard, OpenWeather)
- **0.5.0**: Integração OpenWeather finalizada
- **0.4.0**: Dashboard com gráficos e tabela
- **0.3.0**: Banco SQLite com CRUD
- **0.2.0**: Lógica de irrigação no ESP32
- **0.1.0**: Estrutura inicial e Wokwi configurado

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
