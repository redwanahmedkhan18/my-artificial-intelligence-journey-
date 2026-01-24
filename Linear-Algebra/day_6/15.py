# 1️⃣4️⃣ Configurable Logger

# Goal: Default + optional behavior

# Task:
# Write a function that logs messages:

# log("Server started")
# log("Invalid login", level="ERROR")


# Output:

# [INFO] Server started
# [ERROR] Invalid login


# 💡 Skill: Professional function interfaces

def log(message, level='INFO'):
  level = level.upper()
  if level == 'ERROR':
    print(f"[ERROR] {message}")
  elif level == 'INFO':
    print(f"[INFO] {message}")
  else:
    print(f"[UNKNOWN] {message}")


log("Server started") 
log("Invalid login", level="ERROR") 
log("User logged out", level="INFO") 
