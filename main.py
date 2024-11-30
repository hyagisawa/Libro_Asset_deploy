import os
import sys
import tkinter as tk
import tkinter.filedialog
from datetime import datetime
from pathlib import Path
from tkinter import messagebox

import paramiko

msg_not_found_pKye = "サーバへ接続するための秘密鍵が見つかりません\n処理を中断します"

host_name: str = "stg.libro-plus.com"
prt_number: str = "10022"
user_name: str = "root"
passphrase: str = "hoyusys"
pKey_name: str = "libronext_private.pem"
remote_dir = "/home/httpd/htdocs/books/"  # サーバ側のターゲットディレクトリ


def main() -> None:
    root = tk.Tk()
    root.withdraw()
    ssh_pKye = Path(os.path.expanduser("~")).joinpath(f".ssh/{pKey_name}")

    if ssh_pKye.exists == False:
        # 秘密鍵が見つからないときは処理中断
        messagebox.showerror(msg_not_found_pKye)
        sys.exit()

    with open(ssh_pKye, mode="r") as f:
        pkey = f

    # SFTP接続設定
    cnf = {
        "host": host_name,
        "port": prt_number,
        "user": user_name,
        "pkey": paramiko.RSAKey.from_private_key(pkey, password=passphrase),
    }


if __name__ == "__main__":
    sys.exit(main())

    # pkey_path = pathlib.Path("/Users/meitec-yagisawa/.ssh/libronext_private.pem")
    # pkey = open(pkey_path, mode="r")
    # remote_dir = "/home/httpd/htdocs/books/"

    # # SFTP接続設定
    # cnf = {
    #     "host": "stg.libro-plus.com",
    #     "port": "10022",
    #     "user": "root",
    #     "pkey": paramiko.RSAKey.from_private_key(pkey, password="hoyusys"),
    # }

    # client = paramiko.SSHClient()
    # client.load_system_host_keys()

    # try:
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect(
    #         hostname=cnf["host"],
    #         port=cnf["port"],
    #         username=cnf["user"],
    #         pkey=cnf["pkey"],
    #     )
    #     ## SFTP セッション開始
    #     sftp_connection = client.open_sftp()
    #     files_info = sftp_connection.listdir(remote_dir)

    #     file_list = []
    #     for file_name in files_info:
    #         file_path = remote_dir + "/" + file_name
    #         # ファイル情報を取得
    #         file_stat = sftp_connection.stat(file_path)
    #         modify_dt = datetime.fromtimestamp(file_stat.st_mtime)
    #         file_list.append({"file_name": file_name, "modify_time": modify_dt})
    #     # stdin, stdout, stderr = client.exec_command("echo $PATH")
    #     # for line in stdout:
    #     #     print(line)
    #     print(file_list)

    # except:
    #     print("err")

    # finally:
    #     client.close()
