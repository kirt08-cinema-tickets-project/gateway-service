import base64
import json

async def service_get_telegram_query(fragment : str) -> dict[str, str]:
    decoded_fragment_bytes = base64.urlsafe_b64decode(fragment + "===")
    decoded_fragment = json.loads(decoded_fragment_bytes.decode("utf-8"))
    return {str(v): str(k) for v, k in decoded_fragment.items()}