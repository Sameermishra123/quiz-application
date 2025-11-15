# PowerShell script to fix ChromeDriver version conflict
# Run this script as Administrator

Write-Host "=" -NoNewline
Write-Host ("=" * 69)
Write-Host "ChromeDriver PATH Conflict Fixer (PowerShell)"
Write-Host "=" -NoNewline
Write-Host ("=" * 69)
Write-Host ""

$chromedriverPath = "C:\Windows\chromedriver.exe"

if (Test-Path $chromedriverPath) {
    Write-Host "Found old ChromeDriver at: $chromedriverPath" -ForegroundColor Yellow
    Write-Host ""
    
    $backupPath = "$chromedriverPath.old"
    
    if (Test-Path $backupPath) {
        Write-Host "Backup already exists: $backupPath" -ForegroundColor Yellow
        $response = Read-Host "Delete the old backup and create a new one? (y/n)"
        if ($response -eq 'y') {
            Remove-Item $backupPath -Force
        } else {
            Write-Host "Skipping backup creation." -ForegroundColor Yellow
            exit
        }
    }
    
    Write-Host "Renaming ChromeDriver to prevent PATH conflicts..." -ForegroundColor Cyan
    try {
        Rename-Item -Path $chromedriverPath -NewName "chromedriver.exe.old" -Force
        Write-Host "✓ Successfully renamed ChromeDriver!" -ForegroundColor Green
        Write-Host "  Old: $chromedriverPath" -ForegroundColor Gray
        Write-Host "  New: $backupPath" -ForegroundColor Gray
        Write-Host ""
        Write-Host "You can now run: python test_quiz.py" -ForegroundColor Green
    } catch {
        Write-Host "✗ Error: $_" -ForegroundColor Red
        Write-Host ""
        Write-Host "Try running PowerShell as Administrator:" -ForegroundColor Yellow
        Write-Host "  Right-click PowerShell -> Run as Administrator" -ForegroundColor Yellow
    }
} else {
    Write-Host "✓ No ChromeDriver found in C:\Windows\" -ForegroundColor Green
    Write-Host "  webdriver-manager will download the correct version automatically." -ForegroundColor Green
}

Write-Host ""
Write-Host "=" -NoNewline
Write-Host ("=" * 69)

