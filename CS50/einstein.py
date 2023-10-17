def main():
    m = int(input('please input mass in kgs'))
    c = 300000000
    return ein(m,c)
    
 
def ein(m,c):
    e = m * (c**2)
    return print('your speed is {}'.format(e))

main()


    