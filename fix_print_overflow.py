#!/usr/bin/env python3
"""
Fix Print All by removing overflow from content-body in print mode
"""

with open('index.html', 'r') as f:
    html = f.read()

# Find the second @media print block (the one with song-packet)
# and add content-body overflow fix

old_print_css = '''            .main-content {
                width: 100% !important;
                margin: 0 !important;
            }

            .song-packet {'''

new_print_css = '''            .main-content {
                width: 100% !important;
                margin: 0 !important;
            }

            .content-body {
                overflow: visible !important;
                height: auto !important;
                padding: 0 !important;
            }

            .song-packet {'''

html = html.replace(old_print_css, new_print_css)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Fixed overflow issue in print mode!")
print("\nThe problem was:")
print("  • content-body has overflow-y: auto (scrollable)")
print("  • Page breaks don't work in scrollable containers")
print("\nThe fix:")
print("  • Set overflow: visible in print mode")
print("  • Set height: auto to allow content to flow")
print("\nAll 25 songs should now print on separate pages!")
