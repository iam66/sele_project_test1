favorite_language={'jason':'C','lisa':'python','linda':'java','holly':'.net'}
persons=['jason','cathy','john','holly','linda']
for person in persons:
    if person  in favorite_language.keys():
        print(person+" Tnanks for you cooperation")
    else:
        print(person+" We would like to invite you to our rolling.")
