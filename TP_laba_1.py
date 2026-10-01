from json import dump
from os import path
from platform import system, release, version, platform, machine

def get_info():
    os_name = system()
    if os_name == "Windows":
        os_name = "Windows"
    elif os_name == "Linux":
        os_name = "Linux"
    elif os_name == "Darwin":
        os_name = "macOS"
    else:
        os_name = "Не определена"
    return {
        "os": os_name,
        "os_release": release(),
        "os_version": version(),
        "platform": platform(),
        "architecture": machine()
    }

def save_json(data):
    file = path.join(path.dirname(path.abspath(__file__)), "os_info.json")
    with open(file, "w", encoding="utf-8") as f:
        dump(data, f, indent=4, ensure_ascii=False)
    return file

info = get_info()
file = save_json(info)

print("Информация сохранена, ура!")
print(f"Файл: {file}")
print(f"ОС: {info['os']}")