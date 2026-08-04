# =====================================================================
# INTEGRATION TASK: Testing Day 1 Variables against Day 2 Logic
# =====================================================================

# 1. Define your salary target (converting string data to integers)
my_target_salary_usd = 4500

# 2. Add an automated logic check to evaluate an offer
if my_target_salary_usd >= 4500:
    print("🚀 STRATEGY SUCCESS: This offer matches global international standards.")
else:
    print("❌ POSTURE ALERT: This offer is a local market trap. Keep negotiating.")


# =====================================================================
# CHALLLENGE: Advanced Multi-Tiered Salary Evaluator
# =====================================================================

# Change this number to 1600, then 1000, then run it again to test!
my_target_salary_usd = 4500

if my_target_salary_usd >= 4500:
    print("🚀 STRATEGY SUCCESS: This offer matches global international standards.")

elif my_target_salary_usd >= 1600 and my_target_salary_usd < 4500:
    print("⚠️ MIDDLE CLASS SQUEEZE: This is an average local IT salary (~R30,000). Decent survival, but no leverage.")

else:
    print("❌ CRITICAL POSTURE FAILURE: This is a low-paid survival trap (~R12,000 to R18,000). Reject and walk away.")
