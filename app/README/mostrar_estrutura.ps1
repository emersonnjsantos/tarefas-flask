[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$root = Get-Location

# Pega somente as pastas e arquivos do diretório atual
$folders = Get-ChildItem -Directory
$files = Get-ChildItem -File

# Mostra as pastas com os arquivos de dentro
foreach ($folder in $folders) {
    Write-Host "- $($folder.Name)/"
    $innerFiles = Get-ChildItem -Path $folder.FullName -File
    foreach ($file in $innerFiles) {
        Write-Host "   - $($file.Name)"
    }
}

# Mostra os arquivos que estão diretamente na raiz
foreach ($file in $files) {
    Write-Host "- $($file.Name)"
}
