
def correct_text(text):
	words = text.split() 
	no_space_after = "([{«'].}"
	no_space_before = "[(.,')»]{}…"
	text_corrige = words[0]
	for word in words[1:] :
		if len(text_corrige) != 0 and text_corrige[-1] in no_space_after :
			text_corrige +=word
		elif len(word) != 0 and word[0] in no_space_before :
			text_corrige += word
		else :
			text_corrige += ' '+word
	return text_corrige	
text = input("Saisir une phrase: ")
print(correct_text(text))


"""
text = "      Voici un exemple    (   avec des parenthèses   )     ,    des crochets   [   comme ceci  ]     , et des accolades     {      bien utilisées     }     .      On utilise aussi les guillemets français«    comme ça      ». Attention aux signes de ponctuation    ,      comme les virgules     , les points      , et les points de suspension        …"
_text = "Voici un exemple(avec des parenthèses), des crochets[comme ceci], et des accolades{bien utilisées}. On utilise aussi les guillemets français«comme ça».Attention aux signes de ponctuation, comme les virgules, les points, et les points de suspension…"
print(_text)
"""
