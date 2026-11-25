def check_overdue(days_pending):

    if days_pending >= 7:
        return "Escalation Required"

    elif days_pending >= 3:
        return "Second Reminder"

    else:
        return "Normal Reminder"


# Sample test
days = 8

status = check_overdue(days)

print("Claim Status:", status)
