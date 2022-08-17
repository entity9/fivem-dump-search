import os; current_path = os.getcwd(); lua_files = []; o_folders = []

def fast_scandir(current_path):
    for file in os.listdir(current_path):
        d = os.path.join(current_path, file)
        if os.path.isdir(d):
            o_folders.append(current_path + '\\' + file)
            fast_scandir(current_path + '\\' + file)

def find_luas(o_folders):
    for folder in o_folders:
        for dir in os.listdir(folder):
            if ".lua" in str(dir): lua_files.append(folder + "\\" + dir)

def search_engine(lua_files):
    keyword = (input("Keyword: ")).lower()
    print("")
    count = 0
    for i in lua_files:
        file = open(i, encoding='utf-8', errors='ignore')
        lua = (file.read()).lower()
        if keyword in lua:
            count += 1
            print(f"\n[{count}]", i.replace((str(os.getcwd()) + "\\"), ""))
            for item in lua.split("\n"):
                if keyword in item:
                    print(item.strip())
            print("")

fast_scandir(current_path); find_luas(o_folders); search_engine(lua_files)