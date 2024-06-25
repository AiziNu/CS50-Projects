import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression pattern to find the src attribute of an iframe with a YouTube URL
    pattern = re.compile(r'<iframe[^>]*\s+src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"')
    match = pattern.search(s)
    if match:
        url = match.group(1)
        # Convert the extracted URL to the shorter youtu.be format
        video_id = url.split('/')[-1]
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
