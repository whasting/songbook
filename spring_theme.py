#!/usr/bin/env python3
"""
Update to Spring Frolic V theme with spring colors
"""

with open('index.html', 'r') as f:
    html = f.read()

# Update title
html = html.replace('<title>90s Country Songbook</title>', '<title>Spring Frolic V Country Songbook</title>')
html = html.replace('🎸 Country Songbook', '🌸 Spring Frolic V')
html = html.replace('90s Country Songbook', 'Spring Frolic V Country Songbook')
html = html.replace('Country Songbook - For Personal Use Only', 'Spring Frolic V - Country Songbook 2026')

# Update brown gradient to spring green/yellow gradient
html = html.replace(
    'linear-gradient(135deg, #8B4513 0%, #D2691E 100%)',
    'linear-gradient(135deg, #90EE90 0%, #FFD700 100%)'  # Light green to gold
)

# Update brown colors to spring colors
html = html.replace('#8B4513', '#2E8B57')  # Saddle brown -> Sea green
html = html.replace('#D2691E', '#FFD700')  # Chocolate -> Gold
html = html.replace('#8b4513', '#2E8B57')  # lowercase version

# Update sidebar header background to spring theme
html = html.replace(
    'background: linear-gradient(135deg, #90EE90 0%, #FFD700 100%);',
    'background: linear-gradient(135deg, #87CEEB 0%, #98FB98 100%);',
    1  # Only first occurrence (sidebar header)
)

# Update content header to spring theme
old_content_header_bg = '''        .content-header {
            background: linear-gradient(135deg, #90EE90 0%, #FFD700 100%);'''

new_content_header_bg = '''        .content-header {
            background: linear-gradient(135deg, #87CEEB 0%, #98FB98 100%);'''

html = html.replace(old_content_header_bg, new_content_header_bg)

# Update filter button colors to spring theme
old_filter_btn = '''        .filter-btn.active {
            background: linear-gradient(135deg, #90EE90 0%, #FFD700 100%);'''

new_filter_btn = '''        .filter-btn.active {
            background: linear-gradient(135deg, #98FB98 0%, #87CEEB 100%);'''

html = html.replace(old_filter_btn, new_filter_btn)

# Update song-item active state to spring colors
old_song_active = '''        .song-item.active {
            background: linear-gradient(135deg, #90EE90 0%, #FFD700 100%);'''

new_song_active = '''        .song-item.active {
            background: linear-gradient(135deg, #98FB98 0%, #87CEEB 100%);'''

html = html.replace(old_song_active, new_song_active)

# Update border colors to spring green
html = html.replace('border-left: 4px solid #FFD700', 'border-left: 4px solid #98FB98')
html = html.replace('border-left: 3px solid #FFD700', 'border-left: 3px solid #87CEEB')
html = html.replace('border: 2px solid #FFD700', 'border: 2px solid #98FB98')
html = html.replace('border-bottom: 3px solid #FFD700', 'border-bottom: 3px solid #87CEEB')

# Update theory analysis box to spring yellow
html = html.replace('background: #fff9e6;', 'background: #FFFACD;')  # Light yellow

# Update scrollbar colors
html = html.replace('background: #FFD700;', 'background: #98FB98;')
html = html.replace('background: #90EE90;', 'background: #87CEEB;')

# Update header subtitle
html = html.replace(
    '<p>17 Classic Hits with Theory Analysis</p>',
    '<p>17 Country Classics for Spring 2026</p>'
)

# Update welcome message
html = html.replace(
    '<h2>Welcome to Your Songbook</h2>',
    '<h2>🌸 Welcome to Spring Frolic V</h2>'
)

html = html.replace(
    '<span class="artist">Select a song from the left to view chords</span>',
    '<span class="artist">Select a song to view chords & theory analysis</span>'
)

# Update password box colors
old_pwd_btn = '''        .password-box button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #90EE90 0%, #FFD700 100%);'''

new_pwd_btn = '''        .password-box button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #98FB98 0%, #87CEEB 100%);'''

html = html.replace(old_pwd_btn, new_pwd_btn)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Updated title to 'Spring Frolic V Country Songbook'")
print("✅ Changed colors to spring theme:")
print("   • Light green & sky blue gradients")
print("   • Pale yellow accent colors")
print("   • Sea green text colors")
print("\nSpring theme applied successfully!")
