import pathlib
from datetime import datetime

import paramiko

pkey_path = pathlib.Path("/Users/meitec-yagisawa/.ssh/libronext_private.pem")
pkey = open(pkey_path, mode="r")
remote_dir = "/home/httpd/htdocs/books/"

# SFTP接続設定
cnf = {
    "host": "stg.libro-plus.com",
    "port": "10022",
    "user": "root",
    "pkey": paramiko.RSAKey.from_private_key(pkey, password="hoyusys"),
}

client = paramiko.SSHClient()
client.load_system_host_keys()


try:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=cnf["host"],
        port=cnf["port"],
        username=cnf["user"],
        pkey=cnf["pkey"],
    )
    ## SFTP セッション開始
    sftp_connection = client.open_sftp()
    files_info = sftp_connection.listdir(remote_dir)

    file_list = []
    for file_name in files_info:
        file_path = remote_dir + "/" + file_name
        # ファイル情報を取得
        file_stat = sftp_connection.stat(file_path)
        modify_dt = datetime.fromtimestamp(file_stat.st_mtime)
        file_list.append({"file_name": file_name, "modify_time": modify_dt})
    # stdin, stdout, stderr = client.exec_command("echo $PATH")
    # for line in stdout:
    #     print(line)
    print(file_list)

except:
    print("err")


finally:
    client.close()
