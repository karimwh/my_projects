def main():
    raw = input('please tell me how are you feeling today ?')
    convert_face(raw)
    


def convert_face(raw) :
        raw = raw.replace(":)",'happy').replace(":(",'sad')
        return print(raw)
    

main()


# could not past in the emojis in vscode for somereason