import sqlite3
from ResourceFile import resource_path

class DatabaseManager:
    _instance = None  # Class-level attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialized = False  # Add initialization flag
        return cls._instance

    def __init__(self):
        # Only initialize once
        if not self._initialized:
            self.db_name = 'adanProgram.db'

            # create/connect to the database
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            
            # create general settings table if not exists
            cur.execute("CREATE TABLE if not exists general_settings(name TEXT, value TEXT)")
            con.commit()
            
            # create notification table
            cur.execute("CREATE TABLE if not exists notification (adan_index Integer, seconds Integer, date TEXT, duartion Integer, file_path TEXT, is_permanant Integer, noti_type Integer, active Integer, adan_duration Integer)")
            con.commit()

            cur.execute("CREATE TABLE if not exists adans_state (adan_index Integer, is_active Integer)")
            con.commit()
            
            # Add volume column to adans_sound table if it doesn't exist
            try:
                cur.execute("SELECT volume FROM adans_sound LIMIT 1")
            except sqlite3.OperationalError:
                try:
                    # Table exists but column doesn't, add it
                    cur.execute("ALTER TABLE adans_sound ADD COLUMN volume INTEGER DEFAULT 50")
                    con.commit()
                except sqlite3.OperationalError:
                    # Table doesn't exist, create it
                    cur.execute("CREATE TABLE if not exists adans_sound (adan TEXT, sound TEXT, volume INTEGER DEFAULT 50)")
                    con.commit()
            
            cur.execute("CREATE TABLE if not exists tokens (token TEXT)")
            con.commit()

            cur.execute('''CREATE TABLE if not exists app_version (id INTEGER PRIMARY KEY AUTOINCREMENT, version TEXT)''')
            con.commit()

            con.close()
            
            # add default values if table is empty
            if self.check_if_table_is_empty('general_settings'):
                self.initialize_general_settings()
            
            if self.check_if_table_is_empty('app_version'):
                self.initialize_app_version()
            
            if self.check_if_table_is_empty('adans_state'):
                self.initialize_adans_state()
            
            if self.check_if_table_is_empty('adans_sound'):
                self.initialize_adans_sound()

            self._initialized = True  # Mark the instance as initialized

    def get_token(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM tokens")
        records = res.fetchall()

        con.close()

        return records[0][0]
    
    def check_token(self):
        return self.check_if_table_is_empty('tokens')
    
    def save_token(self, token):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("INSERT INTO tokens VALUES(?)", [(token)])
        con.commit()

        con.close()

    def initialize_app_version(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        current_version = '0.1.0'
        
        cur.execute("INSERT INTO app_version (version) VALUES (?)", (current_version,))
        con.commit()

        con.close()

    def get_app_version(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT version FROM app_version")
        records = res.fetchone()

        con.close()
        return records[0]
        
    def update_app_version(self, new_version):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("UPDATE app_version SET version = ? WHERE id = ?", (new_version, 1))
        con.commit()

        con.close()
        return 

    def initialize_adans_sound(self):
        # Include default volume values (50%)
        data = [
            ("fajer_adan", "resources/sounds/azan2.mp3", 50), 
            ("dohor_adan", "resources/sounds/azan9.mp3", 50), 
            ("aser_adan", "resources/sounds/azan9.mp3", 50), 
            ("magreb_adan", "resources/sounds/azan9.mp3", 50), 
            ("ishaa_adan", "resources/sounds/azan9.mp3", 50)
        ]
        
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.executemany("INSERT INTO adans_sound VALUES(?, ?, ?)", data)

        con.commit()
        con.close()
        
    def get_adans_sound(self):

        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM adans_sound")
        records = res.fetchall()

        con.close()
        
        for record in records:
            print(record)

        return records

    def update_adans_sound(self, row_name, new_val=None, new_volume=None):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        if new_val is not None and new_volume is not None:
            # Update both sound path and volume
            cur.execute("UPDATE adans_sound SET sound = ?, volume = ? WHERE adan = ?", (new_val, new_volume, row_name))
        elif new_val is not None:
            # Update only sound path
            cur.execute("UPDATE adans_sound SET sound = ? WHERE adan = ?", (new_val, row_name))
        elif new_volume is not None:
            # Update only volume
            cur.execute("UPDATE adans_sound SET volume = ? WHERE adan = ?", (new_volume, row_name))

        con.commit()
        con.close()

    def get_settings_data(self):
        
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM general_settings")
        records = res.fetchall()

        con.close()

        return records

    def check_if_table_is_empty(self, table):
        
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute(f"SELECT COUNT(*) FROM {table}")        
        count = res.fetchone()[0]

        con.close()

        return count == 0

    def update_settings(self, row_name, new_value):

        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("UPDATE general_settings SET value = ? WHERE name = ?", (new_value, row_name))

        con.commit()
        con.close()
        
    def initialize_general_settings(self):
        
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        data = [
            ('masjed_name', "اسم المسجد"),
            ('city', "البلد"),
            ('quds_time_diff', '0'),
            ('is_summer_time', '1'),
            ('time_formate', '1'),
            ('is_pre_adan_sound_activated', '0')
        ]

        cur.executemany("INSERT INTO general_settings VALUES(?, ?)", data)

        con.commit()
        con.close()

    def intialize_keys(self):
        con = sqlite3.connect("adanProgram.db")
        cur = con.cursor()
        
        data = [('B0:5C:DA:1F:77:FB')]

        cur.execute("INSERT INTO sign_keys VALUES(?)", data)
        con.commit()

        con.close()
    
    def save_notification_in_db(self, noti_data):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("INSERT INTO notification VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", noti_data)
        con.commit()
        
        con.close()

    def update_notification(self, adan_index, seconds, row, new_val):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute(f"UPDATE notification SET {row} = ? WHERE adan_index = ? AND seconds = ?", (new_val, adan_index, seconds))

        con.commit()
        con.close()

    def change_noti_state(self, adan_index, minute, new_state):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("UPDATE notification SET active = ? WHERE adan_index = ? AND seconds = ?", (new_state, adan_index, minute))

        con.commit()
        con.close()

    def get_notifications(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM notification")
        records = res.fetchall()

        con.close()

        return records

    def delete_notification(self, notification):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("""
                    DELETE FROM notification WHERE adan_index = ? AND seconds = ?
                    """, (notification.get_index(), notification.get_seconds()))
        
        con.commit()
        con.close()
    
    def initialize_adans_state(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        data = [
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
        ]

        cur.executemany("INSERT INTO adans_state VALUES(?, ?)", data)

        con.commit()
        con.close()
    
    def get_adans_state(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM adans_state")
        records = res.fetchall()

        con.close()

        return records

    def update_adan_state(self, adan_index, is_active):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("UPDATE adans_state SET is_active = ? WHERE adan_index = ?", (is_active, adan_index))

        con.commit()
        con.close()
