import sqlite3

class Database:

    def __init__ (self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    async def execute(self, sql: str, parameters: tuple=tuple(),
                fetchone = False, fetchall = False, commit = False):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        elif fetchone:
            data = cursor.fetchone()
        elif fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    async def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS language (user_id INTEGER PRIMARY KEY,
              kind VARCHAR(6) NOT NULL);
              '''
        await self.execute(sql=sql, commit=True)

    async def drop_table(self):
        sql = 'DROP TABLE IF EXISTS language'
        await self.execute(sql=sql, commit=True)

    async def add_user(self, user_id):
        sql = '''INSERT INTO language(user_id, kind) VALUES(?, "uk")
        '''
        try:
            await self.execute(sql=sql, parameters = (user_id,), commit = True)
        except:
            pass

    async def get_user(self, user_id):
        sql = '''SELECT user_id FROM language WHERE user_id=?
        '''
        user= await self.execute(sql=sql, parameters = (user_id,), fetchone = True)
        if user:
            return user
        return False

    async def change_language(self, user_id, kind=None):
        sql = '''UPDATE language SET kind = ? WHERE user_id = ?
        '''
        await self.execute(sql=sql, parameters = (kind, user_id),commit=True)

    async def get_language(self, user_id):
        sql = '''SELECT kind FROM language WHERE user_id = ?
        '''
        return await self.execute(sql=sql, parameters=(user_id,), fetchone=True)