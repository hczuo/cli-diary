#!/usr/bin/env python3
import datetime
import sys
from pathlib import Path

import os          # <--- 新增
import subprocess  # <--- 新增
import time        # <--- 新增


# 1. 获取用户的主目录 (例如 /Users/hczuo)
home_dir = Path.home()
# 2. 定义我们的日记存储文件夹
diary_dir = home_dir / ".cli-diary" # 用 / 运算符拼接路径，非常优雅
# 3. 确保这个文件夹存在，如果不存在就创建它
diary_dir.mkdir(exist_ok=True)

entry = ""

if len(sys.argv) > 1:
    entry = sys.argv[1]
else:
    # 创建一个临时的文件名
    temp_filename = f"diary_entry_{int(time.time())}.tmp"
    temp_file_path = diary_dir / temp_filename

    # 获取系统默认编辑器，如果没设置，就用 VS Code ('code')
    # `code -w` 中的 -w 参数是关键，它告诉 code 命令：
    # “打开文件，并等待我关闭文件后，再把控制权交还给调用你的程序”
    editor = os.environ.get("EDITOR", "code -w")
    
    # 构造并执行命令
    command = f"{editor} {temp_file_path}"
    subprocess.run(command, shell=True, check=True)

    # 编辑器关闭后，读取临时文件的内容
    if temp_file_path.exists():
        entry = temp_file_path.read_text(encoding="utf-8")
        temp_file_path.unlink() # 删除临时文件


if entry.strip(): # 确保内容不为空
    now = datetime.datetime.now()
    today_date_str = now.strftime("%Y-%m-%d")
    time_in_log = now.strftime("%H:%M:%S")
    log_entry = f"[{time_in_log}]\n{entry.strip()}\n\n" # 优化格式以支持多行

    filename = diary_dir / f"{today_date_str}.md" # <--- 改成 .md 文件，支持 Markdown！
    
    with open(filename, "a", encoding="utf-8") as diary_file:
        diary_file.write(log_entry)

    print(f"Diary entry saved to {filename}")
else:
    print("No entry provided. Diary not saved.")