#!/usr/bin/env python3
"""
Add home button, key filters, and print button to songbook
"""

with open('index.html', 'r') as f:
    html = f.read()

# Add CSS for new elements (insert before closing </style>)
new_css = """
        .home-btn {
            display: inline-block;
            margin-top: 10px;
            padding: 8px 16px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 2px solid white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.85em;
            font-weight: bold;
            transition: all 0.2s;
            text-decoration: none;
        }

        .home-btn:hover {
            background: white;
            color: #8B4513;
        }

        .filter-row {
            display: flex;
            padding: 10px;
            gap: 5px;
            background: #f5f5f5;
        }

        .filter-row:first-of-type {
            border-bottom: 1px solid #ddd;
        }

        .filter-row:last-of-type {
            border-bottom: 2px solid #ddd;
        }

        .filter-label {
            display: flex;
            align-items: center;
            font-size: 0.75em;
            font-weight: bold;
            color: #8B4513;
            padding: 0 5px;
            min-width: 45px;
        }

        .print-btn {
            position: absolute;
            top: 20px;
            right: 30px;
            padding: 10px 20px;
            background: rgba(255,255,255,0.3);
            color: white;
            border: 2px solid white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: bold;
            transition: all 0.2s;
            display: none;
        }

        .print-btn:hover {
            background: white;
            color: #8B4513;
        }

        .print-btn.visible {
            display: block;
        }

        .content-header {
            position: relative;
        }

        @media print {
            .sidebar,
            .content-header,
            .print-btn,
            .theory-analysis {
                display: none !important;
            }

            .app-container {
                padding: 0;
            }

            .main-content {
                box-shadow: none;
                border-radius: 0;
            }

            .chord-content {
                border: none;
                padding: 0;
            }

            .chord-content pre {
                font-size: 12px;
            }
        }
"""

html = html.replace('    </style>', new_css + '    </style>')

# Update sidebar header to include home button
old_header = '''            <div class="sidebar-header">
                <h1>🎸 Country Songbook</h1>
                <p>17 Classic Hits with Theory Analysis</p>
            </div>'''

new_header = '''            <div class="sidebar-header">
                <h1>🎸 Country Songbook</h1>
                <p>17 Classic Hits with Theory Analysis</p>
                <button class="home-btn" onclick="showHome()">🏠 Home</button>
            </div>'''

html = html.replace(old_header, new_header)

# Update filter buttons to include progression and key filters
old_filters = '''            <div class="filter-buttons">
                <button class="filter-btn active" onclick="filterSongs('all')">All</button>
                <button class="filter-btn" onclick="filterSongs('I-IV-V')">I-IV-V</button>
                <button class="filter-btn" onclick="filterSongs('I-V-vi-IV')">I-V-vi-IV</button>
            </div>'''

new_filters = '''            <div class="filter-row">
                <span class="filter-label">Prog:</span>
                <button class="filter-btn active" data-filter-type="progression" onclick="filterSongs('all', 'progression')">All</button>
                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-IV-V', 'progression')">I-IV-V</button>
                <button class="filter-btn" data-filter-type="progression" onclick="filterSongs('I-V-vi-IV', 'progression')">I-V-vi-IV</button>
            </div>
            <div class="filter-row">
                <span class="filter-label">Key:</span>
                <button class="filter-btn active" data-filter-type="key" onclick="filterSongs('all', 'key')">All</button>
                <button class="filter-btn" data-filter-type="key" onclick="filterSongs('G', 'key')">G</button>
                <button class="filter-btn" data-filter-type="key" onclick="filterSongs('D', 'key')">D</button>
                <button class="filter-btn" data-filter-type="key" onclick="filterSongs('C', 'key')">C</button>
            </div>'''

html = html.replace(old_filters, new_filters)

# Add print button to content header template in selectSong function
old_header_template = '''            document.getElementById('contentHeader').innerHTML = `
                <h2>${song.title}</h2>
                <span class="artist">${song.artist}</span>
                <div class="theory-badge">${song.theory}</div>
            `;'''

new_header_template = '''            document.getElementById('contentHeader').innerHTML = `
                <h2>${song.title}</h2>
                <span class="artist">${song.artist}</span>
                <div class="theory-badge">${song.theory}</div>
                <button class="print-btn visible" onclick="printSong()">🖨️ Print</button>
            `;'''

html = html.replace(old_header_template, new_header_template)

