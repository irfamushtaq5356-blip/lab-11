\# Storage Estimator-Main



\## Purpose

A Python program that estimates storage size from the values the user enters.



\## How to Run

1\. Install Python 3.

2\. Open a terminal in this folder.

3\. Run: python storage\_estimator.py



\## Example Input/Output

Input:

\# storage\_estimator.py

\# Estimates how much storage a collection of files will need.



def estimate\_storage(num\_files, avg\_size\_mb):

&#x20;   total\_mb = num\_files \* avg\_size\_mb

&#x20;   total\_gb = total\_mb / 1024

&#x20;   return total\_mb, total\_gb





def main():

&#x20;   print("Storage Estimator")

&#x20;   num\_files = int(input("How many files? "))

&#x20;   avg\_size\_mb = float(input("Average file size in MB? "))



&#x20;   total\_mb, total\_gb = estimate\_storage(num\_files, avg\_size\_mb)



&#x20;   print(f"Total storage needed: {total\_mb:.2f} MB")

&#x20;   print(f"That is about {total\_gb:.2f} GB")





main()





Output:

printed estimated storage



\## Author

Irfa mushtaq, 587853 , BSCSB

