import uuid
import subprocess

def create_code_file(language,code):
    file_name=str(uuid.uuid4())+"."+language
    with open("code/"+file_name, "w") as f:
        f.write(code)
      
    return file_name

def execute_file(file_name, language):
    if language=="cpp":
        print("HI")
        result=subprocess.run(["g++","code/"+ file_name], stdout=subprocess.PIPE)
        if(result.returncode==1):
            #Compile time error
            return
        result=subprocess.run(["a.exe"], stdout=subprocess.PIPE)
        if(result.returncode!=0):
            #Runtime Error
            return
        print(result, result.returncode)
        return result.stdout.decode("utf-8")
        # subprocess.call(["a.exe"]) 
        