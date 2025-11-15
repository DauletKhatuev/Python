import psutil
import platform
from datetime import datetime

def format_bytes(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024
    return f"{num:.1f} Y{suffix}"


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Информация о системе
    uname = platform.uname()
    lines = []
    lines.append(f"Timestamp: {now}")
    lines.append("=== System information ===")
    lines.append(f"System   : {uname.system}")
    lines.append(f"Node Name: {uname.node}")
    lines.append(f"Release  : {uname.release}")
    lines.append(f"Version  : {uname.version}")
    lines.append(f"Machine  : {uname.machine}")
    lines.append(f"Processor: {uname.processor}")
    lines.append("")
    
    #Информация о CPU
    lines.append("=== CPU ===")
    lines.append(f"Physical cores  : {psutil.cpu_count(logical=False)}")
    lines.append(f"Total coress    : {psutil.cpu_count(logical=True)}")
    lines.append(f"CPU usage (%)   : {psutil.cpu_percent(interval=1)}")
    lines.append("")
    
    #Память
    svmem = psutil.virtual_memory()
    lines.append("=== Memory ===")
    lines.append(f"Total      : {format_bytes(svmem.total)}")
    lines.append(f"Available  : {format_bytes(svmem.available)}")
    lines.append(f"Used       : {format_bytes(svmem.used)}")
    lines.append(f"Usage (%)  : {svmem.percent}%")
    lines.append("")
    
    #Диск
    disk = psutil.disk_usage("/")
    lines.append("=== Disk (/)===")
    lines.append(f"Total      : {format_bytes(disk.total)}")
    lines.append(f"Used       : {format_bytes(disk.used)}")
    lines.append(f"Free       : {format_bytes(disk.free)}")
    lines.append(f"Usage (%)  : {format_bytes(disk.percent)}%")
    
    #Записать результат в файл в текущей директории
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    

if __name__ == "__main__":
    main()
    