password = input ("Enter your password: ")
score = 0
feedback= []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters long")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add atleast one upper letter")

if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add atleast one lowercase letter")

if any (char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add atleast one number")

if any(not char.isalnum() for char in password):
    score += 1
else:
    feedback.append("Add atleast one special character")

print("\nPassword Strength:")

if score <= 2:
    print("❌ WEAK")
elif score <= 4:
    print("⚠️ MEDIUM")
else:
    print("✅ STRONG")

if feedback:
    print("\n Suggestions:")
    for item in feedback:
        print("-", item)