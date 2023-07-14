import sqlite3 as sql

class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, params = None):
        if TransactionObject.connected:
            if params == None:
                TransactionObject().cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, params)
            return True
        else:
            return False
    
    def fetchall(self):
        return TransactionObject.cur.fetchall()
    
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.commit()
            return True
        else:
            return False
        
    def initDB():
        trans = TransactionObject()
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()

    def insert(nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    def search(nome="", sobrenome="", email="", cpf=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
        trans.disconnect()

    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM clienes WHERE id = ?", (id))
        trans.persist()
        trans.disconnect()

    def update(id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()
    
    initDB()