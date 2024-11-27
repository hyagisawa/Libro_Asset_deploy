import paramiko
import pathlib

pkey_path = pathlib.Path("/Users/meitec-yagisawa/.ssh/libronext_private.pem")
pkey = open(pkey_path, mode="r")

# SFTP接続設定
cnf = {
    "host": "stg.libro-plus.com",
    "port": "10022",
    "user": "root",
    "pkey": paramiko.RSAKey.from_private_key(pkey,password="hoyusys"),
}

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname=cnf["host"],
    port=cnf["port"],
    username=cnf["user"],
    pkey=cnf["pkey"],
)

stdin, stdout, stderr = client.exec_command("hostname")
for line in stdout:
    print(line)

client.close()