# Update filterSongs function to handle both progression and key filters
old_filter_function = '''        function filterSongs(filter) {
            // Update button states
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.currentTarget.classList.add('active');

            // Filter songs
            const songItems = document.querySelectorAll('.song-item');
            songItems.forEach(item => {
                if (filter === 'all') {
                    item.style.display = 'block';
                } else {
                    const progression = item.getAttribute('data-progression');
                    if (progression.includes(filter)) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });

            // Hide empty categories
            document.querySelectorAll('.song-category').forEach(cat => {
                const visibleSongs = cat.querySelectorAll('.song-item[style*="display: block"], .song-item:not([style*="display: none"])');
                if (filter !== 'all' && visibleSongs.length === 0) {
                    cat.style.display = 'none';
                } else {
                    cat.style.display = 'block';
                }
            });
        }'''

new_filter_function = '''        let currentFilters = {
            progression: 'all',
            key: 'all'
        };

        function filterSongs(filter, filterType) {
            // Update filter state
            currentFilters[filterType] = filter;

            // Update button states for this filter type
            document.querySelectorAll(`.filter-btn[data-filter-type="${filterType}"]`).forEach(btn => {
                btn.classList.remove('active');
            });
            event.currentTarget.classList.add('active');

            // Filter songs based on both filters
            const songItems = document.querySelectorAll('.song-item');
            songItems.forEach(item => {
                let showItem = true;

                // Check progression filter
                if (currentFilters.progression !== 'all') {
                    const progression = item.getAttribute('data-progression');
                    if (!progression.includes(currentFilters.progression)) {
                        showItem = false;
                    }
                }

                // Check key filter
                if (currentFilters.key !== 'all') {
                    const key = item.getAttribute('data-key');
                    if (!key.includes(currentFilters.key)) {
                        showItem = false;
                    }
                }

                item.style.display = showItem ? 'block' : 'none';
            });

            // Hide empty categories
            document.querySelectorAll('.song-category').forEach(cat => {
                const visibleSongs = cat.querySelectorAll('.song-item[style*="display: block"], .song-item:not([style*="display: none"])');
                if (visibleSongs.length === 0) {
                    cat.style.display = 'none';
                } else {
                    cat.style.display = 'block';
                }
            });
        }

        function showHome() {
            // Clear active song
            document.querySelectorAll('.song-item').forEach(item => {
                item.classList.remove('active');
            });

            // Reset filters
            currentFilters = { progression: 'all', key: 'all' };
            document.querySelectorAll('.filter-btn').forEach(btn => {
                if (btn.textContent.includes('All')) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // Show all songs
            document.querySelectorAll('.song-item').forEach(item => {
                item.style.display = 'block';
            });
            document.querySelectorAll('.song-category').forEach(cat => {
                cat.style.display = 'block';
            });

            // Show welcome screen
            document.getElementById('contentHeader').innerHTML = `
                <h2>Welcome to Your Songbook</h2>
                <span class="artist">Select a song from the left to view chords</span>
            `;

            document.getElementById('contentBody').innerHTML = `
                <div class="welcome-message">
                    <h2>🎵 Music Theory Patterns</h2>
                    <p>Click any song to see its chords and theory analysis</p>

                    <div class="theory-summary">
                        <h3>Common Progressions in This Collection:</h3>

                        <div class="progression-group">
                            <strong>I-IV-V (Classic Country)</strong><br>
                            <small>10 songs use this or variations</small><br>
                            • I Should Have Been a Cowboy<br>
                            • Chattahoochee<br>
                            • Family Tradition<br>
                            • Boot Scootin' Boogie<br>
                            • Pickup Man
                        </div>

                        <div class="progression-group">
                            <strong>I-V-vi-IV (Modern Country/Pop)</strong><br>
                            <small>3 songs use this progression</small><br>
                            • Gone Country<br>
                            • Drive (For Daddy Gene)<br>
                            • I Love This Bar
                        </div>

                        <div class="progression-group">
                            <strong>Modal Mixture (Borrowed Chords)</strong><br>
                            <small>3 songs use chords from parallel minor</small><br>
                            • How Do You Like Me Now (bVII)<br>
                            • A Country Boy Can Survive (v)<br>
                            • Travelin' Soldier (bVII)
                        </div>

                        <div class="progression-group">
                            <strong>Keys Used:</strong><br>
                            <small>G major: 7 songs | D major: 4 songs | C major: 3 songs</small><br>
                            • Most songs use guitar-friendly open chord keys<br>
                            • E and A major also appear (2 songs each)
                        </div>
                    </div>
                </div>
            `;
        }

        function printSong() {
            window.print();
        }'''

html = html.replace(old_filter_function, new_filter_function)

# Update song items to include data-key attribute
html = html.replace(
    'data-progression="${song.progression}">',
    'data-progression="${song.progression}" data-key="${song.key}">'
)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added home button")
print("✅ Added key filter buttons (G, D, C)")
print("✅ Added print button for chord charts")
print("✅ Updated filter logic to handle multiple filters")
print("\nSongbook updated successfully!")
