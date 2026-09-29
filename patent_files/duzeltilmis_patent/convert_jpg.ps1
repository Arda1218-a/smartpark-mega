
Add-Type -AssemblyName System.Drawing
$inPath = "c:\Users\LENOVO\Documents\oto\patent_files\duzeltilmis_patent\bulten_resim.png"
$outPath = "c:\Users\LENOVO\Documents\oto\patent_files\duzeltilmis_patent\bulten_resim.jpg"
$img = [System.Drawing.Image]::FromFile($inPath)
$img.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
$img.Dispose()
