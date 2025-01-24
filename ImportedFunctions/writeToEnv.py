filePath = "./.env"

def writeToEnv(code):
    
    with open(filePath, "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            if line.startswith("AUTHCODE="):
                file.write(f"AUTHCODE={code}")
            else:
                file.write(line)