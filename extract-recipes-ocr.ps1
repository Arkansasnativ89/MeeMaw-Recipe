# OCR Recipe Extractor for MeeMaw's Cookbook
# This script extracts text from recipe image files using Windows OCR

# Load Windows OCR assembly
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine,Windows.Foundation,ContentType=WindowsRuntime]

# Helper function to convert async operations to sync
Function Await($WinRtTask, $ResultType) {
    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
    })[0]
    $asTask = $asTask.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}

# Get the OCR engine for English
$ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage("en")
if ($null -eq $ocrEngine) {
    Write-Host "ERROR: Could not initialize OCR engine. Make sure English language pack is installed." -ForegroundColor Red
    exit 1
}

# Set paths
$imageFolder = "c:\Users\Hxcar\OneDrive\Documents\MeeMaw Recipe\MeeMaw Recipe Book Image File"
$outputFolder = "c:\Users\Hxcar\OneDrive\Documents\MeeMaw Recipe\extracted-recipes"

# Create output folder if it doesn't exist
if (-not (Test-Path $outputFolder)) {
    New-Item -ItemType Directory -Path $outputFolder | Out-Null
}

# Get all PNG files
$imageFiles = Get-ChildItem -Path $imageFolder -Filter "*.png"
Write-Host "Found $($imageFiles.Count) recipe images to process`n" -ForegroundColor Cyan

$processedCount = 0
$failedCount = 0

foreach ($imageFile in $imageFiles) {
    try {
        Write-Host "Processing: $($imageFile.Name)..." -NoNewline
        
        # Load the image file
        $fileTask = [Windows.Storage.StorageFile]::GetFileFromPathAsync($imageFile.FullName)
        $file = Await $fileTask ([Windows.Storage.StorageFile])
        
        # Open the image stream
        $streamTask = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $stream = Await $streamTask ([Windows.Storage.Streams.IRandomAccessStream])
        
        # Create bitmap decoder
        $decoderTask = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
        $decoder = Await $decoderTask ([Windows.Graphics.Imaging.BitmapDecoder])
        
        # Get the software bitmap
        $bitmapTask = $decoder.GetSoftwareBitmapAsync()
        $bitmap = Await $bitmapTask ([Windows.Graphics.Imaging.SoftwareBitmap])
        
        # Perform OCR
        $ocrResultTask = $ocrEngine.RecognizeAsync($bitmap)
        $ocrResult = Await $ocrResultTask ([Windows.Media.Ocr.OcrResult])
        
        # Extract text
        $extractedText = $ocrResult.Text
        
        # Save to text file
        $outputFileName = [System.IO.Path]::GetFileNameWithoutExtension($imageFile.Name) + ".txt"
        $outputPath = Join-Path $outputFolder $outputFileName
        $extractedText | Out-File -FilePath $outputPath -Encoding UTF8
        
        # Clean up
        $stream.Dispose()
        $bitmap.Dispose()
        
        Write-Host " ✓ Done" -ForegroundColor Green
        $processedCount++
        
    } catch {
        Write-Host " ✗ Failed" -ForegroundColor Red
        Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Yellow
        $failedCount++
    }
    
    # Small delay to prevent overwhelming the system
    Start-Sleep -Milliseconds 100
}

Write-Host "`n" + "=" * 60 -ForegroundColor Cyan
Write-Host "OCR Extraction Complete!" -ForegroundColor Green
Write-Host "Successfully processed: $processedCount files" -ForegroundColor Green
Write-Host "Failed: $failedCount files" -ForegroundColor $(if ($failedCount -eq 0) { "Green" } else { "Yellow" })
Write-Host "Output location: $outputFolder" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
