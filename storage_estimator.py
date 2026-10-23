# storage_estimator.py
# Estimates how much storage a collection of files will need.

def estimate_storage(num_files, avg_size_mb):
    total_mb = num_files * avg_size_mb
    total_gb = total_mb / 1024
    return total_mb, total_gb


def main():
    print("Storage Estimator")
    num_files = int(input("How many files? "))
    avg_size_mb = float(input("Average file size in MB? "))

    total_mb, total_gb = estimate_storage(num_files, avg_size_mb)

    print(f"Total storage needed: {total_mb:.2f} MB")
    print(f"That is about {total_gb:.2f} GB")


main()
