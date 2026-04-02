#!/usr/bin/env python3
"""
Add auto-scroll toggle and transpose buttons to songbook
"""

with open('index.html', 'r') as f:
    html = f.read()

# Add CSS for new controls
new_css = """
        .song-controls {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .control-btn {
            padding: 8px 16px;
            background: rgba(255,255,255,0.3);
            color: white;
            border: 2px solid white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.85em;
            font-weight: bold;
            transition: all 0.2s;
        }

        .control-btn:hover {
            background: white;
            color: #2E8B57;
        }

        .control-btn.active {
            background: white;
            color: #2E8B57;
        }

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

        .scroll-speed {
            display: flex;
            align-items: center;
            gap: 5px;
            margin-top: 5px;
        }

        .speed-btn {
            padding: 4px 8px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 1px solid white;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75em;
            transition: all 0.2s;
        }

        .speed-btn:hover {
            background: rgba(255,255,255,0.4);
        }

        .speed-btn.active {
            background: white;
            color: #2E8B57;
        }

        @media print {
            .song-controls,
            .transpose-controls,
            .scroll-speed {
                display: none !important;
            }
        }
"""

# Insert new CSS before closing </style>
html = html.replace('    </style>', new_css + '    </style>')

# Update the selectSong function to include new controls
old_select_function = """            // Update header
            document.getElementById('contentHeader').innerHTML = `
                <h2>${song.title}</h2>
                <span class="artist">${song.artist}</span>
                <div class="theory-badge">${song.theory}</div>
                <button class="print-btn visible" onclick="printSong()">🖨️ Print</button>
            `;"""

