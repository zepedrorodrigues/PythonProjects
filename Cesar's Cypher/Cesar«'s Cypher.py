alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'

alphabet_lower_final = []

for x in alphabet_lower:
    alphabet_lower_final.append(x)

def cesars_code (message_lower,code_decypher,cypher):
    message_final = ''
    if code_decypher=='1':
        for x in range(len(message_lower)):
            letter = message_lower[x]
            if letter in alphabet_lower_final:
                ind = alphabet_lower_final.index(letter)
                message_final = message_final + alphabet_lower_final[(ind+cypher)%26]
            else:
                message_final = message_final + ' '
        return message_final 
    elif code_decypher == '2':
        for x in range(len(message_lower)):
            letter = message_lower[x]
            if letter in alphabet_lower_final:
                ind = alphabet_lower_final.index(letter)
                message_final = message_final + alphabet_lower_final[(ind-cypher)%26]
            else:
                message_final = message_final + ' '        
        return message_final



message = input('Insert the message:\n ')
message_lower = message.lower()
code_decypher = input('\n Do you want to:\n1.Decrypt\n2.Cypher\n')
cypher = int(input('\nWhat is the code cypher?\n'))
print(cesars_code(message,code_decypher,cypher))



