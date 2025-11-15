"""
Helper script to fix ChromeDriver WinError 193 issues
Run this if you get "WinError 193: %1 is not a valid Win32 application"
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

def clear_webdriver_cache():
    """Clear webdriver-manager cache"""
    cache_path = os.path.join(os.path.expanduser("~"), ".wdm")
    if os.path.exists(cache_path):
        try:
            shutil.rmtree(cache_path)
            print(f"✓ Cleared webdriver-manager cache: {cache_path}")
            return True
        except Exception as e:
            print(f"✗ Could not clear cache: {e}")
            return False
    else:
        print("✓ No cache found (this is fine)")
        return True

def main():
    print("="*70)
    print("ChromeDriver WinError 193 Fixer")
    print("="*70)
    print()
    
    # Check for chromedriver in PATH
    chromedriver_paths = find_chromedriver_in_path()
    
    if chromedriver_paths:
        print(f"⚠ Found {len(chromedriver_paths)} chromedriver.exe in PATH:")
        for path in chromedriver_paths:
            print(f"  - {path}")
        print()
        print("These may cause conflicts. Consider renaming them:")
        for path in chromedriver_paths:
            backup_path = path + ".old"
            print(f"  Rename: {path}")
            print(f"       To: {backup_path}")
        print()
    else:
        print("✓ No chromedriver.exe found in PATH (good!)")
        print()
    
    # Clear webdriver-manager cache
    print("Clearing webdriver-manager cache...")
    clear_webdriver_cache()
    print()
    
    print("="*70)
    print("Next Steps:")
    print("="*70)
    print("1. If you found chromedriver.exe in PATH, rename them (see above)")
    print("2. Run your tests again - webdriver-manager will download fresh ChromeDriver")
    print("3. Make sure your web server is running:")
    print("   cd quiz-application")
    print("   php -S localhost:8000 -t public")
    print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")

