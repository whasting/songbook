#!/usr/bin/env python3
"""
Add Print All button that prints all songs as individual packets
"""

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add Print All button next to Home button in sidebar
old_home_btn = '''                <button class="home-btn" onclick="showHome()">🏠 Home</button>'''

new_buttons = '''                <button class="home-btn" onclick="showHome()">🏠 Home</button>
                <button class="home-btn" onclick="printAll()">🖨️ Print All</button>'''

html = html.replace(old_home_btn, new_buttons)

# 2. Add CSS for print mode - each song on separate page
old_print_css = '''        @media print {
            .song-controls,
            .transpose-controls,
            .scroll-speed {
                display: none !important;
            }
        }'''

new_print_css = '''        @media print {
            .song-controls,
            .transpose-controls,
            .scroll-speed {
                display: none !important;
            }

            .sidebar {
                display: none !important;
            }

            .main-content {
                width: 100% !important;
                margin: 0 !important;
            }

            .song-packet {
                page-break-after: always;
                padding: 20px;
                margin: 0;
            }

            .song-packet:last-child {
                page-break-after: auto;
            }

            .content-header {
                margin-bottom: 20px;
            }

            .print-btn {
                display: none !important;
            }
        }'''

html = html.replace(old_print_css, new_print_css)

# 3. Add printAll() function before the closing </script> tag
print_all_function = '''
        function printAll() {
            // Store current state
            const currentView = document.getElementById('contentHeader').innerHTML;
            const currentBody = document.getElementById('contentBody').innerHTML;

            // Build print view with all songs
            let allSongsHTML = '';

            songs.forEach((song, index) => {
                const isLast = index === songs.length - 1;
                allSongsHTML += `
                    <div class="song-packet" style="padding: 30px 20px;">
                        <div style="margin-bottom: 20px; border-bottom: 2px solid #2E8B57; padding-bottom: 10px;">
                            <h2 style="margin: 0 0 5px 0; color: #2E8B57;">${song.title}</h2>
                            <div style="color: #5BA3C7; font-size: 0.9em; margin-bottom: 5px;">${song.artist}</div>
                            <div style="color: #666; font-size: 0.85em;">${song.theory}</div>
                        </div>
                        <pre style="font-family: 'Courier New', monospace; white-space: pre-wrap; line-height: 1.6; font-size: 0.95em;">${song.chords}</pre>
                    </div>
                `;
            });

            // Update display
            document.getElementById('contentHeader').innerHTML = '<h2 style="color: #2E8B57;">Complete Songbook - 25 Country Classics</h2>';
            document.getElementById('contentBody').innerHTML = allSongsHTML;

            // Print
            setTimeout(() => {
                window.print();

                // Restore previous view after print dialog closes
                setTimeout(() => {
                    document.getElementById('contentHeader').innerHTML = currentView;
                    document.getElementById('contentBody').innerHTML = currentBody;
                }, 100);
            }, 100);
        }
'''

# Find the last function before </script> and add printAll after it
script_end = html.rfind('    </script>')
html = html[:script_end] + print_all_function + '\n' + html[script_end:]

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added Print All button!")
print("\nFeatures:")
print("  • 🖨️ Print All button in sidebar")
print("  • Each song starts on a new page")
print("  • Professional packet format")
print("  • Automatically restores view after printing")
print("\nPrint all 25 songs as individual packets with one click!")
