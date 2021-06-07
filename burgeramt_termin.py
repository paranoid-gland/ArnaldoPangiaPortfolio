import random
excuse_list = ["Entschuldigung",
               "Entschuldung",
               "Entschuldame mucho",
               "Entschulderino",
               "Entschul... ja",
               "Enschulgung",
               "Untschuldengung",
               "I'm sorry",
               "Enschuldingungen Sie mir, danke",
               "please, have mercy",
               "Schuldugung",
               "Schuldung"]

spreche_wrong_list = ["spreche",
                 "... uh... speak...",
                 "sprachen",
                 "spruch",
                 "sprecherino",
                 "spreicho",
                 "spresche",
                 "hablo",
                 "kann sprechen",
                 "spr...sprach...sprech... sprachen",
                 "spreak",
                 "spock",
                 "spups"]

brauche_wrong_list = ["brauche",
                      "bracchio",
                      "braucherino",
                      "brennwert",
                      "breuche",
                      "brodo",
                      "broche"
                      "br...brouch...brauch...broucho",
                      "brant",
                      "... uh, need",
                      "willen wollen",
                      "necessito"]

document_part1_list = ["An",
                       "Auf",
                       "Über",
                       "Unter",
                       "Zwischen",
                       "Ab",
                       "An",
                       "Durch",
                       "Arbeitslos",
                       ]

document_part2_list = ["meldung",
                       "bewerbung",
                       "ordnung",
                       "rechtigung",
                       "schutz",
                       "gemein",
                       "haustier",
                       "antrag",
                       "rechti"]

document_part3_list = ["schein",
                       "gung",
                       "schaft",
                       "stelle",
                       "bescheidigung",
                       "keit",
                       ]

exclamation_list = ["Holy Moly Guacamoley",
                    "¡Madre de Dios",
                    "What?",
                    "Wie, Bitta?",
                    "W...was?",
                    "Ma che cazzo ...?",
                    "Oh putain...",
                    "Oh for Pete's sake",
                    "Was",
                    "Say whaaaaaaaaat?",
                    "Scheißerino!"]

was_ist_das_wrong_list = ["Wat it das",
                          "Was ist das",
                          "Was ist was",
                          "Was ist",
                          "Wasserino ist dasserino",
                          "Walter ist das",
                          "Wasserino ist das",
                          "Was ist es",
                          "Das ist was",
                          "Was...Was it ist"]

def dialogue_part1():
    excuse_marker = random.choice(range(len(excuse_list)))
    spreche_wrong_marker = random.choice(range(len(spreche_wrong_list)))

    return "- Guten Tag! {}, Ich {} nur ein bisschen deutsch.".format(excuse_list[excuse_marker], spreche_wrong_list[spreche_wrong_marker])
    return "- Naja. Was brauchen Sie?"


#excuse_marker= random.choice(range(len(excuse_list)))
#spreche_wrong_marker = random.choice(range(len(spreche_wrong_list)))

#print("- Guten Tag! {}, Ich {} nur ein bisschen deutsch."
#      .format(excuse_list[excuse_marker], spreche_wrong_list[spreche_wrong_marker]))

#print("- Naja. Was brauchen Sie?")

def dialogue_part2():
    brauche_wrong_marker= random.choice(range(len(brauche_wrong_list)))
    document_part1_marker = random.choice(range(len(document_part1_list)))
    document_part2_marker = random.choice(range(len(document_part2_list)))
    document_part3_marker = random.choice(range(len(document_part3_list)))

    return "- Ich {} ein {}{}{}.".format(brauche_wrong_list[brauche_wrong_marker],
              document_part1_list[document_part1_marker],document_part2_list[document_part2_marker],document_part3_list[document_part3_marker]))

def dialogue_part3():
    document_part1_marker = random.choice(range(len(document_part1_list)))
    document_part2_marker = random.choice(range(len(document_part2_list)))
    document_part3_marker = random.choice(range(len(document_part3_list)))

    return "- Haben Sie die {}{}{} mitgebracht?".format(document_part1_list[document_part1_marker],document_part2_list[document_part2_marker], document_part3_list[document_part3_marker])

def dialogue_part4():
    exclamation_marker = random.choice(range(len(exclamation_list)))
    was_ist_das_wrong_marker = random.choice(range(len(was_ist_das_wrong_list)))
    return "- {}! {}?"
      .format(exclamation_list[exclamation_marker], was_ist_das_wrong_list[was_ist_das_wrong_marker])
    return "- Ohne {}{}{} kann ich nichts machen. Nehmen Sie einen anderen Termin und kommen Sie zurück.".format(document_part1_list[document_part1_marker],document_part2_list[document_part2_marker],document_part3_list[document_part3_marker])
    return"  Nächster!"
