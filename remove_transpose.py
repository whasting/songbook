#!/usr/bin/env python3
"""
Remove transpose functionality, keep auto-scroll
"""

with open('index.html', 'r') as f:
    html = f.read()

# Remove transpose controls from header
old_header = """            document.getElementById('contentHeader').innerHTML = `
                <h2>${song.title}</h2>
                <span class="artist">${song.artist}</span>
                <div class="theory-badge">${song.theory}</div>
                <button class="print-btn visible" onclick="printSong()">🖨️ Print</button>
                <div class="song-controls">
                    <button class="control-btn" id="autoScrollBtn" onclick="toggleAutoScroll()">
                        📜 Auto-Scroll
                    </button>
                    <div class="transpose-controls">
                        <button class="transpose-btn" onclick="transposeDown()">−</button>
                        <div class="transpose-display" id="transposeDisplay">
                            Original
                        </div>
                        <button class="transpose-btn" onclick="transposeUp()">+</button>
                    </div>
                </div>
                <div class="scroll-speed" id="scrollSpeedControls" style="display: none;">
                    <span style="font-size: 0.75em; color: white; opacity: 0.8;">Speed:</span>
                    <button class="speed-btn" onclick="setScrollSpeed(0.5)">Slow</button>
                    <button class="speed-btn active" onclick="setScrollSpeed(1)">Normal</button>
                    <button class="speed-btn" onclick="setScrollSpeed(1.5)">Fast</button>
                    <button class="speed-btn" onclick="setScrollSpeed(2)">Very Fast</button>
                </div>
            `;"""

new_header = """            document.getElementById('contentHeader').innerHTML = `
                <h2>${song.title}</h2>
                <span class="artist">${song.artist}</span>
                <div class="theory-badge">${song.theory}</div>
                <button class="print-btn visible" onclick="printSong()">🖨️ Print</button>
                <div class="song-controls">
                    <button class="control-btn" id="autoScrollBtn" onclick="toggleAutoScroll()">
                        📜 Auto-Scroll
                    </button>
                </div>
                <div class="scroll-speed" id="scrollSpeedControls" style="display: none;">
                    <span style="font-size: 0.75em; color: white; opacity: 0.8;">Speed:</span>
                    <button class="speed-btn" onclick="setScrollSpeed(0.5)">Slow</button>
                    <button class="speed-btn active" onclick="setScrollSpeed(1)">Normal</button>
                    <button class="speed-btn" onclick="setScrollSpeed(1.5)">Fast</button>
                    <button class="speed-btn" onclick="setScrollSpeed(2)">Very Fast</button>
                </div>
            `;"""

html = html.replace(old_header, new_header)

# Remove transpose CSS
transpose_css = """
        .transpose-controls {
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .transpose-btn {
            padding: 6px 12px;
            background: rgba(255,255,255,0.3);
            color: white;
            border: 2px solid white;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: bold;
            transition: all 0.2s;
            min-width: 35px;
        }

        .transpose-btn:hover {
            background: white;
            color: #2E8B57;
        }

        .transpose-display {
            padding: 6px 12px;
            background: rgba(255,255,255,0.2);
            color: white;
            border-radius: 6px;
            font-size: 0.85em;
            min-width: 60px;
            text-align: center;
        }
"""

html = html.replace(transpose_css, '')

# Remove transpose JavaScript (everything from "// Transpose functionality" to the end of the original selectSong wrapper)
transpose_js_start = html.find('        // Transpose functionality')
if transpose_js_start != -1:
    # Find the end of the transpose JS (before closing </script>)
    transpose_js_end = html.find('        // Store original chords when selecting a song', transpose_js_start)
    if transpose_js_end != -1:
        # Remove everything from transpose start to the wrapper function
        before_transpose = html[:transpose_js_start]
        # Keep everything after the wrapper
        after_wrapper = html.find('        };', transpose_js_end)
        if after_wrapper != -1:
            after_wrapper_end = html.find('\n', after_wrapper) + 1
            after = html[after_wrapper_end:]
            html = before_transpose + after

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Removed transpose functionality")
print("✅ Kept auto-scroll feature")
print("\nFeatures remaining:")
print("   • 📜 Auto-scroll with speed controls")
print("   • 🖨️ Print button")
print("   • All 25 songs with complete chords")
print("   • Theory analysis")
print("   • Capo information")
print("\nTranspose removed - songbook simplified!")
