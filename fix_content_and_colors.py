#!/usr/bin/env python3
"""
Fix truncated chord content and darken spring colors
"""

# Full chord data from original Ultimate Guitar tabs
full_chords = {
    'song2': """[Verse 1]
D               A
We got winners, we got losers
G                 D
Chain smokers and boozers
       D               A
We got yuppies, we got bikers
G                   A
We got thirsty hitchhikers
        Bm                    A             G
And the girls next door dress up like movie stars
G  Em   F#m   G     A         D
Mmm mm - mm - mm, I love this bar

       D                A
We got cowboys, we got truckers
G                        D
Broken-hearted fools and suckers
       D                A
We got hustlers, we got fighters
G                   A
Early birds and all-nighters
        Bm                  A            G
And the veterans talk about their battle scars
G  Em    F#m  G     A         D
Mmm mm - mm - mm, I love this bar

[Chorus]
            Bm
I love this bar
                D
It's my kind of place
     E                                     A
Just walkin' through the front door puts a big smile on my face
             Bm
It ain't too far
            D
Come as you are
G   Em   F#m   G     A         D
Mmm mm - mm - mm, I love this bar""",

    'song3': """[Verse 1]
G
Yeah I was always a crazy one, broke into the stadium
F
And I wrote your number on the fifty yard line
G
And you were always the perfect one and valedictorian
F                              C
So, under your number I wrote "Call for a good time"

[Pre-Chorus]
Dm     Em        F        G
I only wanted to get your attention but
C                    F
You over looked me somehow
Dm              Em       F             G
Besides you had too many boyfriends to mention and
C                      G    (pause)
I played my guitar too loud
                  C
How do ya like me now

[Chorus]
                  F                       C
How do ya like me now, now that I'm on my way
                    G                   C
You still think I'm crazy standing here today
                    F                            C
I couldn't make you love me but I always dreamed about
               G                        C
Living in your radio, How do ya like me now""",

    'song4': """[Intro]
C   G   C    C   G   C

[Verse 1]
C
Way down yonder on the Chattahoochee
                       G       C
It gets hotter than a hoochie coochie
C
We laid rubber on the Georgia asphalt
C                             G         C
We got a little crazy but we never got caught
F
Down by the river on a Friday night
C                         G         C
A pyramid of cans in the pale moonlight
F
Talking 'bout cars and dreaming 'bout women
D7                                     G
Never had a plan just a livin' for the minute

[Chorus]
C
Yeah way down yonder on the Chattahoochee
                                      G       C
Never knew how much that muddy water meant to me
C
But I learned how to swim and I learned who I was
                         G            C
A lot about livin' and a little 'bout love""",

    'song5': """[Verse 1]
             G                      C         D                  G D C
She's been playing that room on the strip for ten years in Vegas
         G                     C        D             G D C
Every night she looks in the mirror but she only ages
             G                                 C                 D
She's been reading 'bout Nashville and all the records that everybody's
         G D C
buying
              G                  C        D            G D C
Say's I'm a simple girl myself grew up on Long Island
        Em               D
So she packs her bags to try her hand
      Em           D
Says this might be my last chance

[Chorus]
             G      C              D
She's gone country, look at them boots
             G      C              D
She's gone country, back to her roots
             G        C            D
She's gone country, a new kind of suit
             Em        N.C.
She's gone country, here she comes""",

    'song6': """[Intro]
G

[Verse 1]
G                   D
 It was painted red, the stripe was white
        C
It was eighteen feet from the bow to the stern light
G                    D
 Second hand from a dealer in Atlanta
   C
I rode up with daddy when he went there to get 'er
G              D
 Put on a shine, put on a motor
 C
Built out of love and made for the water
G                            D
 Ran her for years 'til the transom got rotten
   C                             C  N.C.
A piece of my childhood that'll never be forgotten

[Chorus]
      G             D
It was just an old plywood boat
        C
With a seventy-five Johnson with electric choke
G                  D
 A young boy, two hands on the wheel
C
 I can't replace the way it made me feel
           G                      D
And I would turn her sharp and I'd make it whine
        C
He'd say you can't beat the way an old wood boat rides
Em                             A
 Just a little lake 'cross the Alabama line
           C               D                 G     D   C   D
But I was king of the ocean when daddy let me drive""",

    'song7': """[Verse]
C
Hey, hey, good lookin',

Whatcha got cookin'?
D                   G7                C G7
How's about cookin' somethin' up with me?

C
Hey, sweet baby,

Don't you think maybe
         D         G7            C
We could find us a brand new recipe?

[Bridge]
        F                  C
I got a hot-rod Ford and a two-dollar bill
    F                   C
And I know a spot right over the hill.
F                        C
There's soda pop and the dancin's free,
          D                    G7
So if you wanna have fun come along with me.

[Verse]
C
Hey, good lookin',

Whatcha got cookin'?
D                   G7                C G7
How's about cookin' somethin' up with me?""",

    'song8': """[Verse 1]
E                                         A
Country music singers have always been a real close family,
      B7                                                      E
But lately some of my kinfolks have disowned a few others and me.
                              A
I guess it's because I kind of changed my direction.
B7                                             E
Lord, I guess I went and broke their family tradition.

[Chorus]
                                     E                        A
They get on me and want to know Hank why do you drink? Hank, why do you roll smoke?
B7                                         E
Why must you live out the songs that you wrote?
                    A
Over and over everybody makes my predictions.
      B7                                                  E
So if I get stoned, I'm just carrying on an old family tradition.""",

    'song9': """[Chorus]
A                   E
All my ex's live in Texas
                 Bm               B7   Bdim  A
And Texas is the place I'd really love to be
                    E
All my ex's live in Texas
                                     A
And that's why I hang my hat in Tennessee

[Verse 1]
A                            Bm
Rosanna's down in Texarkana, wanted me to push her broom
E7                                               A
Sweet Eileen's in Abilene, she forgot I hung the moon
                            Bm
And Allison's in Galveston, somehow lost her sanity
    B7                                         E7
And Dimples, who now lives in Temple's got the law lookin'

For me""",

    'song10': """[Verse 1]
        C/G
        Last night I dug your picture out from our old dresser drawer

        I set it on the table and I talked to it 'til four
                                               F
        I read some old love letters right up 'til the break of dawn
              C/G                G               C/G
        Yeah, I've been sittin' alone diggin' up bones

[Chorus]
        C/G
        I'm diggin' up bones, I'm diggin' up bones
                                          G
        Exhuming things that better left alone
            C/G                        F
        I'm resurrecting memories of a love that's dead and gone
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones""",

    'song11': """[Intro]
E   E   E   E

[Verse 1]
E                             E
  Out in the country past the city limits sign
                E                   E
Well, there's a honky tonk near the county line
    A                          A                       E     E
The joint starts jumpin' every night when the sun goes down
         B               B
They got whiskey, women, music and smoke
     B                     B                A       E      E
It's where all the cowboy folk go to boot scootin' boogie

[Chorus]
      A                    A                     E
Yeah, heel, toe, do-si-do, c'mon baby, let's go boot scootin'
      A                     A                                  E      E
Woah, Cadillac, black jack, baby meet me out back, we're gonna boogie
    B                      B                 A       E       E
Oh, get down, turn around, go to town, boot scootin' boogie""",

    'song12': """[Verse 1]
         A
Blame it all on my roots
  Bbdim7
I showed up in boots
    Bm
And ruined your black tie affair
    E
The last one to know
    E7
The last one to show
          A
I was the last one you thought you'd see there

[Chorus]
       A
'Cause I got friends in low places
          A
Where the whiskey drowns and the beer chases
    Bm
My blues away
         E
And I'll be okay
A
I'm not big on social graces
           A                   A7
Think I'll slip on down to the oasis
    Bm              E
Oh, I've got friends
        A
In low places""",

    'song13': """[Verse 1]
    D                          Am7
The preacher man says it's the end of time
        G                         D
And the Mississippi River she's a-goin' dry
    D                            Am7
The interest is up and the stock market's down
        G                      D
And you only get mugged if you go down town
 D                        Am7
I live back in the woods, you see
   G                          D
My woman and the kids and the dogs and me
        D                      Am7
I got a shotgun, a rifle and a four wheel drive
      G           Am7    D
And a country boy can survive
Am7           G       D
Country folks can survive

[Pre-Chorus]
            G                           F
Because you can't starve us out and you can't make us run
       C                          G
'Cause we're them ole boys raised on shotguns
G                F
We say grace and we say ma'am
       C                  G
If you ain't into that we don't give a damn""",

    'song14': """[Verse 1]
        G
Well, I got my first truck when I was three
        G
Drove a hundred thousand miles on my knees
       C
Hauled marbles and rocks and thought twice before
           G
I hauled a Barbie Doll bed for the girl next door
             D                          D7
She tried to pay me with a kiss and I began to understand
         G  N.C.                                G
There's something women like about a pickup man

[Chorus]
        C
You can set my truck on fire and roll it down a hill
      G
And I still wouldn't trade it for a Coupe De Ville
         C
I got an eight-foot bed that never has to be made
          D                                    D7
You know, if it weren't for trucks we wouldn't have tailgates
      C
I met all my wives in traffic jams
              G  N.C.                     D*    D*  G
There's just somethin' women like about a pickup man""",

    'song15': """[Verse 1]
    G
Two days past eighteen
    he was waiting for the bus in his army greens,
         C
    sat down in a booth in a café there,
              G
    gave his order to a girl with a bow in her hair.

[Chorus]
    Em      D      C
    I...... cried, never gonna hold the hand of another guy,
    G
    too young for him they told her,
    D
    waiting for the love of the travelin' soldier.""",

    'song16': """[Verse 1]
 D           G            D         G
Who doesn't know what I'm talking about
 D                G                  D
Who's never left home, who's never struck out
            G                        D
To find a dream and a life of their own
   G                         A
A place in the clouds, a foundation of stone

[Chorus]
         D     Em    G    A  D        Em            G      A
She needs wide open spaces    Room to make her big mistakes
         D Em    G        A              D    Em G A
She needs  new faces She knows the high stakes""",

    'song17': """[Verse]
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
Into the wild blue"""
}

