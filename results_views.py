from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import PollingUnit, AnnouncedPuResults, Lga
from .forms import PollingUnitForm

def polling_unit_results(request, uniqueid):
    polling_unit = PollingUnit.objects.get(uniqueid=uniqueid)
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_unit)
    context = {'polling_unit': polling_unit, 'results': results}
    return render(request, 'results/polling_unit_results.html', context)

def lga_results(request):
    lgas = Lga.objects.filter(state_id=25)  # Delta State
    selected_lga_id = request.GET.get('lga')
    results = None
    if selected_lga_id:
        results = AnnouncedPuResults.objects.filter(
            polling_unit_uniqueid__lga_id=selected_lga_id
        ).values('party_abbreviation').annotate(total_score=Sum('party_score'))
    context = {'lgas': lgas, 'results': results, 'selected_lga_id': selected_lga_id}
    return render(request, 'results/lga_results.html', context)

def new_polling_unit(request):
    if request.method == 'POST':
        pu_form = PollingUnitForm(request.POST)
        if pu_form.is_valid():
            polling_unit = pu_form.save()
            parties = ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP', 'ANPP', 'LABO', 'CPP']
            for party in parties:
                score = request.POST.get(f'score_{party}')
                if score:
                    AnnouncedPuResults.objects.create(
                        polling_unit_uniqueid=polling_unit,
                        party_abbreviation=party,
                        party_score=int(score)
                    )
            return redirect('polling_unit_results', uniqueid=polling_unit.uniqueid)
    else:
        pu_form = PollingUnitForm()
    context = {'pu_form': pu_form}
    return render(request, 'results/new_polling_unit.html', context)