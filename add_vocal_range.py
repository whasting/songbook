#!/usr/bin/env python3
"""
Add vocal range comfort indicators for baritone (high note: G4)
"""

# Key transposition due to capo (semitones up)
capo_transpose = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8
}

# Typical highest notes for country songs in various keys
# Based on common melody ranges (usually within an octave + a 5th from root)
key_high_notes = {
    'G': 'D5',   # Country songs in G typically go up to D5
    'A': 'E5',   # Country songs in A typically go up to E5
    'D': 'A4',   # Country songs in D typically go up to A4
    'C': 'G4',   # Country songs in C typically go up to G4
    'E': 'B4',   # Country songs in E typically go up to B4
    'F': 'C5',   # Country songs in F typically go up to C5
    'Am': 'E5',  # Minor keys similar to relative major
    'Em': 'B4',
    'Dm': 'A4',
}

# Note to semitone (C4 = 0)
note_to_semitone = {
    'C4': 0, 'C#4': 1, 'D4': 2, 'D#4': 3, 'E4': 4, 'F4': 5, 'F#4': 6,
    'G4': 7, 'G#4': 8, 'A4': 9, 'A#4': 10, 'B4': 11,
    'C5': 12, 'C#5': 13, 'D5': 14, 'D#5': 15, 'E5': 16, 'F5': 17
}

semitone_to_note = {v: k for k, v in note_to_semitone.items()}

def transpose_note(note, semitones):
    """Transpose a note up by semitones"""
    if note not in note_to_semitone:
        return note
    new_semitone = note_to_semitone[note] + semitones
    return semitone_to_note.get(new_semitone, note)

# Song analysis (based on chord files)
songs = [
    {'id': 'song1', 'title': 'I Should Have Been a Cowboy', 'key': 'A', 'capo': 0},
    {'id': 'song2', 'title': 'I Love This Bar', 'key': 'D', 'capo': 0},
    {'id': 'song3', 'title': 'How Do You Like Me Now', 'key': 'A', 'capo': 0},
    {'id': 'song4', 'title': 'Chattahoochee', 'key': 'D', 'capo': 4},
    {'id': 'song5', 'title': 'Gone Country', 'key': 'E', 'capo': 0},
    {'id': 'song6', 'title': 'Drive (For Daddy Gene)', 'key': 'D', 'capo': 0},
    {'id': 'song7', 'title': 'Hey Good Lookin', 'key': 'D', 'capo': 0},
    {'id': 'song8', 'title': 'Family Tradition', 'key': 'D', 'capo': 0},
    {'id': 'song9', 'title': 'All My Exes Live in Texas', 'key': 'E', 'capo': 0},
    {'id': 'song10', 'title': 'Diggin\' Up Bones', 'key': 'A', 'capo': 0},
    {'id': 'song11', 'title': 'Boot Scootin\' Boogie', 'key': 'E', 'capo': 0},
    {'id': 'song12', 'title': 'Friends in Low Places', 'key': 'A', 'capo': 0},
    {'id': 'song13', 'title': 'A Country Boy Can Survive', 'key': 'D', 'capo': 0},
    {'id': 'song14', 'title': 'Pickup Man', 'key': 'A', 'capo': 0},
    {'id': 'song15', 'title': 'Travelin\' Soldier', 'key': 'G', 'capo': 2},
    {'id': 'song16', 'title': 'Wide Open Spaces', 'key': 'G', 'capo': 0},
    {'id': 'song17', 'title': 'Cowboy Take Me Away', 'key': 'F/Am', 'capo': 6},  # Aeolian mode
    {'id': 'song18', 'title': 'Ready To Run', 'key': 'D', 'capo': 0},
    {'id': 'song19', 'title': 'Goodbye Earl', 'key': 'Am', 'capo': 0},
    {'id': 'song20', 'title': 'Boys \'Round Here', 'key': 'D', 'capo': 0},
    {'id': 'song21', 'title': 'Man! I Feel Like a Woman!', 'key': 'G', 'capo': 0},
    {'id': 'song22', 'title': 'Any Man of Mine', 'key': 'D', 'capo': 0},
    {'id': 'song23', 'title': 'That Don\'t Impress Me Much', 'key': 'D', 'capo': 0},
    {'id': 'song24', 'title': 'Thank God I\'m a Country Boy', 'key': 'A', 'capo': 0},
    {'id': 'song25', 'title': 'Rocky Mountain High', 'key': 'D', 'capo': 0},
]

