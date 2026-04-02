#!/usr/bin/env python3
"""
Cross-check index.html chord content against saved .txt files
"""
import re
import os

# Mapping of song IDs to their txt files
song_mapping = {
    'song1': 'I_Should_Have_Been_a_Cowboy.txt',
    'song2': 'I_Love_This_Bar.txt',
    'song3': 'How_Do_You_Like_Me_Now.txt',
    'song4': 'Chattahoochee.txt',
    'song5': 'Gone_Country.txt',
    'song6': 'Drive_For_Daddy_Gene.txt',
    'song7': 'Hey_Good_Lookin.txt',
    'song8': 'Family_Tradition.txt',
    'song9': 'All_My_Exes_Live_in_Texas.txt',
    'song10': 'Diggin_Up_Bones.txt',
    'song11': 'Boot_Scootin_Boogie.txt',
    'song12': 'Friends_in_Low_Places.txt',
    'song13': 'A_Country_Boy_Can_Survive.txt',
    'song14': 'Pickup_Man.txt',
    'song15': 'Travelin_Soldier.txt',
    'song16': 'Wide_Open_Spaces.txt',
    'song17': 'Cowboy_Take_Me_Away.txt',
    'song18': 'Ready_To_Run.txt',
    'song19': 'Goodbye_Earl.txt',
    'song20': 'Boys_Round_Here.txt',
    'song21': 'Man_I_Feel_Like_a_Woman.txt',
    'song22': 'Any_Man_of_Mine.txt',
    'song23': 'That_Dont_Impress_Me_Much.txt',
    'song24': 'Thank_God_Im_a_Country_Boy.txt',
    'song25': 'Rocky_Mountain_High.txt'
}

# Read index.html
with open('index.html', 'r') as f:
    html = f.read()

issues_found = []
all_good = []

for song_id, txt_file in song_mapping.items():
    txt_path = f'chord_files/{txt_file}'

    if not os.path.exists(txt_path):
        issues_found.append(f"❌ {song_id}: TXT file missing: {txt_file}")
        continue

    # Read the txt file
    with open(txt_path, 'r') as f:
        txt_content = f.read()

    # Extract just the chord content (after the header lines)
    txt_lines = txt_content.split('\n')
    # Skip the header lines (first 3 lines)
    txt_chords = '\n'.join(txt_lines[3:]).strip()

    # Find the song in HTML
    song_marker = f"id: '{song_id}'"
    song_start = html.find(song_marker)

    if song_start == -1:
        issues_found.append(f"❌ {song_id}: Not found in HTML")
        continue

    # Find the chords field
    chords_start = html.find("chords: `", song_start)
    if chords_start == -1:
        issues_found.append(f"❌ {song_id}: Chords field not found")
        continue

    # Extract chord content
    chords_content_start = chords_start + len("chords: `")
    chords_end = html.find("`", chords_content_start)

    if chords_end == -1:
        issues_found.append(f"❌ {song_id}: Chords end marker not found")
        continue

    html_chords = html[chords_content_start:chords_end].strip()

    # Compare lengths
    txt_length = len(txt_chords)
    html_length = len(html_chords)

    # Count sections (Verse, Chorus, Bridge, Solo, Outro, Intro)
    txt_sections = len(re.findall(r'\[(Verse|Chorus|Bridge|Solo|Outro|Intro)', txt_chords))
    html_sections = len(re.findall(r'\[(Verse|Chorus|Bridge|Solo|Outro|Intro)', html_chords))

    # Check if content matches
    if txt_chords == html_chords:
        all_good.append(f"✅ {song_id}: Perfect match ({txt_sections} sections, {txt_length} chars)")
    elif txt_length > html_length:
        diff = txt_length - html_length
        issues_found.append(f"⚠️  {song_id}: HTML TRUNCATED by {diff} chars! TXT has {txt_sections} sections, HTML has {html_sections}")
    elif html_length > txt_length:
        diff = html_length - txt_length
        issues_found.append(f"⚠️  {song_id}: HTML has {diff} MORE chars than TXT (TXT: {txt_sections} sections, HTML: {html_sections})")
    else:
        issues_found.append(f"⚠️  {song_id}: Same length but content differs (both {txt_sections} sections)")

# Print results
print("="*70)
print("CHORD CONTENT AUDIT - Index.html vs TXT Files")
print("="*70)

if all_good:
    print(f"\n✅ PERFECT MATCHES ({len(all_good)}):")
    for item in all_good:
        print(f"   {item}")

if issues_found:
    print(f"\n⚠️  ISSUES FOUND ({len(issues_found)}):")
    for item in issues_found:
        print(f"   {item}")
else:
    print(f"\n🎉 NO ISSUES! All {len(all_good)} songs perfectly match their TXT files!")

print(f"\n{'='*70}")
print(f"Total songs checked: {len(song_mapping)}")
print(f"Perfect matches: {len(all_good)}")
print(f"Issues: {len(issues_found)}")
print("="*70)
