
def len_sentence(text) :
	if len(text)<25 :
		return 0
	return 1

def is_sentence(text):
	if text[0].isupper() and text[-1] in '!.?' :
		return 1
	return 0

def contain_symbole(text) :
	for char in text :
		if char in ['@', '#', '$', '%', '&', '*', '+', '-', '=', '/', '\\', '|', '_', '~', '^'] :
			return 1
	return 0
	
def is_acceptable_sentence(text) :
	return len_sentence(text) and is_sentence(text)  and not contain_symbole(text)


def get_all_sentences(texts) :
	index = 0
	sentences = []
	while index < len(texts) :
		sentence = ''
		for i,  char in enumerate(texts) :
			if char in '?.!' or i == len(texts) - 1 :
				sentence = texts[index:i+1]
				sentences.append(sentence)
				index = i+1
	return sentences
	
def correct_text(text):
	words = text.split() 
	no_space_after = "([{«'].}"
	no_space_before = "[(.,')»]?!{}…"
	text_corrige = words[0]
	for word in words[1:] :
		if len(text_corrige) != 0 and text_corrige[-1] in no_space_after :
			text_corrige +=word
		elif len(word) != 0 and word[0] in no_space_before :
			text_corrige += word
		else :
			text_corrige += ' '+word
	return text_corrige

def correct_all_text(tab_text) :
	_text = ''
	for text in tab_text :
		if is_acceptable_sentence(correct_text(text)) :
			_text += correct_text(text)+' ' 
		else:
			print("There's an syntaxically incorrect sentence. Be carreful!!!")
	return _text

def split_and_correct(text) :
	tab = get_all_sentences(text)
	return correct_all_text(tab)

#texts = input("Entrer une chaîne de plusieurs phrases qui commence par une Majuscule et se termine par soit ., ?, !: ")
texts = "Bonjour je suis en train d apprendre le Python et j aime beaucoup ca ! Ceci est une phrase avec beaucoup d ' espaces inutiles que tu dois nettoyer correctement. Le traitement de texte est tres important en data engineering et demande de la rigueur et de la precision ? Enfin voici une derniere phrase pour tester ton programme et verifier si tout fonctionne correctement !"
print(split_and_correct(texts))
