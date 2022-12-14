from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(request):
    recipe = {}
    for search in DATA["omlet"]:
        recipe[search] = DATA["omlet"][search]
    servings = int(request.GET.get("servings", 1))
    for search in recipe:
        recipe[search] *= servings
    context ={
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    #special'no ostavil ra3nie varianti resheni9(tyt ne reali3ovanna fynkci9 otkata koli4estva ingridientov)
    recipe = DATA["buter"]
    servings = int(request.GET.get("servings", 1))
    for search in recipe:
        recipe[search] *= servings
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    recipe = DATA["pasta"]
    servings = int(request.GET.get("servings", 1))
    for search in recipe:
        recipe[search] *= servings
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
