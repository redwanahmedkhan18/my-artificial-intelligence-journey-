# 6️⃣ Configurable Logger (Professional-Level)

# Goal: Multiple defaults + overrides

# Task:
# Create a logger function:

# log("Model trained", level="INFO", timestamp=True)


# Output:

# [INFO] Model trained | 2026-01-21


# Rules:

# level default = "INFO"

# timestamp default = False

# 💡 This is exactly how real libraries work.

import datetime
def log(message, level="INFO", timestamp=False):
    prefix = f"[{level.upper()}]"
    if timestamp:
        now = datetime.datetime.now().strftime('%Y-%d-%m') 
        print(f"{prefix} {message} | {now}")
    else:
        print(f"{prefix} {message}")



# Default usage (INFO, no timestamp)
log("Application started")

# Override level
log("Database connection failed", level="ERROR")

# Override timestamp (default level)
log("User logged in", timestamp=True)

# Override both
log("Data processed successfully", level="DEBUG", timestamp=True)

