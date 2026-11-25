def check_documents(required, submitted):

    missing = []

    for document in required:
        if document not in submitted:
            missing.append(document)

    return missing


# Sample testing data
required_documents = [
    "ID Proof",
    "Address Proof",
    "Bank Statement"
]

submitted_documents = [
    "ID Proof",
    "Bank Statement"
]

missing_documents = check_documents(
    required_documents,
    submitted_documents
)

print("Missing Documents:", missing_documents)
if missing_documents:
    print("Claim Status: Incomplete")
    print("Please submit the missing documents.")
else:
    print("Claim Status: Complete")
