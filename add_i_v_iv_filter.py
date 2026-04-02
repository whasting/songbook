#!/usr/bin/env python3
"""
Add I-V-IV progression filter and homepage entry
"""

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add I-V-IV filter button after I-V-vi-IV
old_filters = '''                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-IV-V', 'progression')">I-IV-V</button>
                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-V-vi-IV', 'progression')">I-V-vi-IV</button>'''

new_filters = '''                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-IV-V', 'progression')">I-IV-V</button>
                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-V-vi-IV', 'progression')">I-V-vi-IV</button>
                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-V-IV', 'progression')">I-V-IV</button>'''

html = html.replace(old_filters, new_filters)

# 2. Add I-V-IV section to homepage theory analysis
# Find the I-V-vi-IV section and add I-V-IV after it
old_homepage = '''                        <div class="progression-group">
                            <strong>I-V-vi-IV (Modern Country/Pop)</strong><br>
                            <small>3 songs - The "pop progression"</small><br>
                            • Ready To Run<br>
                            • Wide Open Spaces<br>
                            • Cowboy Take Me Away
                        </div>'''

new_homepage = '''                        <div class="progression-group">
                            <strong>I-V-vi-IV (Modern Country/Pop)</strong><br>
                            <small>3 songs - The "pop progression"</small><br>
                            • Ready To Run<br>
                            • Wide Open Spaces<br>
                            • Cowboy Take Me Away
                        </div>

                        <div class="progression-group">
                            <strong>I-V-IV (Blues/Rock Influence)</strong><br>
                            <small>4 songs - Classic rock-influenced progression</small><br>
                            • I Should Have Been a Cowboy<br>
                            • Chattahoochee<br>
                            • Hey Good Lookin'<br>
                            • Diggin' Up Bones
                        </div>'''

html = html.replace(old_homepage, new_homepage)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added I-V-IV progression filter and homepage entry!")
print("\nI-V-IV Songs (4 total):")
print("  • I Should Have Been a Cowboy")
print("  • Chattahoochee")
print("  • Hey Good Lookin'")
print("  • Diggin' Up Bones")
print("\nFilter button added to sidebar")
print("Homepage entry added to theory analysis")
