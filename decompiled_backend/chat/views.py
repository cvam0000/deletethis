from django.shortcuts import render,redirect


def index(request):
    if request.user.is_authenticated:
        
        return render(request,'chat/chat.html',{})
    else:
        a=redirect('login')
        return a





def telegram(requet):
	

	response = requests.post(
    url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
    data={'chat_id': 12345, 'text': 'hello friend'}
).json()