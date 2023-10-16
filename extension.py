allowed_extension = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"}


file_name = input("Enter the name of the file: ")

file_extension = file_name.lower().split(".")[-1] if "." in file_name else ""


media_type = allowed_extension.get("." + file_extension, "application/octet-stream")

print(f"Media type for {file_name}: {media_type}")