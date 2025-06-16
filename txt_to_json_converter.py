import os
import json
import shutil

# File paths
old_users_file = "users.txt"
new_users_file = "users.json"
data_folder = "data"

# Step 1: Convert users.txt → users.json
def convert_users():
    if not os.path.exists(old_users_file):
        print("❌ users.txt ফাইল পাওয়া যায়নি।")
        return

    converted_users = {}

    with open(old_users_file, "r") as f:
        for line in f:
            name, pwd, per_day, target = line.strip().split(",")
            converted_users[name] = {
                "password": pwd,
                "per_day": per_day,
                "target": target
            }

    with open(new_users_file, "w") as f:
        json.dump(converted_users, f, indent=4)

    print("✅ users.txt → users.json কনভার্ট সম্পন্ন।")

# Step 2: Move data_<name>.txt → data/<name>.txt
def move_data_files():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    moved = False

    for filename in os.listdir("."):
        if filename.startswith("data_") and filename.endswith(".txt"):
            name = filename[5:-4]  # Remove "data_" and ".txt"
            new_path = os.path.join(data_folder, f"{name}.txt")
            shutil.move(filename, new_path)
            print(f"✅ {filename} → {new_path}")
            moved = True

    if not moved:
        print("ℹ️ কোনো পুরনো data_<name>.txt ফাইল পাওয়া যায়নি।")

# Run both steps
def main():
    convert_users()
    move_data_files()
    print("\n🎉 পুরনো সব ডেটা নতুন ভার্সনে রূপান্তর হয়েছে!")

if __name__ == "__main__":
    main()