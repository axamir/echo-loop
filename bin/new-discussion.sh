#!/bin/bash
# new-discussion.sh - ساخت پوشه گفتگوی جدید با تاریخ و عنوان
if [ -z "$1" ]; then
  echo "استفاده: new-discussion.sh عنوان-گفتگو"
  exit 1
fi
TOPIC="$1"
DATE=$(date +%Y-%m-%d)
FOLDER="$DATE"_"$TOPIC"
mkdir -p "$FOLDER"
cd "$FOLDER"
for lang in fa en; do
  for file in conversation summary reflections; do
    echo "# $file ($lang)" > "$file.$lang.md"
    echo "" >> "$file.$lang.md"
    echo "متن گفتگو به زبان $lang" >> "$file.$lang.md"
  done
done
echo "# Links" > links.md
echo "{}" > meta.json
cd ..
echo "پوشه $FOLDER ساخته شد."
