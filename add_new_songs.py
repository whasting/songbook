#!/usr/bin/env python3
"""
Add 6 new songs to the songbook
"""

with open('index.html', 'r') as f:
    html = f.read()

# New songs data to add
new_songs_js = """            },
            {
                id: 'song18',
                title: 'Ready To Run',
                artist: 'Dixie Chicks',
                category: 'chicks',
                key: 'G',
                progression: 'I-IV-V',
                theory: 'Key: G | I-IV-V-iii',
                analysis: 'Energetic I-IV-V progression in G major with a iii chord (Bm) adding emotional depth. The C/B bass note creates a descending bass line. Uses F-F#-G chromatic movement for dramatic effect.',
                chords: `[Intro]
G  C C/B  D   G  C C/B  G

[Verse 1]
         D
When the train rolls by
             C          G      C  G
I'm gonna be ready this time
         D
When the boy gets that look in his eyes
             C          G      C  G
I'm gonna be ready this time
        D
When my momma says I look good in white
             C          G      C  G
I'm gonna be ready this time      Oh yeah

[Chorus]
Bm                C              D
Ready ready ready ready ready to run
Bm               C               D
All I'm ready to do is have some fun
C               F     F#   G
What's all this talk about love

[Verse 2]
D
I feel the wind blow through my hair
             C           G     C   G
I'm gonna be ready this time
           D
I'll buy a ticket to anywhere
             C          G      C   G
I'm gonna be ready this time
           D
You see it feels like I'm starting to care
                 C          G     C   G
And I'm gonna be ready this time

[Chorus]
Bm                C              D
Ready ready ready ready ready to run
Bm               C               D
All I'm ready to do is have some fun
C               F     F#   G
What's all this talk about love

[Interlude]
G            C C/B D         G    C C/B D
Ready to run         ready to run

[Chorus]
Bm                C              D
Ready ready ready ready ready to run
Bm               C               D
All I'm ready to do is have some fun
C               F     F#   G
What's all this talk about love

[Outro]
D        G   C C/B D D        G   C C/B D
Ready to run         ready to run
         G  C  C/B D           G  C  C/B D
Ready to run         ready to run
    G  C C/B D     G    C C/B D
I'm ready      I'm ready`
            },
            {
                id: 'song19',
                title: 'Goodbye Earl',
                artist: 'Dixie Chicks',
                category: 'chicks',
                key: 'C',
                progression: 'I-IV-V',
                theory: 'Key: C | I-IV-V-vi',
                analysis: 'Classic I-IV-V country progression in C major with vi (Am) for storytelling tension. The narrative structure uses simple chords to let the dark humor story shine. Modal mixture with borrowed chords adds edge.',
                chords: `[Intro]
C  F  C  G  F
C  F  C  G  F

[Verse 1]
C                             F
Mary, Anne and Wanda were the best of friends
C                             G
All through their high school days
F C                   F
  Both members of the 4H Club
     C             G C
Both active in the FFA
C                     F
After graduation Mary Anne went out
 C                       G
lookin' for a bright new world
F C                F
  Wanda looked all around this town
    C       G         C
And all she found was Earl

[Verse 2]
C
Well, it wasn't two weeks
      F
After she got married that
C                     G
Wanda started gettin' abused
           C                F
She put on dark glasses and long sleeved blouses
    C          G       C
And make up to cover a bruise
C                                  F
Well, she finally got the nerve to file for divorce
    C                        G
She let the law take it from there
    C                                F
But Earl walked right through that restraining order
    C              G       C
And put her in intensive care

[Bridge]
     Am                   G
Right away Mary Anne flew in from Atlanta
     F                C
On a red eye midnight flight
         Am
She held Wanda's hand as they
G
Worked out a plan
       F                        G
And it didn't take 'em long to decide

[Chorus]
                 C   F  C
That Earl had to die
    G   F
Goodbye Earl
                 C    F   C
Those black-eyed peas
                         G   F
They tasted all right to me Earl
               C      F   C
You're feelin' weak
              G
Why don't you lay down
    F
And sleep Earl
         C   F   C
Ain't it dark
                   G    F    C  F   C  F
Wrapped up in that tarp Earl`
            },
            {
                id: 'song20',
                title: "Boys 'Round Here",
                artist: 'Blake Shelton ft. Miranda Lambert',
                category: 'new',
                key: 'A',
                progression: 'I-IV',
                theory: 'Key: A | I-IV (two-chord)',
                analysis: 'Modern country-rap hybrid using minimal I-IV progression (A-D). The simplicity allows focus on rhythm and lyrics. This represents the "bro-country" movement mixing country, hip-hop, and rock elements.',
                chords: `[Intro]
N.C.
(Red red red red red red redneck)

A  D   x4

[Verse]
         A
Well the boys 'round here don't listen to The Beatles
    D
Run ole Bocephus through a jukebox needle
     A
At a honky-tonk, where their boots stomp
    D
All night, what? (That's right)
         A
Yea, and what they call work, digging in the dirt
      D
Gotta get it in the ground 'fore the rain come down
       A
To get paid, to get the girl
        D
In your 4 wheel drive (A country boy can survive)

[Chorus]
        A
Yea the boys 'round here
              D
Drinking that ice cold beer
              A
Talkin' 'bout girls, talkin' 'bout trucks
             D
Runnin' them red dirt roads out, kicking up dust
    A
The boys 'round here
             D
Sending up a prayer to the man upstairs
    A
Backwoods legit, don't take no shit
D
Chew tobacco, chew tobacco, chew tobacco, spit`
            },
            {
                id: 'song21',
                title: 'Man! I Feel Like a Woman!',
                artist: 'Shania Twain',
                category: 'new',
                key: 'A',
                progression: 'I-IV-V',
                theory: 'Key: A | I-IV-V-vi',
                analysis: 'Pop-country crossover using I-IV-V-vi (A-D-E-C#m). The verse uses A-D while chorus explodes with E (V). Influenced by rock anthem structure. The F#m7 (vi7) adds sophistication.',
                chords: `[Intro]
"Main Riff" (A,A,A,F#,E,A,A)

              A
Lets go girls, come on

[Verse]
A
I'm going out tonight, I'm feelin' alright
                      D A
Gonna let it all hang out

Wanna make some noise

Really raise my voice
                         D   A
Yeah, I wanna scream and shout

No inhibitions, make no conditions
                   D  A
Get a little outta line

I ain't gonna act politically correct
                         D  A
I only wanna have a good time
G
The best thing about being a woman
A
Is the prerogative

To have a little fun and

[Chorus]
E
Oh, oh, oh go totally crazy

Forget I'm a lady

Men's shirt, short skirts
        C#m
Oh, oh, oh really go wild, yeah
A           E
Doin' it in style

Oh, oh, oh get in the action, feel the attraction

Color my hair

Do what I dare
        C#m
Oh, oh, oh I wanna be free
         A              F#m7
Yeah, to feel the way I feel

Man! I feel like a woman!`
            },
            {
                id: 'song22',
                title: 'Any Man of Mine',
                artist: 'Shania Twain',
                category: 'new',
                key: 'G',
                progression: 'I-IV-V',
                theory: 'Key: G | I-IV-V',
                analysis: 'Classic country I-IV-V in G major (G-C-D). The G7 (I7) and D7 (V7) add bluesy tension. Modulates up a whole step to A for final chorus (dynamic lift). Features walking bass lines typical of 90s country-pop.',
                chords: `[Verse]
G
Any man of mine better be proud of me
D                     G
Even when I'm ugly he still better love me

And I can be late for a date that's fine
       D              G
But he better be on time

Any man of mine'll say it fits just right
     D                           G
When last year's dress is just a little too tight

And anything I do or say better be okay
       D                  G
When I have a bad hair day

[Pre-chorus]
C                      G
And if I change my mind a million times
C                     D
I wanna hear him say: Yeah, yeah, yeah I like that way!

[Chorus]
           C                    G
Any man of mine better walk the line
                 D                                G      G7
Better show me a teasin' squeezin' pleasin' kinda time
                 C                    G
I need a man who knows how the story goes
                F
He's gotta be a heartbeatin' fine treatin'
C                         D
Breathtakin' earthquakin' kind
               G
Any man of mine`
            },
            {
                id: 'song23',
                title: "That Don't Impress Me Much",
                artist: 'Shania Twain',
                category: 'new',
                key: 'Am',
                progression: 'i-VI-III',
                theory: 'Key: Am | i-VI-III-VII (aeolian)',
                analysis: 'Pop-country in A minor using modal progression i-VI-III-VII (Am-F-C-G). This is Aeolian mode borrowed from pop/rock. The minor key gives it attitude. Bridge uses D-A-G (IV-I-bVII in D) for contrast.',
                chords: `[Intro]
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
That don't impress me much`"""

