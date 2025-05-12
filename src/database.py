import sqlite3

# Conectar ao banco
conn = sqlite3.connect('irrigation.db')
cursor = conn.cursor()

# Criar tabela alinhada ao MER simplificado
cursor.execute('''
CREATE TABLE IF NOT EXISTS irrigation_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    humidity REAL,          -- Correspondente a Leitura_Sensor (Tipo_Valor = 'umidade')
    phosphorus INTEGER,     -- Correspondente a Leitura_Sensor (Tipo_Valor = 'P')
    potassium INTEGER,      -- Correspondente a Leitura_Sensor (Tipo_Valor = 'K')
    ph REAL,                -- Correspondente a Leitura_Sensor (Tipo_Valor = 'pH')
    pump_state INTEGER,     -- Estado da bomba (lógica de irrigação)
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Funções CRUD
def create_data(humidity, phosphorus, potassium, ph, pump_state):
    cursor.execute('INSERT INTO irrigation_data (humidity, phosphorus, potassium, ph, pump_state) VALUES (?, ?, ?, ?, ?)',
                   (humidity, phosphorus, potassium, ph, pump_state))
    conn.commit()

def read_all():
    cursor.execute('SELECT * FROM irrigation_data')
    return cursor.fetchall()

def update_data(id, humidity=None, pump_state=None):
    if humidity is not None:
        cursor.execute('UPDATE irrigation_data SET humidity = ? WHERE id = ?', (humidity, id))
    if pump_state is not None:
        cursor.execute('UPDATE irrigation_data SET pump_state = ? WHERE id = ?', (pump_state, id))
    conn.commit()

def delete_data(id):
    cursor.execute('DELETE FROM irrigation_data WHERE id = ?', (id,))
    conn.commit()

# Exemplo de uso
if __name__ == "__main__":
    # Inserir dados simulados
    create_data(45.0, 1, 1, 6.5, 1)
    create_data(60.0, 0, 1, 7.2, 0)

    # Consultar dados
    print("Dados armazenados:")
    for row in read_all():
        print(row)

    # Atualizar um registro
    update_data(1, humidity=50.0)

    # Deletar um registro
    delete_data(2)

    conn.close()