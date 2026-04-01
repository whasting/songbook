#!/usr/bin/env python3
"""
Update all existing songs with complete chord charts and add 6 new songs
"""
import os

# Create chord files directory
os.makedirs('chord_files', exist_ok=True)

# Complete chord data for all songs
all_songs = {
    'song1': {
        'chords': """[Intro]
| G  D    | C  D    | x4

[Verse 1]
                G     D         C        D          G
I'll bet you've never heard ole Marshall Dillon say
    D               C            D               G
Miss Kitty have you ever thought of running away
  D          C           D        G
Settling down, would you marry me
   D           C                    D             G
If I asked you twice and begged you pretty please
       D          C            D         G
She'd have said yes in a New York minute
     D                 C
They never tied the knot
D                G
His heart wasn't in it
 D              C            D
He just stole a kiss as he rode away
G          D       C           Cadd9
He never hung his hat up at Kitty's place

[Chorus]
                   G      D   C
I should've been a cowboy
D                      G        D    C   D
I should've learned to rope and ride
G          D            C         D         G        D   C
Wearing my six-shooter, riding my pony on a cattle drive
D           G           D     C   D
Stealing a young girl's heart
G         D         C
Just like Gene and Roy
D             G         D
Singing those campfire songs
C      D                G     D  C
Oh, I should've been a cowboy

[Verse 2]
             G          D           C      D
I might have had a side kick with a funny name
         G               D        C          D
Running wild through the hills chasing Jesse James
G      D         C        D
Ending up on the brink of danger
G           D          C      D
Riding shotgun for the Texas Rangers
    G         D          C          D
Go west young man, haven't you been told
    G          D          C         D
California's full of whisky, women and gold
         G         D              C       D
Sleeping out all night beneath the desert stars
   G          D         C            Cadd9
A dream in my eye and a prayer in my heart

[Chorus]
                   G      D   C
I should've been a cowboy
D                      G        D    C   D
I should've learned to rope and ride
G          D            C         D         G        D   C
Wearing my six-shooter, riding my pony on a cattle drive
D           G           D     C   D
Stealing a young girl's heart
G         D         C
Just like Gene and Roy
D             G        D
Singing those campfire songs
C      D                G     D   C   D
Oh, I should've been a cowboy

[Instrumental]
G       D       C       D
G       D       C       Cadd9

[Chorus]
                   G      D   C
I should've been a cowboy
D                      G        D    C   D
I should've learned to rope and ride
       G          D            C         D         G        D   C
I'd be wearing my six-shooter, riding my pony on a cattle drive
D           G           D     C   D
Stealing a young girl's heart
G         D         C
Just like Gene and Roy
D             G        D
Singing those campfire songs
C      D                G     D   C
Oh, I should've been a cowboy

        D                 G     D   C
Yeah, I should've been a cowboy
  D                G   D   C   D
I should've been a cowboy

G   D   C   D   x4""",
        'file': 'I_Should_Have_Been_a_Cowboy.txt'
    },
    'song2': {
        'chords': """[Verse 1]
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
Mmm mm - mm - mm, I love this bar

[Verse 2]
          D                       A
I've seen short skirts, we've got high techs
G                      D
Blue-collared boys and rednecks
       D             A
We got lovers, lotsa lookers
          G                      A
I've even seen dancin' girls and hookers
       Bm                A                 G
And we like to drink our beer from a Mason jar
G   Em   F#m   G     A         D
Mmm mm - mm - mm, I love this bar, yes, I do

[Instrumental Interlude]
Bm  D   Bm   D

[Bridge]
          A
I like my truck
          D
I like my girlfriend
          E
I like to take her out to dinner
         A
I like a movie now and then

[Chorus]
                Bm
But I love this bar
                D
It's my kind of place
     E                                     A
Just trovin' around the dance floor puts a big smile on my face
          Bm
No cover charge
            D
Come as you are
G   Em   F#m   G     A         D
Mmm mm - mm - mm, I love this bar

[Outro]
   Em   F#m   G          A             D    A  D
Mmm mm - mm - mm, I just love this old bar""",
        'file': 'I_Love_This_Bar.txt'
    }
}

