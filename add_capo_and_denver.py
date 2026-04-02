#!/usr/bin/env python3
"""
Add capo information and 2 John Denver songs
"""

with open('index.html', 'r') as f:
    html = f.read()

# Capo information for existing songs
capo_info = {
    'song1': 'No capo',
    'song2': 'No capo',
    'song3': 'No capo',
    'song4': 'No capo',
    'song5': 'No capo',
    'song6': 'Capo 4th fret',
    'song7': 'No capo',
    'song8': 'No capo',
    'song9': 'No capo',
    'song10': 'No capo',
    'song11': 'No capo',
    'song12': 'No capo',
    'song13': 'No capo',
    'song14': 'No capo',
    'song15': 'Capo 2nd fret',
    'song16': 'Capo 2nd fret',
    'song17': 'Capo 6th fret',
    'song18': 'No capo',
    'song19': 'No capo',
    'song20': 'No capo',
    'song21': 'Capo 1st fret',
    'song22': 'Capo 1st fret',
    'song23': 'Capo 1st fret'
}

# Add capo field to each song's theory badge display
for song_id, capo in capo_info.items():
    # Find the song object
    song_marker = f"id: '{song_id}'"
    song_start = html.find(song_marker)

    if song_start == -1:
        continue

    # Find the theory field
    theory_start = html.find("theory: '", song_start)
    if theory_start == -1:
        continue

    # Find the end of the theory field
    theory_content_start = theory_start + len("theory: '")
    theory_end = html.find("',", theory_content_start)

    if theory_end == -1:
        continue

    # Get current theory content
    current_theory = html[theory_content_start:theory_end]

    # Add capo info if not already there
    if 'Capo' not in current_theory:
        new_theory = current_theory + f' | {capo}'
        html = html[:theory_content_start] + new_theory + html[theory_end:]
        print(f"✅ Added capo info to {song_id}: {capo}")

