def count_gmail_emails(file_path):
    gmail_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip().endswith('@gmail.com'):
                gmail_count += 1
    return gmail_count

def main():
    file_path = 'list_gmail.txt'
    gmail_count = count_gmail_emails(file_path)
    print("The number of Gmail emails in the list is:", gmail_count)

if __name__ == "__main__":
    main()