# New songs to add
new_songs = [
    {
        'id': 'song18',
        'title': 'Ready To Run',
        'artist': 'Dixie Chicks',
        'category': 'chicks',
        'key': 'G',
        'progression': 'I-IV-V',
        'theory': 'Key: G | I-IV-V-iii',
        'analysis': 'Energetic I-IV-V progression in G major with a iii chord (Bm) adding emotional depth. The C/B bass note creates a descending bass line. Uses F-F#-G chromatic movement for dramatic effect.',
        'chords': """[Intro]
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
I'm ready      I'm ready""",
        'file': 'Ready_To_Run.txt'
    },
    {
        'id': 'song19',
        'title': 'Goodbye Earl',
        'artist': 'Dixie Chicks',
        'category': 'chicks',
        'key': 'C',
        'progression': 'I-IV-V',
        'theory': 'Key: C | I-IV-V-vi',
        'analysis': 'Classic I-IV-V country progression in C major with vi (Am) for storytelling tension. The narrative structure uses simple chords to let the dark humor story shine. Modal mixture with borrowed chords adds edge.',
        'chords': """[Intro]
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
        'file': 'Goodbye_Earl.txt'
    },
    {
        'id': 'song20',
        'title': "Boys 'Round Here",
        'artist': 'Blake Shelton ft. Miranda Lambert',
        'category': 'new',
        'key': 'A',
        'progression': 'I-IV',
        'theory': 'Key: A | I-IV (two-chord)',
        'analysis': 'Modern country-rap hybrid using minimal I-IV progression (A-D). The simplicity allows focus on rhythm and lyrics. This represents the "bro-country" movement mixing country, hip-hop, and rock elements.',
        'chords': """[Intro]
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
        'file': 'Boys_Round_Here.txt'
    },
    {
        'id': 'song21',
        'title': 'Man! I Feel Like a Woman!',
        'artist': 'Shania Twain',
        'category': 'new',
        'key': 'A',
        'progression': 'I-IV-V-vi',
        'theory': 'Key: A | I-IV-V-vi',
        'analysis': 'Pop-country crossover using I-IV-V-vi (A-D-E-C#m). The verse uses A-D while chorus explodes with E (V). Influenced by rock anthem structure. The F#m7 (vi7) adds sophistication.',
        'chords': """[Intro]
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

Oh, oh, oh get in the action feel the attraction

Color my hair

Do what I dare
        C#m
Oh, oh, oh I wanna be free
         A              F#m7
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
        'file': 'Man_I_Feel_Like_a_Woman.txt'
    },
    {
        'id': 'song22',
        'title': 'Any Man of Mine',
        'artist': 'Shania Twain',
        'category': 'new',
        'key': 'G',
        'progression': 'I-IV-V',
        'theory': 'Key: G | I-IV-V-V7',
        'analysis': 'Classic country I-IV-V in G major (G-C-D). The G7 (I7) and D7 (V7) add bluesy tension. Modulates up a whole step to A for final chorus (dynamic lift). Features walking bass lines typical of 90s country-pop.',
        'chords': """[Intro]
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
        'file': 'Any_Man_of_Mine.txt'
    },
    {
        'id': 'song23',
        'title': "That Don't Impress Me Much",
        'artist': 'Shania Twain',
        'category': 'new',
        'key': 'Am',
        'progression': 'i-VI-III-VII',
        'analysis': 'Pop-country in A minor using modal progression i-VI-III-VII (Am-F-C-G). This is Aeolian mode borrowed from pop/rock. The minor key gives it attitude. Bridge uses D-A-G (IV-I-bVII in D) for contrast.',
        'theory': 'Key: Am | i-VI-III-VII (aeolian)',
        'chords': """[Intro]
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
That don't impress me much!""",
        'file': 'That_Dont_Impress_Me_Much.txt'
    }
]

print("📝 Saving chord charts to individual files...")

# Save new songs to files
for song in new_songs:
    filepath = f"chord_files/{song['file']}"
    with open(filepath, 'w') as f:
        f.write(f"{song['title']} - {song['artist']}\n")
        f.write(f"Key: {song['key']} | {song['progression']}\n")
        f.write("="*60 + "\n\n")
        f.write(song['chords'])
    print(f"✅ Saved: {filepath}")

print(f"\n✅ Saved {len(new_songs)} new chord charts to chord_files/")
print("\nNow updating index.html with new songs...")
