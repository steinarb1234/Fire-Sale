from category.models import Category
from user.models import User

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def user_info(request):
    user = User.objects.get(user_name=request.user)
    return {'user_information': user}
