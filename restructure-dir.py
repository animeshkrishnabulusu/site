import os
import shutil
import argparse

def restructure_html_folders(base_folder, dry_run=True):
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        index_html_path = os.path.join(folder_path, "index.html")
        new_html_path = os.path.join(base_folder, f"{folder_name}.html")
        
        if os.path.isdir(folder_path) and os.path.exists(index_html_path):
            if dry_run:
                print(f"[Dry Run] Would rename {index_html_path} -> {new_html_path}")
            else:
                shutil.move(index_html_path, new_html_path)
                # Only remove the folder if it is empty after moving index.html
                if not os.listdir(folder_path):
                    os.rmdir(folder_path)
                    print(f"Moved {index_html_path} -> {new_html_path} and removed {folder_path}")
                else:
                    print(f"Moved {index_html_path} -> {new_html_path}, but {folder_path} is not empty and was not removed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Restructure HTML folders by moving index.html up a level.")
    parser.add_argument("base_folder", help="Path to the top-level folder.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making changes.")
    args = parser.parse_args()
    
    restructure_html_folders(args.base_folder, dry_run=args.dry_run)