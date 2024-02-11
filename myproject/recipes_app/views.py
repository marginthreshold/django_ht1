from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm


def recipe_list(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'recipes_app/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes_app/recipe_detail.html', {'recipe': recipe})


@login_required
def recipe_form(request, pk=None):
    recipe = None
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
        if request.user.username != recipe.author:
            return redirect('recipe_detail', pk=pk)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user.username
            new_recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(initial={'author': request.user.username})

    return render(request, 'recipes_app/recipe_form.html', {'form': form, 'recipe': recipe})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = SignUpForm()
    return render(request, 'recipes_app/signup.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('recipe_list')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('recipe_list')
    else:
        form = LoginForm()

    return render(request, 'recipes_app/login.html', {'form': form})

# class CustomLoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'recipes_app/login.html'
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         next_url = self.request.Get.get('next', None)
#         if next_url:
#             return redirect(next_url)
#         return response
