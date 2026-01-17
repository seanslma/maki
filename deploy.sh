#!/bin/bash

# --- CONFIGURATION ---
# Update these paths to match your Ubuntu folders
MAIN_SITE_REPO="$HOME/dev/seanslma.github.io"
MAKI_SUBFOLDER="$MAIN_SITE_REPO/maki"

echo "Starting build of Maki..."

# 1. Build the MkDocs site
# This triggers the hook to update the time/year
mkdocs build

echo "Running high-performance minification..."
python3 -c "
import os
import minify_html

site_dir = '_site'
for root, dirs, files in os.walk(site_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                # This engine is much more 'forgiving' than the old one
                minified = minify_html.minify(content, minify_js=True, minify_css=True)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(minified)
            except Exception as e:
                print(f'⚠️ Could not minify {path}: {e}')
"

# 2. Ensure the destination exists
mkdir -p "$MAKI_SUBFOLDER"

# 3. Clear old files in the destination (to prevent ghost files)
echo "Cleaning old files in $MAKI_SUBFOLDER..."
rm -rf "${MAKI_SUBFOLDER:?}"/*

# 4. Copy new files
echo "Copying built files to main site repo..."
cp -r _site/* "$MAKI_SUBFOLDER/"

# 5. Navigate to main repo and push
# echo "Committing and pushing to GitHub Pages..."
# cd "$MAIN_SITE_REPO"
# git add maki/
# git commit -m "Update maki docs at $(date '+%Y-%m-%d %H:%M:%S')"
# git push origin main

echo "Done! Site will update at seanslma.github.io/maki"
