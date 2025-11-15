"""
Helper script to start PHP built-in server for testing
Run this before running test_quiz.py
"""

import os
import subprocess
import sys
import time

def check_php_installed():
    """Check if PHP is installed"""
    try:
        result = subprocess.run(['php', '-v'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✓ PHP is installed")
            print(f"  Version: {result.stdout.split()[1]}")
            return True
    except FileNotFoundError:
        print("✗ PHP is not installed or not in PATH")
        return False
    except Exception as e:
        print(f"✗ Error checking PHP: {e}")
        return False

def start_server(port=8000):
    """Start PHP built-in server"""
    project_dir = os.getcwd()
    host = 'localhost'
    
    print(f"\nStarting PHP server on {host}:{port}")
    print(f"Project directory: {project_dir}")
    print(f"\nServer will be available at: http://{host}:{port}/")
    print("\nPress Ctrl+C to stop the server\n")
    print("="*70)
    
    try:
        # Start PHP server
        cmd = ['php', '-S', f'{host}:{port}']
        process = subprocess.Popen(cmd, cwd=project_dir)
        
        # Wait a moment to check if it started successfully
        time.sleep(1)
        if process.poll() is None:
            print(f"✓ Server started successfully!")
            print(f"  URL: http://{host}:{port}/")
            print(f"\nKeep this window open while running tests.")
            print(f"Press Ctrl+C to stop the server.\n")
            
            # Wait for user interrupt
            try:
                process.wait()
            except KeyboardInterrupt:
                print("\n\nStopping server...")
                process.terminate()
                process.wait()
                print("✓ Server stopped")
        else:
            print("✗ Server failed to start")
            return False
            
    except KeyboardInterrupt:
        print("\n\nStopping server...")
        if 'process' in locals():
            process.terminate()
        print("✓ Server stopped")
    except Exception as e:
        print(f"\n✗ Error starting server: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("="*70)
    print("PHP Server Starter for Quiz Application")
    print("="*70)
    
    if not check_php_installed():
        print("\nPlease install PHP:")
        print("  1. Download from: https://www.php.net/downloads.php")
        print("  2. Add PHP to your system PATH")
        print("  3. Or use XAMPP/WAMP/MAMP which includes PHP")
        sys.exit(1)
    
    # Get port from command line or use default
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}, using default: 8000")
    
    start_server(port)

