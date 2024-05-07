import sqlite3

CONN = sqlite3.connect('denver_restaurant_guide.db')
CURSOR = CONN.cursor()