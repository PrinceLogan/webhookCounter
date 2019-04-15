#!/usr/bin/python3

import sqlite3
import json

sqlite_file = 'db.sqlite3'    # name of the sqlite database file

def take_latest():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('select body from destinationWebhook_webhooktransaction WHERE   ID = (SELECT MAX(ID)  FROM destinationWebhook_webhooktransaction)')
    count_results = c.fetchall()
    conn.commit()
    conn.close()
    cr_2 = [item for resp in count_results for item in resp]
    cr_2 = str(cr_2[0])

    y = json.loads(cr_2)
    jack = y['uuid']
    judy = y['source']
    
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('INSERT INTO destinationWebhook_packagestring (string_uuid, source) VALUES ("{0}", "{1}")'.format(jack,judy))
    conn.commit()
    conn.close()

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('DELETE FROM destinationWebhook_webhooktransaction WHERE   ID = (SELECT MAX(ID)  FROM destinationWebhook_webhooktransaction)')
    conn.commit()
    conn.close()

def poll_latest():
    global HankHill1
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('select count(*) from destinationWebhook_webhooktransaction')
    row_num = c.fetchall()
    HankHill1 = [item for resp in row_num for item in resp]
    HankHill1 = int(HankHill1[0])
    conn.commit()
    conn.close()

poll_latest()

while HankHill1 > 0:
    take_latest()
    poll_latest()
#else:
#    pass

