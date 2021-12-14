from django.http import HttpResponse
from django.shortcuts import render, reverse

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


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать и рассчитать рецепт омлета': reverse('omlet'),
        'Показать и рассчитать рецепт пасты': reverse('pasta'),
        'Показать и рассчитать рецепт бутерброда': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
        'яйца, шт': 2 * servings,
        'молоко, л': 0.1 * servings,
        'соль, ч.л.': 0.5 * servings,
        }
    }
    return render(request, template_name, context)

def pasta_view(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
        'макароны, г': 0.3 * servings,
        'сыр, г': 0.05 * servings,
      },
    }
    return render(request, template_name, context)

def buter_view(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
        'хлеб, ломтик': 1 * servings,
        'колбаса, ломтик': 1 * servings,
        'сыр, ломтик': 1 * servings,
        'помидор, ломтик': 1 * servings,
      },
    }
    return render(request, template_name, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
