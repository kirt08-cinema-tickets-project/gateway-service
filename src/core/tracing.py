from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import set_tracer_provider
from opentelemetry import trace

class Tracing:
    def __init__(self):
        self._tracer_provider: TracerProvider | None = None
        self._otlp_exporter: OTLPSpanExporter | None = None

        self._endpoint: str = "http://jaeger:4318/v1/traces"

    def startup(self):
        tracer_provider = TracerProvider(resource=Resource(attributes={
            SERVICE_NAME: "gateway-service"
        }))
        set_tracer_provider(tracer_provider)

        otlp_exporter = OTLPSpanExporter(
            endpoint=self._endpoint  
        )
        span_processor = BatchSpanProcessor(otlp_exporter)
        tracer_provider.add_span_processor(span_processor)

