#!/usr/bin/env python3
"""
Fix Print All to properly show all 25 songs with page breaks
"""

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace the printAll function with a better implementation
old_print_all = '''        function printAll() {
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
        }'''

new_print_all = '''        function printAll() {
            // Store current state
            const currentView = document.getElementById('contentHeader').innerHTML;
            const currentBody = document.getElementById('contentBody').innerHTML;

            // Build print view with all songs
            let allSongsHTML = '';

            songs.forEach((song, index) => {
                const isLast = index === songs.length - 1;
                const pageBreakStyle = isLast ? '' : 'page-break-after: always; break-after: page;';
                allSongsHTML += `
                    <div class="song-packet" style="padding: 30px 20px; ${pageBreakStyle}">
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

            // Print after content renders
            setTimeout(() => {
                window.print();

                // Restore previous view after print dialog closes
                setTimeout(() => {
                    document.getElementById('contentHeader').innerHTML = currentView;
                    document.getElementById('contentBody').innerHTML = currentBody;
                }, 500);
            }, 300);
        }'''

html = html.replace(old_print_all, new_print_all)

# 2. Update the print CSS to ensure page breaks work
old_css = '''            .song-packet {
                page-break-after: always;
                padding: 20px;
                margin: 0;
            }

            .song-packet:last-child {
                page-break-after: auto;
            }'''

new_css = '''            .song-packet {
                page-break-after: always !important;
                break-after: page !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                display: block !important;
                padding: 20px;
                margin: 0;
            }

            .song-packet:last-child {
                page-break-after: auto !important;
                break-after: auto !important;
            }'''

html = html.replace(old_css, new_css)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Fixed Print All functionality!")
print("\nImprovements:")
print("  • Added inline page-break styles for better compatibility")
print("  • Using both old (page-break-after) and new (break-after) CSS properties")
print("  • Increased render timeout to 300ms")
print("  • Added page-break-inside: avoid to prevent songs from splitting")
print("\nAll 25 songs should now print on separate pages!")
