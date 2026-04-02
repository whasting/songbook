#!/usr/bin/env python3
"""
1. Fix homepage to correctly separate I-V-IV from I-IV-V songs
2. Fix Print All with a new approach using a separate print container
"""

with open('index.html', 'r') as f:
    html = f.read()

# 1. Fix the homepage progression groups
# Remove incorrect I-IV-V entry that includes I-V-IV songs
old_homepage = '''                        <div class="progression-group">
                            <strong>I-IV-V (Classic Country)</strong><br>
                            <small>10 songs use this or variations</small><br>
                            • I Should Have Been a Cowboy<br>
                            • I Love This Bar<br>
                            • Gone Country<br>
                            • All My Exes Live in Texas<br>
                            • Boot Scootin' Boogie<br>
                            • Friends in Low Places<br>
                            • A Country Boy Can Survive<br>
                            • Pickup Man<br>
                            • Boys 'Round Here<br>
                            • Rocky Mountain High
                        </div>'''

new_homepage = '''                        <div class="progression-group">
                            <strong>I-IV-V (Classic Country)</strong><br>
                            <small>6 songs use this progression</small><br>
                            • I Love This Bar<br>
                            • Gone Country<br>
                            • All My Exes Live in Texas<br>
                            • Boot Scootin' Boogie<br>
                            • Friends in Low Places<br>
                            • A Country Boy Can Survive
                        </div>

                        <div class="progression-group">
                            <strong>I-V-IV (Blues/Rock Influenced)</strong><br>
                            <small>4 songs - Classic rock-influenced progression</small><br>
                            • I Should Have Been a Cowboy<br>
                            • Chattahoochee<br>
                            • Hey Good Lookin'<br>
                            • Diggin' Up Bones
                        </div>'''

html = html.replace(old_homepage, new_homepage)

# 2. Completely rewrite printAll function with a new approach
# Remove old printAll function
old_print_all_start = html.find('        function printAll() {')
old_print_all_end = html.find('        }', old_print_all_start) + 9  # Include the closing brace
old_print_all = html[old_print_all_start:old_print_all_end]

new_print_all = '''        function printAll() {
            // Create a hidden print container
            const printContainer = document.createElement('div');
            printContainer.id = 'printAllContainer';
            printContainer.style.display = 'none';

            // Build all songs HTML
            songs.forEach((song, index) => {
                const songDiv = document.createElement('div');
                songDiv.style.pageBreakAfter = index < songs.length - 1 ? 'always' : 'auto';
                songDiv.style.breakAfter = index < songs.length - 1 ? 'page' : 'auto';
                songDiv.style.padding = '30px 20px';

                songDiv.innerHTML = `
                    <div style="margin-bottom: 20px; border-bottom: 2px solid #2E8B57; padding-bottom: 10px;">
                        <h2 style="margin: 0 0 5px 0; color: #2E8B57;">${song.title}</h2>
                        <div style="color: #5BA3C7; font-size: 0.9em; margin-bottom: 5px;">${song.artist}</div>
                        <div style="color: #666; font-size: 0.85em;">${song.theory}</div>
                    </div>
                    <pre style="font-family: 'Courier New', monospace; white-space: pre-wrap; line-height: 1.6; font-size: 0.95em;">${song.chords}</pre>
                `;

                printContainer.appendChild(songDiv);
            });

            // Add to body
            document.body.appendChild(printContainer);

            // Show print container, hide main content
            printContainer.style.display = 'block';
            document.querySelector('.app-container').style.display = 'none';

            // Print
            window.print();

            // Cleanup after print
            window.addEventListener('afterprint', function cleanup() {
                printContainer.remove();
                document.querySelector('.app-container').style.display = 'flex';
                window.removeEventListener('afterprint', cleanup);
            });
        }'''

html = html.replace(old_print_all, new_print_all)

# 3. Add CSS for print container
print_container_css = '''
        #printAllContainer {
            display: none;
        }

        @media print {
            #printAllContainer {
                display: block !important;
            }

            #printAllContainer > div {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
        }
'''

# Add before closing </style>
style_end = html.rfind('    </style>')
html = html[:style_end] + print_container_css + '\n' + html[style_end:]

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Fixed homepage progression groups!")
print("\nI-IV-V songs (6 total):")
print("  • I Love This Bar")
print("  • Gone Country")
print("  • All My Exes Live in Texas")
print("  • Boot Scootin' Boogie")
print("  • Friends in Low Places")
print("  • A Country Boy Can Survive")

print("\nI-V-IV songs (4 total):")
print("  • I Should Have Been a Cowboy")
print("  • Chattahoochee")
print("  • Hey Good Lookin'")
print("  • Diggin' Up Bones")

print("\n✅ Rewrote Print All function!")
print("New approach:")
print("  • Creates separate hidden print container")
print("  • Hides main app during print")
print("  • Uses afterprint event for cleanup")
print("  • Each song has explicit page-break styles")
