meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    meme_dict[word]
    print (meme_dict[word])
else:
   print ("этого слова у нас нет в базе данных, пожалуйста обратитесь вот по этой сылке : https://youtu.be/ech4bJ5g9V8?si=91Mg0XIAp8jDNtV2")
