from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class형은 mixin, 함수형은 decorator
# Create your views here.
from .models import Photo

@login_required
def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    # photo object에서 orm관련 메니져이름이 기본이 object이다. all()부분이 query부분
    # photo model의 object메니져에게 전부 달라고 요청한다.
    return render(request, 'photo/list.html',{'photos':photos})
    # template 밑의 photo의 html # 불러온 photos 변수를 html 안에서 photos라고 쓰겠다.

class PhotoUpLoadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text'] # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'

    def form_valid(self, form): # 입력된 정보가 올바르면 저장하는 함수
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 데이터가 올바르다면 저장
            form.instance.save()
            return redirect('/') #루트로 가게 한다.
        else:
            return self.render_to_response({'form':form}) # 방금 입력받은 form을 그대로 돌려준다.

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

