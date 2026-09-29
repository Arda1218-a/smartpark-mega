Add-Type -AssemblyName System.Drawing
$inPath = "c:\Users\LENOVO\Documents\oto\patent_files\bulten_resim.png"
$outPath = "c:\Users\LENOVO\Documents\oto\patent_files\bulten_resim.jpg"

if (Test-Path $inPath) {
    $img = [System.Drawing.Image]::FromFile($inPath)
    $img.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $img.Dispose()
    Write-Host "True JPEG Generated Successfully!"
}