# Find the last song in the array (song17) and insert after it
marker = """                chords: `[Verse]
               Am    G      C
I said I wanna touch the earth
        Am       G     C
I wanna break it in my hands
        Am       G     C    F     G
I wanna grow something wild and unruly

[Chorus]
       C    F   G
Cowboy take me away
                 Am
Fly this girl as high as you can
  F           G
Into the wild blue`
            }"""

replacement = """                chords: `[Verse]
               Am    G      C
I said I wanna touch the earth
        Am       G     C
I wanna break it in my hands
        Am       G     C    F     G
I wanna grow something wild and unruly

[Chorus]
       C    F   G
Cowboy take me away
                 Am
Fly this girl as high as you can
  F           G
Into the wild blue`""" + new_songs_js + """
            }"""

html = html.replace(marker, replacement)

# Update the title and subtitle
html = html.replace(
    '<p>17 Country Classics for Spring 2026</p>',
    '<p>23 Country Classics for Spring 2026</p>'
)
html = html.replace(
    '<title>Spring Frolic V Country Songbook</title>',
    '<title>Spring Frolic V Country Songbook (23 Songs)</title>'
)

# Update README in welcome screen
old_welcome_text = """                    <div class="theory-summary">
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
                    </div>"""

new_welcome_text = """                    <div class="theory-summary">
                        <h3>Common Progressions in This Collection (23 Songs):</h3>

                        <div class="progression-group">
                            <strong>I-IV-V (Classic Country)</strong><br>
                            <small>14 songs use this or variations</small><br>
                            • I Should Have Been a Cowboy<br>
                            • Chattahoochee<br>
                            • Family Tradition<br>
                            • Boot Scootin' Boogie<br>
                            • Any Man of Mine<br>
                            • Ready To Run
                        </div>

                        <div class="progression-group">
                            <strong>I-V-vi-IV (Modern Country/Pop)</strong><br>
                            <small>4 songs use this progression</small><br>
                            • Gone Country<br>
                            • Drive (For Daddy Gene)<br>
                            • I Love This Bar<br>
                            • Man! I Feel Like a Woman!
                        </div>

                        <div class="progression-group">
                            <strong>Modal Mixture (Borrowed Chords)</strong><br>
                            <small>3 songs use chords from parallel minor</small><br>
                            • How Do You Like Me Now (bVII)<br>
                            • A Country Boy Can Survive (v)<br>
                            • Travelin' Soldier (bVII)
                        </div>

                        <div class="progression-group">
                            <strong>Minor Key Songs (Aeolian Mode):</strong><br>
                            <small>2 songs in minor keys</small><br>
                            • That Don't Impress Me Much (Am)<br>
                            • Cowboy Take Me Away (Am)
                        </div>

                        <div class="progression-group">
                            <strong>Keys Used:</strong><br>
                            <small>G major: 9 songs | A major: 5 songs | D major: 4 songs | C major: 3 songs</small><br>
                            • Most songs use guitar-friendly open chord keys<br>
                            • Modern pop-country crossovers (Shania) favor A major
                        </div>
                    </div>"""

html = html.replace(old_welcome_text, new_welcome_text)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("✅ Added 6 new songs to index.html:")
print("   18. Ready To Run - Dixie Chicks")
print("   19. Goodbye Earl - Dixie Chicks")
print("   20. Boys 'Round Here - Blake Shelton ft. Miranda Lambert")
print("   21. Man! I Feel Like a Woman! - Shania Twain")
print("   22. Any Man of Mine - Shania Twain")
print("   23. That Don't Impress Me Much - Shania Twain")
print("\n✅ Updated title to show 23 songs")
print("✅ Updated theory analysis summary")
print("\nSongbook now has 23 country classics!")
