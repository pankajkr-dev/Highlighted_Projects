import psutil

def show_memory_usage():
    mem = psutil.virtual_memory()
    print(f"🧠 Total RAM: {mem.total / (1024 ** 2):.2f} MB")
    print(f"✅ Available RAM: {mem.available / (1024 ** 2):.2f} MB")
    print(f"📊 Used RAM: {mem.used / (1024 ** 2):.2f} MB")
    print(f"💯 RAM Usage: {mem.percent}%")

if __name__ == "__main__":
    show_memory_usage()
