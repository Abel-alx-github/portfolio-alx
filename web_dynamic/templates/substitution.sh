#!/usr/bin/bash

#substitute static wit ../static in a file



# Check if a file is provided as an argument
if [ $# -eq 0 ]; then
  echo "Error: Please provide a filename as an argument."
    exit 1
  fi

# Get the filename from the first argument

filename="$1"

# Create a temporary file for the modified content

tempfile=$(mktemp)

# Use sed to replace "static" with "../static" in the file

sed 's/image/\.\.\/static\/image/g' "$filename" > "$tempfile"
#sed 's/style/\.\.\/static\/style/g' "$filename" > "$tempfile"
# Check if the sed command was successful (exit code 0 indicates success)
if [ $? -eq 0 ]; then
  # Move the temporary file over the original file (atomic replacement)
  mv "$tempfile" "$filename"
  echo "Successfully replaced 'static' with '../static' in '$filename'"
else
   echo "Error: Failed to replace strings in '$filename'"
   # Clean up the temporary file if sed failed
   rm "$tempfile"
fi

