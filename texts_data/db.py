import sqlite3 
import subprocess
import shlex
import getpass
import os 

path = "/Users/stephie/Library/Messages/chat.db"
con = sqlite3.connect(path)

cur = con.cursor()
res = cur.execute("SELECT date, id, text from message left join handle on message.handle_id=handle.ROWID where handle.id='+8615504069017' AND message.is_from_me=1");
ret = res.fetchall()

#print(type(ret))
texts=[]

for line in ret:
	texts.append(line[2])

with open('s_text.txt','w') as f:
	for text in texts:
		f.write("%s\n" % text)
