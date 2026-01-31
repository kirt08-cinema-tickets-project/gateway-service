from datetime import datetime, timezone
from typing import Dict


async def service_ping() -> Dict:
    return {
        "status": "pong", 
        "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S-%d/%m/%Y")
    }
