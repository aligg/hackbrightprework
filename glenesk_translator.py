lan_dictionary = {'cat': 'ota', 'dog': 'kelb', 'hello': 'marhaba', 'goodbye': 'masalama', 'food': 'ekl', 'Egypt': 'masr', 'shoe': 'gazma', 'terrorism': 'irhab', 'program': 'birnamij', 'state': 'wilaya'}

def translate(word): 
    if word in lan_dictionary:
        print lan_dictionary[word]
    else: 
        print 'No such word!'

 translate('cat')