# New John Denver songs
new_denver_songs = """            },
            {
                id: 'song24',
                title: 'Thank God I\\'m a Country Boy',
                artist: 'John Denver',
                category: 'new',
                key: 'A',
                progression: 'I-IV-V',
                theory: 'Key: A | I-IV-V-vi | No capo',
                analysis: 'Upbeat I-IV-V in A major (A-D-E) with vi (F#m) for color. Uses 2/4 time signature (uncommon in country). The IV chord gets extra beats on line 3 of verses. Simple diatonic harmony perfect for fiddle-driven bluegrass style.',
                chords: `[Verse 1]
      A                            D
Well, life on a farm is kinda laid back
      A                            G        D
Ain't much an old country boy like me can't hack
     A               E           D
It's early to rise, early in the sack
      A         E           A
Thank God I'm a country boy

[Verse 2]
  A                                   D
A simple kind of life never did me no harm
A                       G            D
Raisin' me a family and workin' on a farm
   A             F#m           E            D
My days are all filled with an easy country charm
      A         E           A
Thank God I'm a country boy

[Chorus]
        E                     A
Well, I got me a fine wife, I got me old fiddle
         E                     A
When the sun's comin' up I got cakes on the griddle
    A          F#m           E             D
And life ain't nothin' but a funny, funny riddle
      A         E          A
Thank God I'm a country boy

[Verse 3]
         A                                      D
When the work's all done and the sun's settin' low
  A                         G             D
I pull out my fiddle and I rosin' up the bow
        A         F#m        E             D
But the kids are asleep so I keep it kinda low
      A         E           A
Thank God I'm a country boy

[Verse 4]
A                                    D
I'd play "Sally Goodin" all day if I could
        A                         G            D
But the lord and my wife wouldn't take it very good
     A             F#m        E           D
So I fiddle when I can and I work when I should
      A         E          A
Thank God I'm a country boy

[Chorus]
        E                     A
Well, I got me a fine wife, I got me old fiddle
         E                     A
When the sun's comin' up I got cakes on the griddle
    A           F#m          E7            D
And life ain't nothin' but a funny, funny riddle
      A         E       A
Thank God I'm a country boy

[Solo]
A         D
A      G  D
A  F#m E  D  D
A  E   A
A         D
A      G  D
A  F#m E  D  D
A  E   A

[Verse 5]
        A                                      D
Well, I wouldn't trade my life for diamonds or jewels
  A                     G            D
I never was one of them money hungry fools
    A              F#m           E       D
I'd rather have my fiddle and my farming tools
      A         E       A
Thank God I'm a country boy

[Verse 6]
      A                                 D
Yeah, city folk drivin' in a black limousine
        A                   G             D
A lotta sad people thinkin' that's mighty keen
      A          F#m           E           D
Well, son let me tell you now exactly what I mean
        A         E       A
I thank God I'm a country boy

[Chorus]
        E                     A
Well, I got me a fine wife, I got me old fiddle
         E                     A
When the sun's comin' up I got cakes on the griddle
    A          F#m           E             D
And life ain't nothin' but a funny, funny riddle
      A         E          A
Thank God I'm a country boy

[Solo]
A         D
A      G  D
A  F#m E  D  D
A  E   A
A         D
A      G  D
A  F#m E  D  D
A  E   A

[Verse 7]
         A                                     D
Well, my fiddle was my daddy's till the day he died
       A                              G             D
And he took me by the hand and held me close to his side
          A           F#m              E          D
He said: "Live a good life and play my fiddle with pride
          A            E          A
And thank God you're a country boy

[Verse 8]
         A                                      D
My daddy taught me young how to hunt and how to whittle
   A                                G           D
He taught me how to work and play a tune on the fiddle
   A                F#m             E7          D
He taught me how to love and how to give just a little
      A         E           A
Thank God I'm a country boy

[Chorus]
        E                     A
Well, I got me a fine wife, I got me old fiddle
         E                     A
When the sun's comin' up I got cakes on the griddle
    A          F#m           E            D
And life ain't nothin' but a funny, funny riddle
      A         E            A
Thank God I'm a country boy    Yeehaw!

[Outro]
A         D
A      G  D
A  F#m E  D  D
A  E   A  A`
            },
            {
                id: 'song25',
                title: 'Rocky Mountain High',
                artist: 'John Denver',
                category: 'new',
                key: 'D',
                progression: 'I-ii-IV-V7',
                theory: 'Key: D (Capo 2: E) | I-ii-IV-V7-V | Capo 2nd fret',
                analysis: 'Folk ballad in D major (sounds in E with capo 2). Uses I-ii-IV-V7 (D-Em-G-A7) progression. The ii chord (Em) adds melancholy depth. Incorporates C (bVII) borrowed from mixolydian mode. Rich harmonic palette for storytelling. The chorus features dramatic ascending melody.',
                chords: `Capo 2nd fret (Key of E, played in D)

[Intro]
D  Em  G  2x

A7

[Verse 1]
       D                          Em     C       A
He was born in the summer, of his twenty seventh year;
       D                          Em     G
Coming home to a place he'd never been before
   D
He left yesterday behind him,
          Em         C     A
you might say he was born again
          D                      Em    G
You might say he found a key for every door

        D                                Em       C    A
When he first came to the mountains, his life was far away;
       D                Em   G
On the road and hanging by a song
        D                               Em      C      A
But the string's already broken, and he doesn't really care;
         D                           Em       G     A
It keeps changing fast, and it don't last for long

[Chorus]
        G        A              D
But the Colorado Rocky Mountain high
     G               A           D
I've seen it raining fire in the sky
    G               A            D             G   A  G
The shadow from the starlight is softer than a lul la by
      A        D     Em     G
Rocky Mountain high,    Colorado
      A        D     Em     G     A7
Rocky Mountain high,    Colorado

[Verse 2]
   D                                   Em     C        A
He climbed cathedral mountains, he saw silver clouds below;
       D                    Em      G
he saw everything as far as you can see
         D
And they say that he got crazy once,
       Em       C         A
and he tried to touch the sun;
       D                 Em       C   G
And he lost a friend but kept the memory

       D                            Em      C       A
Now he walks in quiet solitude, the forests and the streams;
        D              Em      G
seeking grace in every step he takes
    D                                  Em      C    A
His sight has turned inside himself to try and understand;
      D           Em         C        G
the serenity of a clear blue mountain lake

[Chorus]
        G        A              D
And the Colorado Rocky Mountain high
     G               A           D
I've seen it raining fire in the sky
G               A             D   G  A  G
talk to God and listen to the casual re ply
      A        D     Em     G
Rocky Mountain high,    Colorado
      A        D     Em    G     A7
Rocky Mountain high,   Colorado

[Verse 3]
        D
Now his life is full of wonder,
        Em          C          A
but his heart still knows some fear;
     D               Em     C     G
of a simple thing he cannot comprehend
         D
Why they try to tear the mountains down,
   Em         C      A
To bring in a couple more;
     D            Em     C       G
more people, more scars upon the land

[Chorus]
        G        A              D
And the Colorado Rocky Mountain high
     G               A           D
I've seen it raining fire in the sky
  G              A                D            G   A  G
I know he'd be a poorer man if he never saw an eag le fly
      A        D
Rocky Mountain high

        G        A              D
And the Colorado Rocky Mountain high
     G               A           D
I've seen it raining fire in the sky
G                  A            D     A      G
Friends around the campfire and every body's high
      A        D     Em     G
Rocky Mountain high,    Colorado
      A        D     Em     G
Rocky Mountain high,    Colorado
      A        D     Em     G
Rocky Mountain high,    Colorado
      A        D     Em     G
Rocky Mountain high,    Colorado . . .`
            }"""

