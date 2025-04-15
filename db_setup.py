import os
import sqlite3

DATABASE = 'pc_parts.db'

def create_connection():
    """Создает подключение к базе данных SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        print(f"Подключение к базе данных {DATABASE} успешно установлено")
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return conn


def create_tables(conn):
    """Создание базы данных."""
    try:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cpus (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                socket TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS motherboards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                socket TEXT NOT NULL,
                ram_type TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ram (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ram_type TEXT NOT NULL,
                speed INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gpus (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                power_consumption INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS power_supplies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                wattage INTEGER NOT NULL
            )
        ''')

        conn.commit()
        print("Таблицы успешно созданы")

    except sqlite3.Error as e:
        print(f"Ошибка при создании таблиц: {e}")


def populate_tables(conn):
    """Заполняет таблицы тестовыми данными."""
    try:
        cursor = conn.cursor()

        def insert_if_not_exists(table_name, data, columns):
            """Вставляет данные, если они еще не существуют."""
            placeholders = ', '.join(['?'] * len(columns))
            select_query = f"SELECT 1 FROM {table_name} WHERE {' AND '.join([f'{col} = ?' for col in columns])}"
            cursor.execute(select_query, data)
            if cursor.fetchone() is None:  # Запись не существует
                insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                cursor.execute(insert_query, data)
                return True  # Данные вставлены
            return False  # Данные уже существуют

        cpus = [
            
            ('Intel Core i3-12100K', 'LGA1700'),
            ('Intel Core i5-12400K', 'LGA1700'),
            ('Intel Core i5-12600K', 'LGA1700'),
            ('Intel Core i7-12700K', 'LGA1700'),
            ('Intel Core i9-12900KS', 'LGA1700'),
            ('Intel Core i3-13100K', 'LGA1700'),
            ('Intel Core i5-13400K', 'LGA1700'),
            ('Intel Core i5-13600K', 'LGA1700'),
            ('Intel Core i7-13700K', 'LGA1700'),
            ('Intel Core i9-13900KS', 'LGA1700'),
            ('Intel Core i3-14100K', 'LGA1700'),
            ('Intel Core i5-14400K', 'LGA1700'),
            ('Intel Core i5-14600K', 'LGA1700'),
            ('Intel Core i7-14700K', 'LGA1700'),
            ('Intel Core i9-14900KS', 'LGA1700'),
            ('Intel Core Ultra 5 225K', 'LGA1851'),
            ('Intel Core Ultra 5 235K', 'LGA1851'),
            ('Intel Core Ultra 5 245K', 'LGA1851'),
            ('Intel Core Ultra 7 265K', 'LGA1851'),
            ('Intel Core Ultra 9 285K', 'LGA1851'),
            ('Intel Core Ultra 9 285KS', 'LGA1851'),

            ('AMD Ryzen 5 5500', 'AM4'),
            ('AMD Ryzen 5 5600', 'AM4'),
            ('AMD Ryzen 5 5600X', 'AM4'),
            ('AMD Ryzen 7 5700', 'AM4'),
            ('AMD Ryzen 7 5700X', 'AM4'),
            ('AMD Ryzen 7 5800X', 'AM4'),
            ('AMD Ryzen 9 5900X', 'AM4'),
            ('AMD Ryzen 9 5950X', 'AM4'),
            ('AMD Ryzen 5 7500f', 'AM5'),
            ('AMD Ryzen 5 7600', 'AM5'),
            ('AMD Ryzen 5 7600X', 'AM5'),
            ('AMD Ryzen 7 7700', 'AM5'),
            ('AMD Ryzen 7 7700X', 'AM5'),
            ('AMD Ryzen 7 7800X', 'AM5'),
            ('AMD Ryzen 9 7900X', 'AM5'),
            
            ('AMD Ryzen 5 9600', 'AM5'),
            ('AMD Ryzen 5 9600X', 'AM5'),
            ('AMD Ryzen 7 9700', 'AM5'),
            ('AMD Ryzen 7 9700X', 'AM5'),
            ('AMD Ryzen 7 9800X', 'AM5'),
            ('AMD Ryzen 9 9900X', 'AM5'),
            ('AMD Ryzen 9 9950X', 'AM5'),
            ('AMD Ryzen 7 9800X3D', 'AM5'),
            ('AMD Ryzen 9 9900X3D', 'AM5'),
            ('AMD Ryzen 9 9950X3D', 'AM5'),
            ('AMD Ryzen 7 7800X3D', 'AM5'),
            ('AMD Ryzen 9 7900X3D', 'AM5'),
            ('AMD Ryzen 9 7950X3D', 'AM5'),
            ('AMD Ryzen 9 7950X', 'AM5')
        ]

        for name, socket in cpus:
            if insert_if_not_exists('cpus', (name, socket), ['name', 'socket']):
                print(f"Процессор '{name}' добавлен.")
            else:
                print(f"Процессор '{name}' уже существует.")

        motherboards = [
            ('ASUS ROG Strix Z690-A Gaming WiFi', 'LGA1700', 'DDR5'),
            ('ASUS ROG Strix B760-G', 'LGA1700', 'DDR4'),
            ('ASUS TUF Gaming Z790-Plus', 'LGA1700', 'DDR4'),
            ('Gigabyte B550 Gaming X V2', 'AM4', 'DDR4'),
            ('ASUS ROG Strix Z690-A Gaming WiFi', 'LGA1700', 'DDR5'),
            ('ASUS ROG Strix B760-G', 'LGA1700', 'DDR4'),
            ('GIGABYTE Z890 AORUS ELITE WIFI7', 'LGA1851', 'DDR5'),
            ('ASUS ROG STRIX Z890-E GAMING WIFI', 'LGA1851', 'DDR5'),
            ('ASUS TUF GAMING B860-PLUS WIFI', 'LGA1851', 'DDR5'),
            ('MSI MAG B860 TOMAHAWK WIFI', 'LGA1851', 'DDR5'),
            ('ASUS ROG Strix B760-G', 'LGA1700', 'DDR4'),
            
            ('MSI X870 GAMING PLUS WIFI', 'AM5', 'DDR5'),
            ('MSI MPG B550 GAMING PLUS', 'AM4', 'DDR4'),
            ('ASUS PRIME H610M-K D4', 'LGA1700', 'DDR4'),
            ('Gigabyte A520M DS3H', 'AM4', 'DDR4'),
            ('Asrock A520M-HDV', 'AM4', 'DDR4'),
            ('ASUS ROG Maximus Z790 Hero', 'LGA1700', 'DDR5'),
            ('ASUS ROG Crosshair X670E Hero', 'AM5', 'DDR5')
        ]

        for name, socket, ram_type in motherboards:
            if insert_if_not_exists('motherboards', (name, socket, ram_type), ['name', 'socket', 'ram_type']):
                print(f"Материнская плата '{name}' добавлена.")
            else:
                print(f"Материнская плата '{name}' уже существует.")

        ram = [
            ('Corsair Vengeance LPX 16GB (2x8GB) DDR4 3200MHz', 'DDR4', 3200),
            ('G.Skill Trident Z5 32GB (2x16GB) DDR5 6000MHz', 'DDR5', 6000),
            ('ADATA XPG SPECTRIX D35G RGB (2x8GB) DDR4 3200MHz', 'DDR4', 3200),
            ('ADATA XPG SPECTRIX D35G RGB (2x16GB) DDR4 3200MHz', 'DDR4', 6000),
            ('ADATA XPG SPECTRIX D35G RGB (2x16GB) DDR4 3600MHz', 'DDR4', 6000),
            ('FURY Beast Black RGB (2x16GB) DDR4 3600MHz', 'DDR4', 6000),
            ('ADATA XPG SPECTRIX D35G RGB (2x8GB) DDR4 3600MHz', 'DDR4', 6000),
            ('ADATA XPG Lancer RGB (2x16GB) DDR4 6000MHz', 'DDR4', 6000),
            ('ADATA XPG Lancer RGB (2x16GB) DDR5 5600MHz', 'DDR5', 5600),
            ('ADATA XPG SPECTRIX D35G RGB (2x16GB) DDR5 6000MHz', 'DDR5', 6000),
            ('FURY Beast Black RGB (2x16GB) DDR5 5600MHz', 'DDR5', 5600),
            ('FURY Beast Black RGB (2x16GB) DDR5 6600MHz', 'DDR5', 6600),
            ('ADATA XPG Lancer RGB (2x16GB) DDR5 6000MHz', 'DDR5', 6000),
            ('G.Skill Trident Z5 16GB (2x8GB) DDR5 6600MHz', 'DDR5', 6600),
            ('Kingston Fury Beast 16GB (2x8GB) DDR5 5200MHz', 'DDR5', 5200),
            ('Crucial Ballistix 16GB (2x8GB) DDR4 3600MHz', 'DDR4', 3600)
        ]
        for name, ram_type, speed in ram:
            if insert_if_not_exists('ram', (name, ram_type, speed), ['name', 'ram_type', 'speed']):
                print(f"ОЗУ '{name}' добавлена.")
            else:
                print(f"ОЗУ '{name}' уже существует.")

        gpus = [
            ('NVIDIA GeForce RTX 2070Super', 215),
            ('NVIDIA GeForce RTX 2070', 175),
            ('NVIDIA GeForce RTX 2080', 215),
            ('NVIDIA GeForce RTX 2080Super', 250),
            ('NVIDIA GeForce RTX 2060', 160),
            ('NVIDIA GeForce RTX 2060super', 175),
            
            ('NVIDIA GeForce RTX 3070', 220),
            ('NVIDIA GeForce RTX 3080', 320),
            ('NVIDIA GeForce RTX 3060', 170),
            ('NVIDIA GeForce RTX 3060ti', 200),
            ('NVIDIA GeForce RTX 3070', 220),
            
            ('NVIDIA GeForce RTX 3090', 350),
            ('NVIDIA GeForce RTX 3050', 130),
            ('NVIDIA GeForce RTX 4080', 320),
            ('NVIDIA GeForce RTX 4060', 115),
            ('NVIDIA GeForce RTX 4060ti', 165),
            ('NVIDIA GeForce RTX 4070', 200),
            ('NVIDIA GeForce RTX 4070ti', 285),
            ('NVIDIA GeForce RTX 4070Super', 220),
            ('NVIDIA GeForce RTX 4070ti Super', 285),
            ('NVIDIA GeForce RTX 4080SUPER', 320),
            ('NVIDIA GeForce RTX 4090', 450),
            ('AMD Radeon RX 7900 XTX', 355),
            ('AMD Radeon RX 7900 XT', 300),
            ('AMD Radeon RX 6950 XT', 335),
            ('AMD Radeon RX 6900 XT', 300),
            ('AMD Radeon RX 7800 XT', 263),
            ('AMD Radeon RX 6800 XT', 300),
            ('AMD Radeon RX 7700 XT', 245),
            ('AMD Radeon RX 6700 XT', 230),
            ('AMD Radeon RX 7600 XT', 190),
            ('AMD Radeon RX 6600 XT', 160),
            ('AMD Radeon RX 7600 ', 165),
            ('AMD Radeon RX 6600 ', 132),
            ('AMD Radeon RX 5700 XT', 225),
            ('AMD Radeon RX 5700 ', 180),
            ('AMD Radeon RX 5600 XT', 150),
            ('AMD Radeon RX 5500 XT', 130),
            ('AMD Radeon RX 5500', 130)
        ]
        for name, power_consumption in gpus:
            if insert_if_not_exists('gpus', (name, power_consumption), ['name', 'power_consumption']):
                print(f"Видеокарта '{name}' добавлена.")
            else:
                print(f"Видеокарта '{name}' уже существует.")

        power_supplies = [
            ('Corsair RM750x (2021)', 750),
            ('Seasonic FOCUS GX-850', 850),
            ('be quiet! Straight Power 11 1000W', 1000),
            ('Cougar GEX850', 850),
            ('Thermaltake Toughpower GF3 1000W', 1000),
            (' DEEPCOOL GamerStorm PN1200M', 1200),
            ('Thermaltake Toughpower GT 850W Snow', 850),
            ('ZALMAN TeraMax II 1000W', 1000),
            ('Thermaltake Toughpower PF1 ARGB 850W', 850),
            ('Thermaltake Toughpower GF 650W', 650),
            ('DEEPCOOL PQ1000M', 1000),
            ('DEEPCOOL PX1000G', 1000),
            ('DEEPCOOL PQ850M', 850),
            ('DEEPCOOL PM750D', 750),
            ('DEEPCOOL PN750D', 750),
            ('Thermaltake Toughpower GF 750W', 750),
            ('DEEPCOOL PN650M', 650),
            ('EVGA SuperNOVA 650 GA', 650)
        ]


        for name, wattage in power_supplies:
            if insert_if_not_exists('power_supplies', (name, wattage), ['name', 'wattage']):
                print(f"Блок питания '{name}' добавлен.")
            else:
                print(f"Блок питания '{name}' уже существует.")

    except sqlite3.Error as e:
        print(f"Ошибка при заполнении таблиц: {e}")


def main():
    # Добавляем удаление базы данных, если она существует
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print(f"Удалена существующая база данных: {DATABASE}")

    conn = create_connection()
    if conn:
        create_tables(conn)
        populate_tables(conn)  # Вызываем populate_tables здесь
        conn.close()
        print("Все операции с базой данных успешно завершены.")
    else:
        print("Не удалось установить соединение с базой данных.")



if __name__ == "__main__":
    main()
