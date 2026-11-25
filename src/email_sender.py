def create_reminder_email(customer, claim_id, missing_docs):

    subject = "Missing Documents - Claim Follow-up"

    message = f"""
Dear {customer},

Your insurance claim ({claim_id})
is pending due to missing documents.

Please submit the following documents:

{', '.join(missing_docs)}

Thank you,
Insurance Support Team
"""

    return subject, message


if __name__ == "__main__":
    subject, message = create_reminder_email(
        "Customer A",
        "CL001",
        ["ID Proof", "Address Proof"]
    )

    print(subject)
    print(message)
