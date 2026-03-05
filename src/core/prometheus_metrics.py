from prometheus_client import Counter, Histogram, Gauge


REQUEST_COUNT = Counter("http_request_total", "Total number of HTTP requests",
                        ["service", "method", "endpoint", "status"])

REQUEST_DURATION = Histogram("http_request_duration_seconds",
                             "HTTP request latency",
                             ["service", "method", "endpoint", "status"],
                             buckets=[0.05, 0.1, 0.2, 0.3, 0.5, 1, 1.5, 2, 3, 5])

REQUEST_IN_FLIGHT = Gauge("http_requests_in_flight",
                          "Current number of in-flight HTTP requests",
                          ["service"])
