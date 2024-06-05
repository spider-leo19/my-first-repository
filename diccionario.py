meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "SPEEDRUN":"Pasarte rapido algo o hacer algo rapido",
            "CREEPY":"aterrador, siniestro"
            "F":"fallaste"
    
}
            
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("Esa palbra significa", meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no se encuentra en el meme_dict")
