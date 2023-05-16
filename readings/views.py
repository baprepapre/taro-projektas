from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q, F
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .models import Reading, Card, CardInstance
from .forms import UserUpdateForm
import random


def index(request):
    return render(request, 'index.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
            
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojas su vardu {username} jau užregistruotas')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, f'Vartotojas {username} sėkmingai užregistruotas')
                    return redirect('login')
            
        else:
            messages.error(request, 'Slaptažodžiai nesutampa')
            return redirect('register')
        
    return render(request, 'register.html')


class CardsListView(generic.ListView):
    model = Card
    template_name = 'all_cards.html'
    

def card(request, card_id):
    specific_card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card.html', {'card': specific_card})


def filter_by(request, attribute):
    cards = Card.objects.all()
    if attribute == 'major':
        cards = cards.filter(arcana='major')
    if attribute == 'minor':
        cards = cards.filter(arcana='minor')
    if attribute == 'wands':
        cards = cards.filter(suit='wands')
    if attribute == 'cups':
        cards = cards.filter(suit='cups')
    if attribute == 'swords':
        cards = cards.filter(suit='swords')
    if attribute == 'pentacles':
        cards = cards.filter(suit='pentacles')

    context = {
        'cards': cards,
        'attribute': attribute
    }
    return render(request, 'filter_cards.html', context=context)


def all_readings(request):
    return render(request, 'all_readings.html')


def one_card(request):
    all_cards = Card.objects.all()

    choice = random.sample(list(all_cards.values_list('pk', flat=True)), 1)

    chosen_card = CardInstance.objects.create(
        card = Card.objects.get(pk=choice[0]),
        position = random.choice(['', ', apversta'])
    )

    if request.user.is_authenticated:
        Reading.objects.create(
            type = 'Viena korta',
            cards = f'{chosen_card.card.name}{chosen_card.position}',
            user = request.user
        )

    return render(request, 'one_card.html', {'card': chosen_card})


def three_cards(request, reading_type):
    all_cards = Card.objects.all()

    choices = random.sample(list(all_cards.values_list('pk', flat=True)), 3)

    chosen_cards = CardInstance.objects.bulk_create(
        [
        CardInstance(
        card = Card.objects.get(pk=choices[0]),
        position = random.choice(['', ', apversta'])        
        ),
        CardInstance(
        card = Card.objects.get(pk=choices[1]),
        position = random.choice(['', ', apversta'])        
        ),
        CardInstance(
        card = Card.objects.get(pk=choices[2]),
        position = random.choice(['', ', apversta'])        
        )
        ]
    )

    reading_cards = []
    for card in chosen_cards:
        reading_cards.append(f'{card.card.name}{card.position}')
    reading_cards_str = ' | '.join(reading_cards)

    if reading_type == 1:
        reading_type_str = 'Praeitis, Dabartis, Ateitis'
    if reading_type == 2:
        reading_type_str = 'Jūs, Jūsų Kelias, Jūsų Potencialas'
    if reading_type == 3:
        reading_type_str = 'Situacija, Veiksmas, Baigtis'

    if request.user.is_authenticated:
        Reading.objects.create(
            type = reading_type_str,
            cards = reading_cards_str,
            user = request.user
        )

    context = {
        'card1': chosen_cards[0],
        'card2': chosen_cards[1],
        'card3': chosen_cards[2],
        'reading_type': reading_type
    }
    return render(request, 'three_cards.html', context=context)


class ReadingsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Reading
    template_name = 'my_readings.html'
    paginate_by = 11

    def get_queryset(self):
        return Reading.objects.filter(user=self.request.user).order_by(F('date').desc())
    

def delete_reading(request, reading_id):
    if request.method == 'POST':
        reading = Reading.objects.get(pk=reading_id)
        reading.delete()
        return redirect('my_readings')
    return render(request, 'delete_reading.html', {'reading_id': reading_id})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profilis sėkmingai atnaujintas')
            return redirect(to='profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'user_form': user_form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print('form valid')
        form.save()
        messages.success(self.request, 'Slaptažodis sėkmingai pakeistas')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        if 'old_password' in form.errors:
            messages.error(self.request, 'Dabartinis slaptažodis neteisingas')
        if 'new_password2' in form.errors:
            messages.error(self.request, 'Slaptažodžiai nesutampa')
        return super().form_invalid(form)
    

def search(request):
    query = request.GET.get('query')
    search_results = Card.objects.filter(Q(name__icontains=query))
    return render(request, 'search.html', {'cards': search_results, 'query': query})
