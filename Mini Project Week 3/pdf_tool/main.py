from pdf_operations import merge_pdfs, split_pdf
from logger import log_action
import os

def menu():
    print("\nPDF Tool Menu")
    print("1. Merge PDF files")
    print("2. Split a PDF into pages")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pdfs = input("Enter paths to PDF files (comma-separated): ").split(',')
            output = input("Output filename (e.g., merged.pdf): ").strip()
            merge_pdfs(pdfs, output)
            log_action(f"Merged files into {output}")
            print("✅ Merge complete!")

        elif choice == "2":
            path = input("PDF to split: ").strip()
            output_dir = input("Output directory: ").strip()
            os.makedirs(output_dir, exist_ok=True)
            split_pdf(path, output_dir)
            log_action(f"Split {path} into pages in {output_dir}")
            print("✅ Split complete!")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
