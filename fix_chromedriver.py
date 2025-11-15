"""
Helper script to fix ChromeDriver version mismatch issues
This script helps identify and resolve ChromeDriver PATH conflicts
"""

import os
import shutil
from pathlib import Path

def find_chromedriver_in_path():
    """Find chromedriver.exe in system PATH"""
    chromedriver_paths = []
    path_env = os.environ.get('PATH', '')
    
    for path_dir in path_env.split(os.pathsep):
        if path_dir:
            chromedriver_path = os.path.join(path_dir, 'chromedriver.exe')
            if os.path.exists(chromedriver_path):
                chromedriver_paths.append(chromedriver_path)
    
    return chromedriver_paths

def check_chrome_version():
    """Try to detect Chrome version"""
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    
    for chrome_path in chrome_paths:
        if os.path.exists(chrome_path):
            try:
                import subprocess
                result = subprocess.run(
                    [chrome_path, '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return result.stdout.strip()
            except:
                pass
    
    return "Unable to detect Chrome version"

def main():
    print("="*70)
    print("ChromeDriver PATH Conflict Fixer")
    print("="*70)
    print()
    
    # Check Chrome version
    chrome_version = check_chrome_version()
    print(f"Detected Chrome: {chrome_version}")
    print()
    
    # Find chromedriver in PATH
    chromedriver_paths = find_chromedriver_in_path()
    
    if not chromedriver_paths:
        print("✓ No chromedriver.exe found in PATH - you're good to go!")
        print("  webdriver-manager will download the correct version automatically.")
        return
    
    print(f"⚠ Found {len(chromedriver_paths)} chromedriver.exe in PATH:")
    print()
    for i, path in enumerate(chromedriver_paths, 1):
        print(f"  {i}. {path}")
        try:
            size = os.path.getsize(path)
            print(f"     Size: {size:,} bytes")
        except:
            pass
        print()
    
    print("="*70)
    print("RECOMMENDED ACTIONS:")
    print("="*70)
    print()
    print("Option 1: Rename the old chromedriver (Recommended)")
    print("  This preserves the file but removes it from PATH detection:")
    print()
    for path in chromedriver_paths:
        backup_path = path + ".old"
        print(f"  Rename: {path}")
        print(f"       To: {backup_path}")
        print()
        try:
            if os.path.exists(backup_path):
                print(f"  ⚠ Backup already exists: {backup_path}")
            else:
                response = input(f"  Rename {os.path.basename(path)}? (y/n): ")
                if response.lower() == 'y':
                    try:
                        os.rename(path, backup_path)
                        print(f"  ✓ Successfully renamed to {backup_path}")
                    except PermissionError:
                        print(f"  ✗ Permission denied. Run as Administrator or close any programs using chromedriver.")
                    except Exception as e:
                        print(f"  ✗ Error: {e}")
        except KeyboardInterrupt:
            print("\n  Cancelled.")
            break
    
    print()
    print("Option 2: Delete the old chromedriver")
    print("  (Only if you're sure you don't need it)")
    print()
    print("Option 3: Remove the directory from PATH")
    print("  (Advanced - modify system environment variables)")
    print()
    print("="*70)
    print("After fixing, run: python test_quiz.py")
    print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")

