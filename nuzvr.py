import json

def GetImageByName(pokedex, alternateForms, pokeName):
    for pokemon in pokedex:
        if pokeName == pokemon['name']:
            return GenerateImageLink(FormatNumber(pokemon['id'])) + ' ' + pokeName
        elif pokeName == 'Mega ' + pokemon['name'] or pokeName == 'Primal ' + pokemon['name'] or pokeName == 'Alolan ' + pokemon['name']:
            return GenerateImageLink(FormatNumber(pokemon['id']) + MegaOrPrimalOrAlolan(pokeName)) + ' ' + pokeName
    
    for pokemon in alternateForms:
        if pokeName == pokemon['name']:
            return pokemon['image'] + ' ' + pokeName

def GetInputFile(filename = 'pokemon.txt'):
    pokemon = []
    with open(filename, 'r', encoding='utf8') as fp:
        for line in fp:
            pokemon.append(line.rstrip('\n'))
    return pokemon

def GetAlternateForms():
    with open('alternate-forms.json', 'r') as fp:
        forms = json.load(fp)
        return forms

def FormatNumber(val):
    if 10 < val < 100:
        return '0' + str(val)
    elif val < 10:
        return '00' + str(val)
    else:
        return str(val)

def MegaOrPrimalOrAlolan(pokeName):
    if 'Mega ' in pokeName:
        return '-m'
    elif 'Primal ' in pokeName:
        return '-p'
    elif 'Alolan ' in pokeName:
        return '-a'
    else:
        return ''

def GenerateImageLink(dexNum):
    return '[img]https://www.serebii.net/pokedex-sm/icon/' + dexNum + '.png[/img]'

def main():
    open('output.txt', 'w').close()
    with open('pokedex.json', 'r', encoding='utf8') as dexFile:
        pokedex = json.load(dexFile)
        alt = GetAlternateForms()
        instructions = 'Put the list of Pokemon in pokemon.txt. Give each Pokemon its own line. \n- Megas should be in the format \'Mega Lucario\', same goes for Primals.\n- Alolan Forms should be in the format \'Alolan Marowak\'.\n- The following alternate forms are accepted: '
        formsList = []
        for form in alt:
            formsList.append(form['name'])
        alternateForms = (', ').join(formsList)
        
        print(instructions, end='')
        print(alternateForms)
        # filename = input('File name: ')
        inputPokemon = GetInputFile()

        for pokemon in inputPokemon:
            with open('output.txt', 'a') as fp:
                fp.write(GetImageByName(pokedex, alt, pokemon) + '\n')

main()