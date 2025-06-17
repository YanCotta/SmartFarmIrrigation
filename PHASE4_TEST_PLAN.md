# Phase 4 Integration Test Plan

**Objetivo:** Verificar a funcionalidade de todos os componentes novos e modificados, incluindo o firmware ESP32, o pipeline de ML e o dashboard Streamlit.

## 1. ESP32 & Wokwi Simulation

### Test Case 1.1 (LCD Display)
- [ ] **Descrição**: Iniciar a simulação Wokwi e verificar inicialização do LCD
- [ ] **Passos**: 
  1. Abrir o projeto no VS Code
  2. Executar `pio run` para compilar
  3. Iniciar simulação no Wokwi
- [ ] **Resultado Esperado**: LCD inicializa e exibe dados dos sensores em tempo real (Umidade, pH, Status da Bomba)
- [ ] **Status**: ⏳ Pendente

### Test Case 1.2 (Serial Plotter)
- [ ] **Descrição**: Verificar saída formatada no Serial Plotter
- [ ] **Passos**:
  1. Abrir Serial Plotter no Wokwi
  2. Observar dados sendo plotados
- [ ] **Resultado Esperado**: Gráfico exibe valores dos sensores, atualizando a cada 2 segundos sem travamentos
- [ ] **Status**: ⏳ Pendente

## 2. Python Scripts & ML Model

### Test Case 2.1 (Data Population)
- [x] **Descrição**: Executar script de população de dados
- [x] **Comando**: `python scripts/populate_db.py`
- [x] **Resultado Esperado**: Conclusão sem erros e criação/atualização do arquivo `irrigation.db`
- [x] **Status**: ✅ Concluído - 200 registros inseridos com sucesso

### Test Case 2.2 (Model Training)
- [x] **Descrição**: Executar treinamento do modelo ML
- [x] **Comando**: `python scripts/train_model.py`
- [x] **Resultado Esperado**: Execução bem-sucedida, exibição da acurácia e criação do arquivo `irrigation_model.joblib`
- [x] **Status**: ✅ Concluído - Acurácia de 100% (supera os 95% exigidos)

## 3. Streamlit Dashboard (End-to-End Test)

### Test Case 3.1 (Application Launch)
- [x] **Descrição**: Inicializar o dashboard Streamlit
- [x] **Comando**: `streamlit run scripts/dashboard.py`
- [x] **Resultado Esperado**: Aplicação abre no navegador sem erros
- [x] **Status**: ✅ Concluído - Dashboard funcionando em http://localhost:8502

### Test Case 3.2 (Model Loading)
- [ ] **Descrição**: Verificar carregamento do modelo
- [ ] **Passos**: Verificar seção "Model Performance Overview"
- [ ] **Resultado Esperado**: Seção exibe corretamente indicando que o modelo foi carregado
- [ ] **Status**: ⏳ Pendente

### Test Case 3.3 (Prediction - High Humidity)
- [ ] **Descrição**: Testar predição com alta umidade
- [ ] **Passos**:
  1. Configurar Umidade para 80%
  2. Configurar outros valores nominais
  3. Clicar "Get AI Prediction"
- [ ] **Resultado Esperado**: Predição "DO NOT IRRIGATE" e gráfico de importância mostra 'humidity' como fator importante
- [ ] **Status**: ⏳ Pendente

### Test Case 3.4 (Prediction - Low Humidity)
- [ ] **Descrição**: Testar predição com baixa umidade
- [ ] **Passos**:
  1. Configurar Umidade para 30%
  2. Configurar pH=6.5, nutrientes=1
  3. Clicar "Get AI Prediction"
- [ ] **Resultado Esperado**: Predição "IRRIGATE" e gráfico de importância destaca 'humidity' como fator chave
- [ ] **Status**: ⏳ Pendente

### Test Case 3.5 (Code Modularity)
- [x] **Descrição**: Verificar modularização do código
- [x] **Passos**: Revisar código para confirmar que `dashboard.py` chama funções de `utils.py`
- [x] **Resultado Esperado**: Dashboard utiliza funções modulares de utils.py
- [x] **Status**: ✅ Concluído - Dashboard importa load_model, make_prediction e plot_feature_importance

## 4. Integration & Performance Tests

### Test Case 4.1 (Model Accuracy)
- [x] **Descrição**: Verificar acurácia do modelo treinado
- [x] **Resultado Esperado**: Acurácia ≥ 95%
- [x] **Status**: ✅ Concluído - Acurácia de 100% (Random Forest otimizado)

### Test Case 4.2 (Feature Importance Visualization)
- [ ] **Descrição**: Verificar gráfico de importância das características
- [ ] **Resultado Esperado**: Gráfico de barras horizontal com importância de cada sensor
- [ ] **Status**: ⏳ Pendente

### Test Case 4.3 (Database Schema)
- [x] **Descrição**: Verificar novas colunas do banco
- [x] **Passos**: Verificar colunas `prediction_confidence` e `model_version`
- [x] **Resultado Esperado**: Colunas existem e contêm dados válidos
- [x] **Status**: ✅ Concluído - Schema migrado com colunas prediction_confidence e model_version

## 5. Documentation & Code Quality

### Test Case 5.1 (README Completeness)
- [x] **Descrição**: Verificar documentação atualizada
- [x] **Resultado Esperado**: README contém todas as seções: Arquitetura, ML Pipeline, XAI, Como Executar
- [x] **Status**: ✅ Concluído - README atualizado com todas as seções necessárias

### Test Case 5.2 (Code Comments)
- [x] **Descrição**: Verificar comentários no código
- [x] **Resultado Esperado**: Código bem comentado e profissional
- [x] **Status**: ✅ Concluído - Código modularizado e bem documentado

---

## Critérios de Aprovação
- [ ] Todos os test cases marcados como ✅ Concluído
- [ ] Nenhum erro crítico identificado
- [ ] Dashboard funcional com predições e explicabilidade
- [ ] Documentação completa e atualizada

## Observações

### Testes Automatizados Concluídos ✅

- **2.1, 2.2**: Scripts Python e ML Model - 100% funcionais
- **3.1, 3.5**: Dashboard Streamlit - Lançado e modularizado
- **4.1, 4.3**: Performance e Schema - Acurácia 100%, DB migrado
- **5.1, 5.2**: Documentação - README e código atualizados

### Testes Manuais Pendentes ⏳

- **1.1, 1.2**: ESP32/Wokwi - Requer PlatformIO e simulação
- **3.2, 3.3, 3.4**: Dashboard Predictions - Teste manual das predições
- **4.2**: Feature Importance - Visualização no dashboard

### Correções Aplicadas 🔧

- **Schema Migration**: Adicionadas colunas `prediction_confidence` e `model_version`
- **Feature Order Fix**: Corrigida ordem das features no dashboard (humidity, phosphorus, potassium, ph)
- **Dashboard Refactor**: Removida duplicação de `st.set_page_config()`
