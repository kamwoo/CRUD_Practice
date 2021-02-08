from django.shortcuts import render
from .forms import *

# Create your views here.
# CRUD Create, Update는 입력받을려면 form태그가 필요하다.

def register(request):
    if request.method == "POST":
        # 회원가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # 필수 필드가 다 입력되었는지 확인
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
            # 2번째 인자 파일로 new_user의 정보들을 new_user라는 이름으로 넘겨준다.
    else:
        # 회원가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})