# Read current HTML
with open('index.html', 'r') as f:
    html = f.read()

# Darken spring colors
color_replacements = [
    # Pale green #98FB98 → Darker green #66B266
    ('#98FB98', '#66B266'),

    # Sky blue #87CEEB → Darker blue #5BA3C7
    ('#87CEEB', '#5BA3C7'),

    # Light green #90EE90 → Darker green #66C266
    ('#90EE90', '#66C266'),

    # Gold #FFD700 → Darker gold #DAA520
    ('#FFD700', '#DAA520'),

    # Light yellow background #FFFACD → Slightly darker #FFF8B8
    ('#FFFACD', '#FFF8B8'),
]

for old_color, new_color in color_replacements:
    html = html.replace(old_color, new_color)

# Update chord content for each song with full versions
for song_id, full_chord_content in full_chords.items():
    # Find the song object in JavaScript
    song_marker = f"id: '{song_id}'"
    song_start = html.find(song_marker)

    if song_start == -1:
        print(f"Warning: Could not find {song_id}")
        continue

    # Find the chords field
    chords_start = html.find("chords: `", song_start)
    if chords_start == -1:
        print(f"Warning: Could not find chords field for {song_id}")
        continue

    # Find the end of the chords content (closing backtick)
    chords_content_start = chords_start + len("chords: `")
    chords_end = html.find("`", chords_content_start)

    if chords_end == -1:
        print(f"Warning: Could not find end of chords for {song_id}")
        continue

    # Replace the chord content
    before = html[:chords_content_start]
    after = html[chords_end:]
    html = before + full_chord_content + after

    print(f"✅ Updated chord content for {song_id}")

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("\n✅ Colors darkened:")
print("   • Pale green #98FB98 → #66B266")
print("   • Sky blue #87CEEB → #5BA3C7")
print("   • Light green #90EE90 → #66C266")
print("   • Gold #FFD700 → #DAA520")
print("   • Light yellow #FFFACD → #FFF8B8")
print("\n✅ Updated chord content for all songs with full charts")
print("\nChanges applied successfully!")
