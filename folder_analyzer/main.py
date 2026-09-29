import os

def format_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"
    else:
        return f"{size / (1024 ** 3):.2f} GB"


def analyze_folder(folder_path):
    total_size = 0
    file_count = 0
    folder_count = 0
    files = []
    extensions = {}

    for root, dirs, filenames in os.walk(folder_path):
        folder_count += len(dirs)

        for filename in filenames:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
            except OSError:
                continue

            total_size += size
            file_count += 1

            files.append((size, file_path))

            extension = os.path.splitext(filename)[1].lower()

            if extension == "":
                extension = "No Extension"

            extensions[extension] = extensions.get(extension, 0) + size

    files.sort(reverse=True)

    print("\n========== FOLDER ANALYZER ==========")

    print(f"Total Size   : {format_size(total_size)}")
    print(f"Files        : {file_count}")
    print(f"Folders      : {folder_count}")

    print("\n--- Largest 5 Files ---")

    for size, path in files[:5]:
        print(f"{format_size(size):>10}  {path}")

    print("\n--- File Type Usage ---")

    for extension, size in sorted(
        extensions.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{extension:15} {format_size(size)}")


folder = input("Enter folder path: ")

if os.path.isdir(folder):
    analyze_folder(folder)
else:
    print("Invalid folder path!")