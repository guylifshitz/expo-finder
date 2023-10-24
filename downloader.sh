#!/bin/bash
set -B   # enable brace expansion

mkdir -p downloads
echo "This script downloads 25 pages, this should be sufficient to get all exhibitions."
for ((i=1;i<=25;i++)); 
do 
   echo $i
    echo "curl https://www.offi.fr/expositions-musees/programme.html?npage=$i&valuesSortGroup=lieu&tri=asc -o downloads/$i.html"
    curl "https://www.offi.fr/expositions-musees/programme.html?npage=$i&valuesSortGroup=lieu&tri=asc" -o "downloads/$i.html"
done
