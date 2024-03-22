#!/bin/bash

# Created by HeckSec

url=$1

if [ ! -d "$url" ];then
        mkdir $url
fi

if [ ! -d "$url/recon" ];then
        mkdir $url/recon
fi

echo "[+] Gathering Subdomains with Sublist3r..."
sublist3r -d $url -o $url/recon/subdomains.txt
sort -u $url/recon/subdomains.txt >> $url/recon/initial.txt # this removes duplicates and saves to a new file 
rm $url/recon/subdomains.txt # removes old file with possible duplicates


sed -i -e 's_^_https://_' $url/recon/initial.txt # this adds https: to the beginning of each line as the following tools appreciate the formality. 

echo "[+] Probing for alive domains with probethis..."
cat $url/recon/initial.txt | probethis.py -s 200,401 -o $url/recon/alive_subs.txt

echo "[+] Probing for Directories with feroxbuster.."
cat $url/recon/alive_subs.txt | feroxbuster --stdin --silent -s 200 401 --depth 5 -x php,html,js,json,docx,xlxs,csv,txt,aspx  -q --wordlist /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt -o $url/recon/dirs.txt
# CHANGE WORDLIST, FILEPATH, & DEPTH IF NECESSARY

sort -u $url/recon/dirs.txt >> $url/recon/fin_dirs.txt
rm $url/recon/dirs.txt 