# Find the last song (song23) and add the new songs after it
marker = """                chords: `[Intro]
| Am |

  F  G    Am         F  G  Am
Ow     ah huh yeah yeah

[Verse 1]
Am               F                     C           G
I've known a few guys who thought they were pretty smart
    Am               F     C          G
But you've got being right down to an art
Am                 F                  C        G
You think you're a genius - you drive me up the wall
         Am      F       C           G
You're a regular original, a know-it-all

[Bridge]
D     A       G
Oh-oo-oh, you think you're special
D     A                    G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you're a rocket scientist
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the brain but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
                      Am   F  C  G
That don't impress me much

Am   F  C  G

[Verse 2]
Am             F                 C             G
I never knew a guy who carried a mirror in his pocket
      Am          F     C        G
And a comb up his sleeve-just in case
             Am         F           C            G
And all that extra hold gel in your hair oughtta lock it
Am                  F          C          G
'Cause Heaven forbid it should fall outta place

[Bridge]
D     A       G
Oh-oo-oh, you think you're special
D     A                    G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you're Brad Pitt
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the looks but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
                      Am   F  C  G
That don't impress me much

[Instrumental]
| Am F | G Am | Am F | G Am |
| Am F | G Am | Am F | G Am |
| N.C. |

[Verse 3]
       Am           F                 C         G
You're one of those guys who likes to shine his machine
            Am          F                C          G
You make me take off my shoes before you let me get in
Am        F                   C        G
I can't believe you kiss your car good night
Am         F         C            G
C'mon baby tell me - you must be jokin', right!

[Bridge]
D     A       G
Oh-oo-oh, you think you're something special
D     A       G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you've got a car
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the moves but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
           F          C   G   Am
That don't impress me much
       F         C             G           Am
You think you're cool but have you got the touch
F            C             G            Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm on the long, cold, lonely night

[Outro]
                      Am F G       Am F G Am
That don't impress me much!    Ah uhu yeah.
F   G                                       Am   F G
Okay so what do you think you're Elvis or something?
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am
That don't impress me much!`
            }"""

replacement = """                chords: `[Intro]
| Am |

  F  G    Am         F  G  Am
Ow     ah huh yeah yeah

[Verse 1]
Am               F                     C           G
I've known a few guys who thought they were pretty smart
    Am               F     C          G
But you've got being right down to an art
Am                 F                  C        G
You think you're a genius - you drive me up the wall
         Am      F       C           G
You're a regular original, a know-it-all

[Bridge]
D     A       G
Oh-oo-oh, you think you're special
D     A                    G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you're a rocket scientist
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the brain but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
                      Am   F  C  G
That don't impress me much

Am   F  C  G

[Verse 2]
Am             F                 C             G
I never knew a guy who carried a mirror in his pocket
      Am          F     C        G
And a comb up his sleeve-just in case
             Am         F           C            G
And all that extra hold gel in your hair oughtta lock it
Am                  F          C          G
'Cause Heaven forbid it should fall outta place

[Bridge]
D     A       G
Oh-oo-oh, you think you're special
D     A                    G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you're Brad Pitt
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the looks but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
                      Am   F  C  G
That don't impress me much

[Instrumental]
| Am F | G Am | Am F | G Am |
| Am F | G Am | Am F | G Am |
| N.C. |

[Verse 3]
       Am           F                 C         G
You're one of those guys who likes to shine his machine
            Am          F                C          G
You make me take off my shoes before you let me get in
Am        F                   C        G
I can't believe you kiss your car good night
Am         F         C            G
C'mon baby tell me - you must be jokin', right!

[Bridge]
D     A       G
Oh-oo-oh, you think you're something special
D     A       G
Oh-oo-oh, you think you're something else

[Chorus]
N.C.
Okay, so you've got a car
           F          C   G   Am
That don't impress me much
       F       C                 G        Am
So you got the moves but have you got the touch
F            C             G              Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm in the middle of the night
           F          C   G   Am
That don't impress me much
       F         C             G           Am
You think you're cool but have you got the touch
F            C             G            Am
Don't get me wrong, yeah I think you're alright
    F                  C           G
But that won't keep me warm on the long, cold, lonely night

[Outro]
                      Am F G       Am F G Am
That don't impress me much!    Ah uhu yeah.
F   G                                       Am   F G
Okay so what do you think you're Elvis or something?
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am F G    Am F G Am F G
That don't impress me much!  Oh no!
                      Am
That don't impress me much!`""" + new_denver_songs + """
            }"""

html = html.replace(marker, replacement)

# Update title to show 25 songs
html = html.replace(
    '<title>Spring Frolic V Country Songbook (23 Songs)</title>',
    '<title>Spring Frolic V Country Songbook (25 Songs)</title>'
)
html = html.replace(
    '<p>23 Country Classics for Spring 2026</p>',
    '<p>25 Country Classics for Spring 2026</p>'
)

# Update welcome screen
html = html.replace(
    '<h3>Common Progressions in This Collection (23 Songs):</h3>',
    '<h3>Common Progressions in This Collection (25 Songs):</h3>'
)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("\n✅ Added capo information to all existing songs")
print("\n✅ Added 2 new John Denver songs:")
print("   24. Thank God I'm a Country Boy - Key: A | No capo")
print("   25. Rocky Mountain High - Key: D (Capo 2: plays in E)")
print("\n✅ Updated title to show 25 songs")
print("\nSongbook now has 25 country classics with capo info!")
