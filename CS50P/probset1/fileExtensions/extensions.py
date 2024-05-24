fname = input("File Name: ").split('.')

#? Search for the extension to get the MIME values
fname[-1] = fname[-1].lower()
match fname[-1].lower().strip():
    case "gif" | "png":
        print(f"image/{fname[-1]}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf"| "zip":
        print(f"application/{fname[-1]}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
