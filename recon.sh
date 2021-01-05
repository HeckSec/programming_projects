#!/bin/bash

url=$1

if [ ! -d "$url" ];then
	mkdir $url
fi

if [ ! -d "$url/recon" ];then
	mkdir $url/recon
fi

echo "[+] Harvesting Subdomains with Assetfinder..."
assetfinder --subs-only $url >> $url/recon/assets.txt
cat $url/recon/assets.txt | grep $1 >> $url/recon/final.txt
rm $url/recon/assets.txt 

# echo "[+] Harvesting Subdomains with Owasp Amass..."
# amass enum -d $url >> $url/recon/f.txt 
# sort -u $url/recon/assets.txt >> $url/recon/final.txt
# rm $url/recon/f.txt

echo "[+] Probing for Alive Domains..."
cat $url/recon/final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' >> $url/recon/alive.txt
