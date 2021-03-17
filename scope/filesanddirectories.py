import os


def list_directories(s):  # S is the directory name

    def dir_list(d):
        nonlocal tab_stop  # tab_stop var is not local, and is also not global, it is in the closing scope
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)  # Combining directory and the file in output
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0  # TAB STOP IS DEFINED HERE!!!
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


list_directories('.')


