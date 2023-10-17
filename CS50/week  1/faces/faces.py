def main():
    raw = input('please tell me how are you feeling today ?')
    convert_face(raw)
    


def convert_face(raw) :
        raw = raw.replace(":)", "🙂").replace(":(","🙁")
        return print(raw)


  

main()


