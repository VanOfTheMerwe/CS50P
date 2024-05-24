import sys
import csv

def main():
    students = []

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        try:
            with open(sys.argv[1], "r") as readfile, open(sys.argv[2], "w") as writefile:
                reader = csv.DictReader(readfile)
                for row in reader:
                    splited = row["name"].split(",")
                    students.append({
                        "first": splited[1].lstrip(),
                        "last": splited[0],
                        "house": row["house"
                        ]})
                writer = csv.DictWriter(writefile, fieldnames=["first", "last", "house"])
                writer.writerow({
                    "first": "first",
                    "last": "last",
                    "house": "house"
                })
                for row in students:
                    writer.writerow({
                        "first": row["first"],
                        "last": row["last"],
                        "house": row["house"]
                    })

        except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")

if __name__ == "__main__":
    main()
