$files = @((Get-ChildItem -Path <PATH> -Recurse -Filter *.<EXTENSION>).FullName)
foreach($data in $files) {
	echo "----------------------- $data -----------------------"
	Get-Content $data
	echo "`r`n`r`n`r"
}