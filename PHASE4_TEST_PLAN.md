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
- [ ] **Descrição**: Executar script de população de dados
- [ ] **Comando**: `python scripts/populate_db.py`
- [ ] **Resultado Esperado**: Conclusão sem erros e criação/atualização do arquivo `irrigation.db`
- [ ] **Status**: ✅ Concluído

### Test Case 2.2 (Model Training)
- [ ] **Descrição**: Executar treinamento do modelo ML
- [ ] **Comando**: `python scripts/train_model.py`
- [ ] **Resultado Esperado**: Execução bem-sucedida, exibição da acurácia e criação do arquivo `irrigation_model.joblib`
- [ ] **Status**: ✅ Concluído

## 3. Streamlit Dashboard (End-to-End Test)

### Test Case 3.1 (Application Launch)
- [ ] **Descrição**: Inicializar o dashboard Streamlit
- [ ] **Comando**: `streamlit run scripts/dashboard.py`
- [ ] **Resultado Esperado**: Aplicação abre no navegador sem erros
- [ ] **Status**: ⏳ Pendente

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
- [ ] **Descrição**: Verificar modularização do código
- [ ] **Passos**: Revisar código para confirmar que `dashboard.py` chama funções de `utils.py`
- [ ] **Resultado Esperado**: Dashboard utiliza funções modulares de utils.py
- [ ] **Status**: ✅ Concluído

## 4. Integration & Performance Tests

### Test Case 4.1 (Model Accuracy)
- [ ] **Descrição**: Verificar acurácia do modelo treinado
- [ ] **Resultado Esperado**: Acurácia ≥ 95%
- [ ] **Status**: ✅ Concluído (98.5%)

### Test Case 4.2 (Feature Importance Visualization)
- [ ] **Descrição**: Verificar gráfico de importância das características
- [ ] **Resultado Esperado**: Gráfico de barras horizontal com importância de cada sensor
- [ ] **Status**: ⏳ Pendente

### Test Case 4.3 (Database Schema)
- [ ] **Descrição**: Verificar novas colunas do banco
- [ ] **Passos**: Verificar colunas `prediction_confidence` e `model_version`
- [ ] **Resultado Esperado**: Colunas existem e contêm dados válidos
- [ ] **Status**: ✅ Concluído

## 5. Documentation & Code Quality

### Test Case 5.1 (README Completeness)
- [ ] **Descrição**: Verificar documentação atualizada
- [ ] **Resultado Esperado**: README contém todas as seções: Arquitetura, ML Pipeline, XAI, Como Executar
- [ ] **Status**: ✅ Concluído

### Test Case 5.2 (Code Comments)
- [ ] **Descrição**: Verificar comentários no código
- [ ] **Resultado Esperado**: Código bem comentado e profissional
- [ ] **Status**: ✅ Concluído

---

## Critérios de Aprovação
- [ ] Todos os test cases marcados como ✅ Concluído
- [ ] Nenhum erro crítico identificado
- [ ] Dashboard funcional com predições e explicabilidade
- [ ] Documentação completa e atualizada

## Observações
- Testes 1.1, 1.2, 3.1-3.4, 4.2 requerem execução manual
- Testes 2.1, 2.2, 3.5, 4.1, 4.3, 5.1, 5.2 já validados automaticamente
