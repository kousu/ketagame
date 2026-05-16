
# this works (so loong as the background is white) but the results have pixellation
mogrify -format png -transparent white -fuzz 5%  *.png

debackground_broken() {
# XXX this doesn't work
# - Create a mask from the white background
# - Blur the mask
# - Use it only as the alpha channel
# - Keep original RGB untouched
for f in *.png; do
  magick "$f" \
    \( +clone -fuzz 5% -fill black -opaque white -fill white +opaque white -blur 0x2 \) \
    -alpha off -compose CopyOpacity -composite \
    "$f"
done
}
