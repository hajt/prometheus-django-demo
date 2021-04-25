import random
import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .metrics import (errors, generate_requests_metric, last_visit, latency,
                      latency2, pending_requests, status)


def home(request):
    generate_requests_metric(request, "/")
    last_visit.labels(endpoint="/").set(time.time())
    return HttpResponse("Prometheus Client in Django App Demo!")


@csrf_exempt
@errors.count_exceptions()
def counter(request):
    requests = generate_requests_metric(request, "/counter")
    last_visit.labels(endpoint="/counter").set(time.time())
    if random.random() < 0.3:
        raise Exception("Random exception")
    return HttpResponse(
        f"Counter examples. Watch metrics: <i>{requests.describe()[0].name}"
        f", {errors.describe()[0].name}</i>"
    )


@csrf_exempt
def gauge(request):
    generate_requests_metric(request, "/gauge")
    pending_requests.inc()
    time.sleep(3)
    pending_requests.dec()
    last_visit.labels(endpoint="/gauge").set(time.time())
    return HttpResponse(
        "Gauge examples. Watch metrics: <i>"
        f"{pending_requests.describe()[0].name}, "
        f"{last_visit.describe()[0].name}</i>"
    )


def summary(request):
    generate_requests_metric(request, "/summary")
    start = time.time()
    time.sleep(round(random.random(), 1))
    latency.observe(time.time() - start)
    last_visit.labels(endpoint="/summary").set(time.time())
    return HttpResponse(
        f"Summary example. Watch metric: <i>{latency.describe()[0].name}</i>"
    )


@latency2.time()
def histogram(request):
    generate_requests_metric(request, "/histogram")
    time.sleep(round(random.random(), 1))
    last_visit.labels(endpoint="/histogram").set(time.time())
    return HttpResponse(
        "Histogram example. Watch metric: <i>"
        f"{latency2.describe()[0].name}</i>"
    )


@errors.count_exceptions()
def enum(request):
    generate_requests_metric(request, "/enum")
    last_visit.labels(endpoint="/enum").set(time.time())
    if random.random() < 0.3:
        status.state("error")
        raise Exception("Random exception")
    status.state("success")
    return HttpResponse(
        f"Enum example. Watch metric: <i>{status.describe()[0].name}</i>"
    )
