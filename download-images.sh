#!/bin/bash
# Run this script from the project root to download all images from the live site.
# Usage: bash download-images.sh

BASE="assets/images"

mkdir -p "$BASE/bio" "$BASE/publications" "$BASE/home"

echo "Downloading bio images..."
curl -sL -o "$BASE/bio/headshot.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613625616591-U7YCTG6G7SV5RRRD91ES/F4CDEC52-1243-44ED-8D80-5F9B97A68D2B+copy.JPG"
curl -sL -o "$BASE/bio/teamwork.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1615839391199-IHY6V127YZVD4ANCMIUV/IMG_2788.jpg"

echo "Downloading publications images..."
curl -sL -o "$BASE/publications/aiga-2022.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/88afcc09-3aef-4cd1-af60-83c565337f12/Screen+Shot+2022-10-12+at+7.57.18+PM.jpg"
curl -sL -o "$BASE/publications/design-thesis.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/0b4c3abe-2f81-45ad-8ffd-d8a5d5e7d5fb/Frame+68+%281%29.jpg"
curl -sL -o "$BASE/publications/rsd10-racial-justice.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/6b278eec-65b1-43c3-9446-96eed2689ef4/Group+1+%284%29.png"
curl -sL -o "$BASE/publications/imaginaries-lab-climate.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/52ac0e03-dfc2-4b2e-a2f5-36c5273b90f7/Frame+69.jpg"
curl -sL -o "$BASE/publications/iasdr-2021-workshop.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/d131d5b8-281d-4f5e-a6fc-e19264eddb92/IASDR+2021+-+Workshop+Presentation+%282%29.png"
curl -sL -o "$BASE/publications/publications-header.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/fddbafc2-7284-4010-a9bb-75ab08e3db79/Frame+70.png"

echo "Downloading homepage images..."
curl -sL -o "$BASE/home/hero.jpg" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616040585918-H9KZ0DY0ZR0CP8MYD3X2/4C70FDA4-2AF2-4803-8DF5-77C85A4B8F83.jpg"
curl -sL -o "$BASE/home/card-jpmorgan.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1732598885556-VQOWBS3548A5BQG8KT1G/Group+402.png"
curl -sL -o "$BASE/home/card-theleague.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1612676534853-VEB6XIMR4VTP04M45NDM/The+League+Spread.png"
curl -sL -o "$BASE/home/card-lyftotto.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1614227737702-JW0BAYWAIEL13VITZ2LO/Group+5.png"
curl -sL -o "$BASE/home/card-ontra.png" "https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1612676572809-DFRSP5IN4X6KYSD0785X/incloud+poster.png"

echo "Done! Verifying downloads..."
for f in "$BASE"/bio/* "$BASE"/publications/* "$BASE"/home/*; do
    if [ -f "$f" ]; then
        size=$(wc -c < "$f")
        echo "  $f ($size bytes)"
    fi
done
