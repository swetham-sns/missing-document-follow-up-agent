from document_checker import check_documents
from email_sender import create_reminder_email
from escalation import check_overdue

def run_agent():

    print("Missing Document Follow-up Agent Started!")

    required = [
        "ID Proof",
        "Address Proof",
        "Bank Statement"
    ]

    submitted = [
        "ID Proof",
        "Bank Statement"
    ]

    missing = check_documents(required, submitted)

    print("\nMissing Documents:", missing)

    if missing:
        subject, message = create_reminder_email(
            "Customer A",
            "CL001",
            missing
        )

        print("\nReminder Email:")
        print(subject)
        print(message)

    status = check_overdue(8)

    print("\nEscalation Status:", status)
    print("\nWorkflow Completed!")

if __name__ == "__main__":
    run_agent()