new_select_function = """            // Update header
            document.getElementById('contentHeader').innerHTML = `
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

html = html.replace(old_select_function, new_select_function)

# Add JavaScript functions for auto-scroll and transpose
new_js = """

        // Auto-scroll functionality
        let autoScrollInterval = null;
        let scrollSpeed = 1; // pixels per interval
        let scrollSpeedMultiplier = 1; // 0.5 = slow, 1 = normal, 1.5 = fast, 2 = very fast

        function toggleAutoScroll() {
            const btn = document.getElementById('autoScrollBtn');
            const speedControls = document.getElementById('scrollSpeedControls');

            if (autoScrollInterval) {
                // Stop scrolling
                clearInterval(autoScrollInterval);
                autoScrollInterval = null;
                btn.classList.remove('active');
                speedControls.style.display = 'none';
            } else {
                // Start scrolling
                const contentBody = document.getElementById('contentBody');
                autoScrollInterval = setInterval(() => {
                    contentBody.scrollTop += scrollSpeed * scrollSpeedMultiplier;

                    // Stop at bottom
                    if (contentBody.scrollTop >= contentBody.scrollHeight - contentBody.clientHeight) {
                        clearInterval(autoScrollInterval);
                        autoScrollInterval = null;
                        btn.classList.remove('active');
                        speedControls.style.display = 'none';
                    }
                }, 50);
                btn.classList.add('active');
                speedControls.style.display = 'flex';
            }
        }

        function setScrollSpeed(multiplier) {
            scrollSpeedMultiplier = multiplier;

            // Update active button
            document.querySelectorAll('.speed-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.currentTarget.classList.add('active');
        }

        // Stop auto-scroll on manual scroll
        document.addEventListener('DOMContentLoaded', function() {
            const contentBody = document.getElementById('contentBody');
            let isManualScroll = false;

            contentBody.addEventListener('wheel', function() {
                if (autoScrollInterval) {
                    isManualScroll = true;
                    clearInterval(autoScrollInterval);
                    autoScrollInterval = null;
                    const btn = document.getElementById('autoScrollBtn');
                    if (btn) btn.classList.remove('active');
                    const speedControls = document.getElementById('scrollSpeedControls');
                    if (speedControls) speedControls.style.display = 'none';
                }
            });
        });

        // Transpose functionality
        let currentTranspose = 0;
        let currentSongId = null;
        let originalChords = null;

        const chromaticScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
        const alternateNames = {
            'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'
        };

        function transposeChord(chord, steps) {
            if (!chord || chord.trim() === '') return chord;

            // Match chord pattern: root note (with optional # or b) + modifiers
            const chordRegex = /^([A-G][#b]?)(.*)/;
            const match = chord.match(chordRegex);

            if (!match) return chord;

            let root = match[1];
            const modifiers = match[2];

            // Convert alternate names to standard
            if (alternateNames[root]) {
                root = alternateNames[root];
            }

            // Find current position in chromatic scale
            let index = chromaticScale.indexOf(root);
            if (index === -1) return chord;

            // Transpose
            index = (index + steps + 12) % 12;

            return chromaticScale[index] + modifiers;
        }

        function transposeChordLine(line, steps) {
            // This regex finds chord patterns in a line
            // Matches: A, Am, A7, Asus4, C/G, etc.
            const chordPattern = /\b([A-G][#b]?(?:maj|min|m|sus|add|aug|dim|[0-9])*(?:\/[A-G][#b]?)?)\b/g;

            return line.replace(chordPattern, (match) => {
                // Handle slash chords (e.g., C/G)
                if (match.includes('/')) {
                    const [rootChord, bassNote] = match.split('/');
                    return transposeChord(rootChord, steps) + '/' + transposeChord(bassNote, steps);
                }
                return transposeChord(match, steps);
            });
        }

        function updateTransposeDisplay() {
            const display = document.getElementById('transposeDisplay');
            if (!display) return;

            if (currentTranspose === 0) {
                display.textContent = 'Original';
            } else if (currentTranspose > 0) {
                display.textContent = '+' + currentTranspose;
            } else {
                display.textContent = currentTranspose.toString();
            }
        }

        function transposeUp() {
            currentTranspose++;
            if (currentTranspose > 11) currentTranspose = 11;
            applyTranspose();
        }

        function transposeDown() {
            currentTranspose--;
            if (currentTranspose < -11) currentTranspose = -11;
            applyTranspose();
        }

        function applyTranspose() {
            if (!originalChords) return;

            const lines = originalChords.split('\\n');
            const transposedLines = lines.map(line => {
                // Only transpose lines that look like chord lines
                // (lines with chord symbols, not lyrics)
                if (/^[A-G]/.test(line.trim()) || /\s+[A-G][#b]?(?:m|maj|sus|add|aug|dim|[0-9])*/.test(line)) {
                    return transposeChordLine(line, currentTranspose);
                }
                return line;
            });

            const transposedChords = transposedLines.join('\\n');

            // Update the display
            const chordContent = document.querySelector('.chord-content pre');
            if (chordContent) {
                chordContent.textContent = transposedChords;
            }

            updateTransposeDisplay();
        }

        // Store original chords when selecting a song
        const originalSelectSong = selectSong;
        selectSong = function(songId) {
            // Reset transpose when changing songs
            currentTranspose = 0;
            currentSongId = songId;

            // Stop auto-scroll if active
            if (autoScrollInterval) {
                clearInterval(autoScrollInterval);
                autoScrollInterval = null;
            }

            // Call original function
            originalSelectSong(songId);

            // Store original chords
            const song = songs.find(s => s.id === songId);
            if (song) {
                originalChords = song.chords;
            }

            updateTransposeDisplay();
        };"""

# Insert new JavaScript before closing </script>
html = html.replace('    </script>', new_js + '    </script>')

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added auto-scroll toggle with speed controls:")
print("   • Slow, Normal, Fast, Very Fast speeds")
print("   • Auto-stops at bottom or on manual scroll")
print("   • Toggle on/off with 📜 button")
print("\n✅ Added transpose functionality:")
print("   • + and − buttons to transpose up/down")
print("   • Shows current transposition (+1, -2, Original, etc.)")
print("   • Handles all chord types (major, minor, 7ths, sus, slash chords)")
print("   • Automatically converts enharmonic equivalents (Db → C#)")
print("   • Resets to original when changing songs")
print("\nFeatures added successfully!")
