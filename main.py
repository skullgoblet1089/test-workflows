import os
from datetime import datetime, timezone

local_time = datetime.now()
utc_time = datetime.utcnow()
local_tz = local_time.astimezone().tzinfo.tzname(local_time)

print("Hello, world!")
if "GITHUB_WORKFLOW" in os.environ:
    print(
        f"GitHub workflow {os.environ['GITHUB_WORKFLOW']} \
        triggered by {os.environ['GITHUB_EVENT_NAME']}"
    )
print(f"local time is: {local_time} {local_tz}")
print(f"  utc time is: {utc_time} GMT")
