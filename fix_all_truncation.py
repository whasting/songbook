#!/usr/bin/env python3
"""
Fix all truncated songs and add missing songs to index.html
"""
import re

# Read index.html
with open('index.html', 'r') as f:
    html = f.read()

# Songs that need fixing with their complete content from TXT files
fixes = {
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
      A
And I saw the surprise
        Bbdim7
And the fear in his eyes
     Bm                      Dm7
When I took his glass of champagne
E
I toasted you
            E7
Said honey, we may be through
    E                        E7
But you'll never hear me complain

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
In low places

[Verse 2]
        A
Well, I guess I was wrong
  Bbdim7
I just don't belong
    Bm
But then, I've been there before
     E
Everything's alright
     E7
I'll just say goodnight
         A
And I'll show myself to the door
     A
Hey, I didn't mean
   Bbdim7
To cause a big scene
     Bm                  Dm7
Just give me an hour and then
      E
Well, I'll be as high as that
E7
Ivory tower
E                    E7
  That you're livin' in

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
In low places

[Verse 3]
  A
I guess I was wrong
  Bbdim7
I just don't belong
    Bm
But then, I've been there before
         E
And everything's alright
     E7
I'll just say goodnight
         A
And I'll show myself to the door
A
I didn't mean
   Bbdim7
To cause a big scene
     Bm                      Dm7
Just wait 'til I finish this glass
     E
Then sweet little lady
          E7
I'll head back to the bar
E
And you can
        E7
Kiss my ass!

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
In low places

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

    'song19': """[Intro]
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
Wrapped up in that tarp Earl

[Verse 3]
C                   F
The cops came by to bring Earl in
C
They searched the house
         G
High and low
          C
Then they tipped their hats
          F                        C             G      C
And said "thank you ladies, if you hear from him let us know"
C
Well, the weeks went by and
F
Spring turned to Summer
C                     G
And Summer faded into Fall
       C                  F
And it turns out he was a missing person
    C        G        C
Who nobody missed at all

[Bridge]
       Am
So the girls bought some land
      G
And a roadside stand
F              C
Out on Highway 109
          Am
They sell Tennessee ham
    G
And strawberry jam
         F
And they don't
                  G
Lose any sleep at night 'cause

[Chorus]
            C  F   C
Earl had to die
   G    F
Goodbye Earl
          C
We need a break
F        C             G   F
Let's go out to the lake Earl
             C  F  C
We'll pack a lunch
                     G     F
And stuff you in the trunk Earl
                  C    F    C
Well, is that all right
                     G       F
Good, let's go for a ride
C    F     C    G     F       C
Earl Hey""",

    'song20': """[Intro]
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
Chew tobacco, chew tobacco, chew tobacco, spit

[Bridge]
A             D                       A        D
    Aw heck  (Red red red red red red redneck)

[Verse]
         A                 N.C.
Well the boys 'round here, they're keeping it country

Ain't a damn one know how to do the dougie
 A
(You don't do the dougie?) No, not in Kentucky
          D
But these girls 'round here yep, they still love me
         A
Yea, the girls 'round here, they all deserve a whistle
D
Shakin' that sugar, sweet as Dixie crystal
     A
They like that y'all and southern drawl
    D
And just can't help it cause they just keep fallin'

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
Chew tobacco, chew tobacco, chew tobacco, spit

[Outro]
 A             D                           A         D
(Ooh     let's ride)                      (Ooh let's ride)
    Aw heck        Red red red red red red redneck
                A                      D
               (Ooh              let's ride)
I'm one of them boys 'round here
                        A             D
                       (Ooh     let's ride)
Red red red red red red redneck""",

    'song21': """[Intro]
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

Man! I feel like a woman!

[Verse]
A
The girls need a break

Tonight we're gonna take
                             D  A
The chance to get out on the town

We don't need romance

We only wanna dance
                              D  A
We're gonna let our hair hang down
G
The best thing about being woman
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
         A            F#m7
Yeah, to feel the way I feel

Man! I feel like a woman!

[Solo]
G , D , A

G , D , A , E

G
The best thing about being woman
A
Is the prerogative

To have a little fun

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
         A            F#m7
Yeah, to feel the way I feel

Man! I feel like a woman!

[Outro]
A , G , D  X3

A""",

    'song22': """[Intro]
e|-----------------------------------|
B|-1/3--1---0-1-0--------------------|
G|----------------0-0-----0-2-0-2----|
D|----------------------0----0-------|
A|-----------------------------------|
E|-----------------------------------|

G  D G

[Verse]
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
Any man of mine

[Verse]
     G
Well any man of mine better disagree
       D                           G
When I say another woman's lookin' better than me

And when I cook him dinner and I burn it black
            D                         G
He better say: Mmm, I like it like that

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
               C     G  C
Any man of mine

[Bridge]
C                    D
Let me hear him say: Yeah, yeah, yeah I like that way!
G                               A
  Any man - any man - any maaaan

[Chorus - Key Change to A]
           D                    A
Any man of mine better walk the line
                 E                                A     A7
Better show me a teasin' squeezin' pleasin' kinda time
                 D                    A
I need a man who knows, how the story goes
                G
He's gotta be a heartbeatin' fine treatin'
D                         E
Breathtakin' earthquakin' kind
               A
Any man of mine

[Outro]
A  D A""",

    'song23': """[Intro]
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
That don't impress me much!"""
}

# Fix each truncated song
for song_id, complete_chords in fixes.items():
    song_marker = f"id: '{song_id}'"
    song_start = html.find(song_marker)

    if song_start == -1:
        print(f"⚠️  Could not find {song_id}")
        continue

    # Find chords field
    chords_start = html.find("chords: `", song_start)
    if chords_start == -1:
        print(f"⚠️  Could not find chords field for {song_id}")
        continue

    chords_content_start = chords_start + len("chords: `")
    chords_end = html.find("`", chords_content_start)

    # Replace with complete content
    before = html[:chords_content_start]
    after = html[chords_end:]
    html = before + complete_chords + after

    print(f"✅ Fixed {song_id}")

# Now add the missing John Denver songs (24 and 25)
# Find the end of song23 and add songs 24-25 after it
song23_marker = "id: 'song23'"
song23_end = html.find("}", html.find("chords: `", html.find(song23_marker)))

if song23_end != -1:
    # Add John Denver songs
    denver_songs = """,
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

    before_denver = html[:song23_end + 1]
    after_denver = html[song23_end + 1:]
    html = before_denver + denver_songs + after_denver
    print("✅ Added song24 (Thank God I'm a Country Boy)")
    print("✅ Added song25 (Rocky Mountain High)")

# Write fixed HTML
with open('index.html', 'w') as f:
    f.write(html)

print("\n" + "="*70)
print("✅ TRUNCATION FIX COMPLETE!")
print("="*70)
print("Fixed songs:")
print("  • song12: Friends in Low Places (all 3 verses)")
print("  • song19: Goodbye Earl (complete)")
print("  • song20: Boys 'Round Here (complete)")
print("  • song21: Man! I Feel Like a Woman! (complete)")
print("  • song22: Any Man of Mine (complete)")
print("  • song23: That Don't Impress Me Much (complete)")
print("Added missing songs:")
print("  • song24: Thank God I'm a Country Boy (8 verses complete)")
print("  • song25: Rocky Mountain High (complete)")
print("\nAll 25 songs now have complete, untruncated content!")
