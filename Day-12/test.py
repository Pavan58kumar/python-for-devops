def Update_Server_ConfigFile(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

Update_Server_ConfigFile("server.conf","MAX_CONNECTIONS", "1000")
