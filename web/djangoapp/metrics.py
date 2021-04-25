from prometheus_client import Counter, Enum, Gauge, Histogram, Info, Summary

info = Info("app", "Information about the application")
info.info({"version": "1.1", "language": "python", "framework": "django"})

requests = Counter(
    "app_requests_total",
    "Number of various requests.",
    ["method", "endpoint"]
)
errors = Counter(
    "app_errors_total",
    "Number of errors on a page."
)
pending_requests = Gauge(
    "app_pending_requests",
    "Number of pending requests on a page."
)
last_visit = Gauge(
    "app_last_visit_time_seconds",
    "The last time when a page was served.",
    ["endpoint"]
)
latency = Summary(
    "app_page_latency_seconds",
    "Time for a request on a page (using summary)."
)
latency2 = Histogram(
    "app_page_latency2_seconds",
    "Time for a request on a page (using histogram)."
)
status = Enum(
    "app_page_last_load_status",
    "Status of last load a page",
    states=["unknown", "success", "error"],
)


def generate_requests_metric(request, endpoint):
    if request.method == "GET":
        requests.labels(method="get", endpoint=endpoint).inc()
    elif request.method == "POST":
        requests.labels(method="post", endpoint=endpoint).inc()
    return requests
