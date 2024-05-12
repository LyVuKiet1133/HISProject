import os


def start():
    try:
        file_path = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
        if os.path.exists(file_path):
            print("Open WinAppDriver.exe\n")
            os.startfile(file_path)
    except Exception as e:
        print("Encountered Exception\n")
        raise RuntimeError(e)


def stop():
    try:
        os.system("taskkill /f /IM WinAppDriver.exe")
    except Exception as e:
        raise RuntimeError(e)


'''if __name__ == "__main__":
    start()
    stop()
'''
