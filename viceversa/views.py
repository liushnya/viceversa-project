from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words_quantity = len(user_text.split())
	reversed_text = user_text[::-1]
	# print(test_get_text)
	return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text,
		'wordsquantity': words_quantity})