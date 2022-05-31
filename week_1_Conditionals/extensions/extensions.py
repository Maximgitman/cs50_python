def main():
    extension_dict = {"gif" : "image/gif",
                      "jpg" : "image/jpeg",
                      "jpeg" : "image/jpeg", 
                      "png" : "image/png", 
                      "pdf" : "application/pdf", 
                      "txt" : "text/plain", 
                      "zip" : "application/zip", 
                      "other" : "application/octet-stream"
                      }
    
    file_name = input("File name: ").strip()
    file_extension = file_name.split(".")[-1].lower()

    if file_extension in extension_dict.keys():
        print(extension_dict[file_extension])
    else:
        print(extension_dict["other"])
    

    
main()