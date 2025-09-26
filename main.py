import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

entry = "这是我的第一次，硬编码日志"
log_entry = f"[{current_time}] {entry}\n"

with open("diary.txt", "a") as diary_file:
    diary_file.write(log_entry)

print("Diary entry saved successfully.")