max_comfortable = 'G4'
max_semitone = note_to_semitone[max_comfortable]

print("="*80)
print("VOCAL RANGE ANALYSIS - Baritone (Max: G4)")
print("="*80)

vocal_data = []

for song in songs:
    key = song['key'].split('/')[0]  # Handle F/Am -> F
    if '/' in song['key']:  # For modal songs, use the second key
        key = song['key'].split('/')[1]

    capo = song['capo']

    # Get typical high note for this key
    typical_high = key_high_notes.get(key, 'G4')

    # Transpose up by capo amount
    actual_high = transpose_note(typical_high, capo)
    actual_high_semitone = note_to_semitone.get(actual_high, 7)

    # Determine comfort level
    diff = actual_high_semitone - max_semitone
    if diff <= 0:
        comfort = 'PERFECT'
        emoji = '✅'
        suggestion = 'Comfortable in original key'
    elif diff <= 2:
        comfort = 'GOOD'
        emoji = '👍'
        suggestion = 'Slightly challenging but doable'
    elif diff <= 4:
        comfort = 'CHALLENGING'
        emoji = '⚠️'
        suggestion = f'High notes may be difficult, consider capo down {diff} frets'
    else:
        comfort = 'DIFFICULT'
        emoji = '❌'
        suggestion = f'Too high, drop capo {diff} frets or transpose down'

    vocal_data.append({
        'id': song['id'],
        'title': song['title'],
        'comfort': comfort,
        'emoji': emoji,
        'high_note': actual_high,
        'suggestion': suggestion
    })

    print(f"\n{emoji} {song['title']}")
    print(f"   Key: {song['key']} (Capo {capo})")
    print(f"   Highest Note: {actual_high}")
    print(f"   Comfort: {comfort}")
    print(f"   {suggestion}")

# Count by comfort level
perfect = sum(1 for s in vocal_data if s['comfort'] == 'PERFECT')
good = sum(1 for s in vocal_data if s['comfort'] == 'GOOD')
challenging = sum(1 for s in vocal_data if s['comfort'] == 'CHALLENGING')
difficult = sum(1 for s in vocal_data if s['comfort'] == 'DIFFICULT')

print("\n" + "="*80)
print(f"SUMMARY:")
print(f"  ✅ PERFECT (at or below G4): {perfect} songs")
print(f"  👍 GOOD (slightly high): {good} songs")
print(f"  ⚠️  CHALLENGING (moderately high): {challenging} songs")
print(f"  ❌ DIFFICULT (too high): {difficult} songs")
print("="*80)

# Now update index.html to add vocal comfort badges
with open('index.html', 'r') as f:
    html = f.read()

# Add vocal comfort to each song's theory badge
for song_data in vocal_data:
    song_id = song_data['id']

    # Find the song entry in the JavaScript
    pattern = f"id: '{song_id}',"
    if pattern in html:
        # Find the theory field for this song
        song_start = html.find(pattern)
        theory_start = html.find("theory: '", song_start)

        if theory_start != -1:
            theory_end = html.find("'", theory_start + 9)
            current_theory = html[theory_start + 9:theory_end]

            # Add vocal comfort emoji and note to theory
            new_theory = f"{current_theory} | {song_data['emoji']} High: {song_data['high_note']}"

            # Replace the theory field
            html = html[:theory_start + 9] + new_theory + html[theory_end:]

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("\n✅ Updated index.html with vocal range indicators!")
print("\nVocal comfort now shows in theory badge:")
print("  ✅ = Perfect (at or below G4)")
print("  👍 = Good (slightly challenging)")
print("  ⚠️  = Challenging (moderately high)")
print("  ❌ = Difficult (too high)")
