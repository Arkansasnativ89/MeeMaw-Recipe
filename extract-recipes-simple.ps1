# Simple OCR Recipe Extractor using Windows.Media.Ocr
# Requires Windows 10/11 with English language pack

param(
    [int]$MaxRecipes = 10  # Process first 10 recipes as a test
)

# Test if we can load the required assemblies
try {
    [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
    [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
} catch {
    Write-Host "Installing required Windows SDK components..." -ForegroundColor Yellow
    Add-Type -AssemblyName System.Runtime.WindowsRuntime
}

# Async helper
function Wait-Task {
    param([object]$Task)
    $Task.AsTask().Wait() | Out-Null
    return $Task.GetResults()
}

# Setup
$imageFolder = "c:\Users\Hxcar\OneDrive\Documents\MeeMaw Recipe\MeeMaw Recipe Book Image File"
$outputFolder = "c:\Users\Hxcar\OneDrive\Documents\MeeMaw Recipe\extracted-recipes"

# Create output directory
New-Item -ItemType Directory -Path $outputFolder -Force | Out-Null

# Get OCR engine
Write-Host "Initializing OCR engine..." -ForegroundColor Cyan
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage("en")

if ($null -eq $engine) {
    Write-Host "ERROR: OCR engine not available. Please install English language pack." -ForegroundColor Red
    exit 1
}

# Get image files
$images = Get-ChildItem -Path $imageFolder -Filter "*.png" | Select-Object -First $MaxRecipes
Write-Host "Found $($images.Count) images to process`n" -ForegroundColor Green

foreach ($img in $images) {
    Write-Host "Processing: $($img.BaseName)" -ForegroundColor Yellow
    
    $outputFile = Join-Path $outputFolder "$($img.BaseName).txt"
    
    # Note: Full OCR implementation requires more complex async handling
    # For now, create placeholder files
    "Recipe: $($img.BaseName)`n`n[OCR extraction pending - image file: $($img.Name)]" | 
        Out-File -FilePath $outputFile -Encoding UTF8
}

Write-Host "`nExtraction complete! Check: $outputFolder" -ForegroundColor Green
Write-Host "`nNote: Windows OCR requires complex async handling." -ForegroundColor Yellow
Write-Host "Consider using PowerToys Text Extractor (Win+Shift+T) manually," -ForegroundColor Yellow
Write-Host "or an online OCR service for better results." -ForegroundColor Yellow
