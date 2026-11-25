import csv

def read_claims(filename="claims.csv"):

    claims = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                claims.append(row)

    except FileNotFoundError:
        print("Claims file not found!")

    return claims


if __name__ == "__main__":
    data = read_claims()
    print(data)
