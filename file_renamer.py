#File Date Renaming Script

import os
import time
from datetime import datetime
from pathlib import Path

def get_files(folder_path, file_extensions=None):
    """Get all files from the specified folder, optionally filtered by extensions."""
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")
    
    if file_extensions is None:
        # Get all files (excluding directories)
        all_files = [f for f in folder.iterdir() if f.is_file()]
    else:
        # Get files with specific extensions
        all_files = set()  # Use set to avoid duplicates
        for ext in file_extensions:
            all_files.update(folder.glob(f"*.{ext}"))
            all_files.update(folder.glob(f"*.{ext.upper()}"))
    
    return list(all_files)

def get_modification_date(file_path):
    """Get the modification date of a file in YYYYMMDD format."""
    mod_time = os.path.getmtime(file_path)
    mod_date = datetime.fromtimestamp(mod_time)
    return mod_date.strftime("%Y%m%d")

def generate_new_filename(file_path):
    """Generate new filename with modification date prefix."""
    mod_date = get_modification_date(file_path)
    original_name = file_path.name
    
    # Check if filename already starts with a date pattern
    if len(original_name) >= 8 and original_name[:8].isdigit() and original_name[8] == '-':
        print(f"  Skipping '{original_name}' - already has date prefix")
        return None
    
    new_name = f"{mod_date}-{original_name}"
    return file_path.parent / new_name

def preview_changes(file_list, new_names):
    """Display preview of changes to be made."""
    print("\n" + "="*60)
    print("PREVIEW OF CHANGES:")
    print("="*60)
    
    changes_count = 0
    for i, (old_path, new_path) in enumerate(zip(file_list, new_names)):
        if new_path is not None:
            print(f"{changes_count + 1:2d}. {old_path.name}")
            print(f"    -> {new_path.name}")
            changes_count += 1
    
    if changes_count == 0:
        print("No files need to be renamed.")
        return False
    
    print(f"\nTotal files to rename: {changes_count}")
    return True

def rename_files(file_list, new_names):
    """Rename files and return list of successful renames for potential rollback."""
    renamed_files = []
    
    try:
        for old_path, new_path in zip(file_list, new_names):
            if new_path is not None:
                old_path.rename(new_path)
                renamed_files.append((new_path, old_path))  # Store (new, original) for rollback
                print(f"✓ Renamed: {old_path.name} -> {new_path.name}")
        
        return renamed_files
        
    except Exception as e:
        print(f"\nError during renaming: {e}")
        # Rollback any successful renames
        if renamed_files:
            print("Rolling back changes...")
            for new_path, original_path in renamed_files:
                try:
                    new_path.rename(original_path)
                    print(f"✓ Rolled back: {new_path.name} -> {original_path.name}")
                except Exception as rollback_error:
                    print(f"✗ Failed to rollback {new_path.name}: {rollback_error}")
        raise

def rollback_changes(renamed_files):
    """Rollback all the renamed files."""
    print("\nRolling back changes...")
    for new_path, original_path in renamed_files:
        try:
            new_path.rename(original_path)
            print(f"✓ Rolled back: {new_path.name} -> {original_path.name}")
        except Exception as e:
            print(f"✗ Failed to rollback {new_path.name}: {e}")

def main():
    print("File Renamer - Add Modification Date Prefix")
    print("=" * 50)
    
    # Get folder path from user
    while True:
        folder_path = input("\nEnter the folder path containing files: ").strip()
        if folder_path:
            break
        print("Please enter a valid folder path.")
    
    # Ask user for file type preference
    print("\nFile type options:")
    print("1. All files")
    print("2. Specific file types (e.g., jpg, mp4, png)")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice == '1':
            file_extensions = None
            break
        elif choice == '2':
            extensions_input = input("Enter file extensions separated by commas (e.g., jpg,mp4,png): ").strip()
            file_extensions = [ext.strip().lower() for ext in extensions_input.split(',') if ext.strip()]
            if file_extensions:
                break
            else:
                print("Please enter at least one valid file extension.")
        else:
            print("Please enter '1' or '2'.")
    
    try:
        # Get all files
        files = get_files(folder_path, file_extensions)
        
        if not files:
            if file_extensions:
                print(f"No files with extensions {file_extensions} found in '{folder_path}'")
            else:
                print(f"No files found in '{folder_path}'")
            return
        
        if file_extensions:
            print(f"\nFound {len(files)} file(s) with extensions: {', '.join(file_extensions)}")
        else:
            print(f"\nFound {len(files)} file(s)")
        
        # Generate new filenames
        new_filenames = []
        for file_path in files:
            new_name = generate_new_filename(file_path)
            new_filenames.append(new_name)
        
        # Preview changes
        has_changes = preview_changes(files, new_filenames)
        
        if not has_changes:
            return
        
        # Ask for confirmation
        while True:
            confirm = input("\nProceed with renaming? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                break
            elif confirm in ['n', 'no']:
                print("Operation cancelled.")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        # Perform renaming
        print("\nRenaming files...")
        renamed_files = rename_files(files, new_filenames)
        
        print(f"\n✓ Successfully renamed {len(renamed_files)} file(s)!")
        
        # Ask if user wants to keep the changes
        while True:
            keep_changes = input("\nAre you satisfied with the results? Keep changes? (y/n): ").strip().lower()
            if keep_changes in ['y', 'yes']:
                print("Changes kept. Operation completed successfully!")
                break
            elif keep_changes in ['n', 'no']:
                rollback_changes(renamed_files)
                print("All changes have been rolled back.")
                break
            else:
                print("Please enter 'y' to keep changes or 'n' to rollback.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
