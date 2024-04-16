from django.shortcuts import render
from store.models import Category, Food  # store앱의 모델 가져오기
from .models import Cart
from django.http import JsonResponse

def customer_index(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'customer/index.html', context)

def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)

def add_cart(request):
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # 장바구니에 해당 음식 정보가 있으면 get(food=food)
    # 없으면 새로 생성해서 적용
    try:
        cart = Cart.objects.get(food=food)
    except:
        cart = Cart.objects.create(food=food)
    finally:
        pass
    cart.amount+=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)


def remove_cart(request):
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # cart, created = Cart.objects.get_or_create(food=food)
    cart, _ = Cart.objects.get_or_create(food=food)
    
    cart.amount-=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)


def modify_cart(request):
    # 어떤 음식(food_id)에 amount를 amountChange만큼 변경
    food_id= request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(food=food)
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    # 변경된 최종 결과를 반환(JSON)
    context = {
        'newQuantity':cart.amount,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)