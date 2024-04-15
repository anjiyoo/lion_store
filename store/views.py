from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Category
from django.core.files.storage import FileSystemStorage

# def upload(request):
#     fs=FileSystemStorage()
#     uploaded_file = request.FILES['file']
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = fs.url(name)
#     return HttpResponse("{}에 저장이 잘 되었습니다.".format(url))

def add_food(request):
    # 요청이 GET방식으로 오면 페이지만 보여줌
    if request.method=='GET':
        return render(request=request, template_name='store/add_food.html')
    # 요청이 POST방식으로 오면 DB 값 추가(Products 테이블에 값 생성)
    elif request.method=='POST':
        # Food.objects.create(name='')
        # request.POST['']

        # Categofy 인스턴스 가져오기
        category = Category.objects.get(name=request.POST['category'])

        # Food 내용 구성
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        
        Food.objects.create(category=category, name=food_name, price=food_price , description=food_description, image_url=url)        
        return redirect('index')   

def food_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('index')      

def food_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'store/food_detail.html', context)
