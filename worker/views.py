from django.http import HttpRequest
from django.shortcuts import render

from worker.models import Worker


def list_all_workers(request):
    workers = Worker.objects.all()
    w = []
    for worker in workers:
        w.append(worker.get_dict())
    return render(request, 'main.html', context={'workers': w})


def detail(request: HttpRequest, pk):
    worker = Worker.objects.get(id=pk)
    worker_dict = worker.get_dict()
    worker_dict['taxes'] = [{'rate': tax.rate * 100, 'name': tax.name} for tax in worker.taxes.all()]
    worker_dict['premiums'] = [{'rate': premium.rate * 100, 'name': premium.name} for premium in worker.premiums.all()]
    worker_dict['leveled_salary'] = (worker.position.min_salary * (
        worker.level.rate)) + worker.position.min_salary if worker.level else worker.position.min_salary
    return render(request, 'detail.html', context=worker_dict)
