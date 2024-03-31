vocale='aeiou'
#consoanele sunt ordonate intr-un mod haotic pentru buna functionare si optimizare a programului !!!
consoane='mnrdzvlchsptbfgjkxy'#q si w nu exista
print('#################################################################\n'
'#                                                               #\n'
'#  _____ _____ _____ _______ _____ ____  _   _          _____   #\n'
'# |  __ \_   _/ ____|__   __|_   _/ __ \| \ | |   /\   |  __ \  #\n'
'# | |  | || || |       | |    | || |  | |  \| |  /  \  | |__) | #\n'
'# | |  | || || |       | |    | || |  | | . ` | / /\ \ |  _  /  #\n'
'# | |__| || || |____   | |   _| || |__| | |\  |/ ____ \| | \ \  #\n'
'# |_____/_____\_____|  |_|  |_____\____/|_| \_/_/_   \_\_|  \_\ #\n'
'# |___ \   / ____|         | |  / ____(_)     | (_)             #\n'
'#   __) | | (___  _   _  __| | | |     _  ___ | |_  __ _ _ __   #\n'
"#  |__ <   \___ \| | | |/ _` | | |    | |/ _ \| | |/ _` | '_ \  #\n"
'#  ___) |  ____) | |_| | (_| | | |____| | (_) | | | (_| | | | | #\n'
'# |____/  |_____/ \__,_|\__,_|  \_____|_|\___/|_|_|\__,_|_| |_| #\n'
'#                                                               #\n'
'#################################################################\n')
def treisud():
    text=input('Romana: ')
    shift=-1
    encrypted_text=''
    for char in text.lower():
        if not char.isalpha():
            encrypted_text+= char
        else:
            if char in vocale:
                #REGULA: e=i 
                if char == 'e':
                    encrypted_text+='i'
                #regula o=u
                elif char =='o':
                    encrypted_text+='u'
                else:
                    index=vocale.find(char)
                    new_index=(index +shift) %len(vocale)
                    encrypted_text+=vocale[new_index]
            if char in consoane:
                #REGULA: L=L
                if char=='l':
                    encrypted_text+= 'l'
                else:
                    index=consoane.find(char)
                    new_index=(index +shift) %len(consoane)
                    encrypted_text+= consoane[new_index]
    print(f'3 Sud Cioliana: {encrypted_text}') 
def romana():
    text=input('3 Sud Cioliana: ')
    shift=1
    check=0
    encrypted_text=''
    for char in text.lower():
        check+=1
        if not char.isalpha():
            encrypted_text+= char
        else:
            if char in vocale:
                #REGULA: i=e 
                if char == 'i':
                    encrypted_text+='e'
                else:
                    index=vocale.find(char)
                    new_index=(index +shift) %len(vocale)
                    encrypted_text+=vocale[new_index]
            if char in consoane:
                if char=='l' and check<len(text) - 1 and text[check-1] != text[check+1]:
                    encrypted_text+='l'            
                else:    #TO DO : daca l e intre doua vocale de acelasi fel, l=l 
                    index=consoane.find(char)
                    new_index=(index +shift) %len(consoane)
                    encrypted_text+= consoane[new_index]
    print(f'Romana: {encrypted_text}') 
print('1- Roamna => 3 Sud Cioliana\n'
      '2- 3 Sud Cioliana => Romana (BETA)')
choice=int(input('Alege dictionarul: '))
if choice==1:
    treisud()
if choice==2:
    romana()
