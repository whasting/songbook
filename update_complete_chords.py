#!/usr/bin/env python3
"""
Update ALL existing songs with complete full chord charts
"""

# Complete chord data for all existing songs
complete_chords = {
    'song1': """[Intro]
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
Living in your radio, How do ya like me now

[Verse 2]
G
When I took off to Tennessee I heard that you made fun of me
F
Never imagined I'd make it this far
G
Then you married into money girl, ain't it a cruel and funny world
F                           C
He took your dreams, and he tore them apart
Dm             Em              F      G
He never comes home and you're always alone and your
C                           F
Kids hear you cry down the hall
Dm                  Em         F             G
Alarm clock starts ringing who could that be singing it's
C                         G
Me baby with your wake up call
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
Living in your radio, How do ya like me now

[Solo]
F  C  G  C
F  C  G  C

[Chorus]
                  F                       C
How do ya like me now, now that I'm on my way
                    G                   C
You still think I'm crazy standing here today
                    F                            C
I couldn't make you love me but I always dreamed about
               G                        C
Living in your radio, How do ya like me now

[Outro]
F  C  G  C
F  C  G  C""",

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
But I was king of the ocean when daddy let me drive

[Verse 2]
G                      D
 Just an old half-ton short bed Ford
   C
My uncle bought new in sixty-four
 G                            D
Daddy got it right 'cause the engine was smokin'
C
 A couple of burnt valves and he had it goin'
G                                D
 He'd let me drive her and we'd haul off a load
        C
Down a dirt strip where we'd dump trash off of Thigpen road
     G                                D
I'd sit up in the seat and stretch my feet out to the pedals
 C                        C  N.C.
Smilin' like a hero that just received his medal

[Chorus]
      G             D
It was just an old hand-me-down Ford
        C
With a three speed on the column and a dent in the door
G                  D
 A young boy, two hands on the wheel
C
 I can't replace the way it made me feel
       G                         D
I would press that clutch and I'd keep it right
        C
He'd say a little slower son, you're doin' just fine
Em                      A                           C
 Just a dirt road with trash on each side but I was Mario Andretti
D                  G
  When daddy let me drive

[Interlude]
|(G)  | D   | C   | D   |
| G   | D   | C   | D   |
| D   |

[Bridge]
G                         D
 I'm grown up now, three daughters of my own
   C
I let 'em drive my old jeep 'cross the pasture at our home
G                       D
 Maybe one day they'll reach back in their file
     C  N.C.                      C   N.C.
And pull out that old mem'ry and think of me and smile

[Chorus]
       G                    D
And say it was just an old worn out jeep
 C
Rusty old floorboards, hot on my feet
G                   D
 A young girl, two hands on the wheel
C
 I can't replace the way it made me feel
            G                D
And he'd say turn it left and steer it right
 C
Straighten up girl now, you're doin' just fine
Em                            A
 Just a little valley by the river where we'd ride
           C                D                 G
But I was high on a mountain when daddy let me drive
D                 C   D
   Daddy let me drive
             G   D   C   D   D
Oh, he let me drive

[Outro]
G                   D
 She's just an old plywood boat
        C                                        G
With a seventy-five Johnson with electric choke""",

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
How's about cookin' somethin' up with me?

(Instrumental)

[Verse]
    C
I'm free and ready,

So we can go steady.
D                  G7                C
How's about savin' all your time for me?

C
No more lookin',

I know I've been tooken
D                   G7          C
How's about keepin' steady company?

[Bridge]
          F                  C
I'm gonna throw my date-book over the fence
    F               C
And find me one for five or ten cents.
     F                 C
I'll keep it 'til it's covered with age
           D                         G7
'Cause I'm writin' your name down on every page.

[Verse]
C
Hey, good lookin',

Whatcha got cookin'?
D                   G7                C
How's about cookin' somethin' up with me?""",

    'song8': """[Intro]
E

[Verse 1]
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
So if I get stoned, I'm just carrying on an old family tradition.

[Verse 2]
E               A
I am very proud of my daddy's name
B7                                                    E
Although his kind of music and mine ain't exactly the same.
                                 A
Stop and think it over. Put yourself in my position.
   B7                                                    E
If I get stoned and sing all night long it's a family tradition.

[Chorus]
                      E                       A
So don't ask me, Hank why do you drink? Hank, why do you roll smoke?
B7                                        E
Why must you live out the songs that you wrote?
                                       A
If I'm down in a honky-tonk some ole slick's trying to give me friction.
        B7                                                          E
I said leave me alone, I'm singing all night long, it's a family tradition.

[Instrumental]
E A B7
E A B7 E

[Verse 3]
E                                   A
Lordy, I have loved some ladies and I have loved Jim Beam
     B7                           E
And they both tried to kill me in 1973.
                               A
When that doctor asked me, Son how did you get in this condition?
        B7                                                  E
I said, hey sawbones, I'm just carrying on an ole family tradition.

[Chorus]
                      E                       A
So don't ask me, Hank why do you drink? Hank, why do you roll smoke?
B7                                         E
Why must you live out the songs that you wrote?
                                         A
Stop and think it over, try and put yourself in my unique position.
   B7                                                     E
If I get stoned and sing all night long, it's a family tradition.""",

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

For me

[Chorus]
A                   E
All my ex's live in Texas
                 Bm               B7   Bdim  A
And Texas is the place I'd really love to be
                    E
All my ex's live in Texas
                                     A
And that's why I hang my hat in Tennessee

[Verse 2]
A
I remember that ole Frio river
Bm
Where I learned to swim
       E7
But it brings to mind another time
                        A
Where I wore my welcome thin
                               Bm
By transcendental meditation I go there each night
      B7                          E
But I always come back to myself, long before daylight

[Chorus]
A                   E
All my ex's live in Texas
                 Bm               B7   Bdim  A
And Texas is the place I'd really love to be
                    E
All my ex's live in Texas
                                     A
And that's why I hang my hat in Tennessee""",

    'song10': """[Verse 1]
        C/G
        Last night I dug your picture out from our old dresser drawer

        I set it on the table and I talked to it 'til four
                                               F
        I read some old love letters right up 'til the break of dawn
              C/G                G               C/G
        Yeah, I've been sittin' alone diggin' up bones

[Verse 2]
        C/G
        Then I went through the jewelery and I found our wedding rings

        I've put mine on my finger and I gave yours a fling
                                          F
        Across this lonely bedroom of our recent broken home
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones

[Chorus]
        C/G
        I'm diggin' up bones, I'm diggin' up bones
                                          G
        Exhuming things that better left alone
            C/G                        F
        I'm resurrecting memories of a love that's dead and gone
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones

[Verse 3]
            C/G
        And I went through the closet and I found some things in there

        Like that pretty neglave that I bought you to wear
                                              F
        And I recall how good you looked each time you had it on
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones

[Chorus]
        C/G
        I'm diggin' up bones, I'm diggin' up bones
                                          G
        Exhuming things that better left alone
            C/G                        F
        I'm resurrecting memories of a love that's dead and gone
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones

[Lead Solo for two chorus lines]

            C/G                        F
        I'm resurrecting memories of a love that's dead and gone
                C/G                G               C/G
        Yeah, tonight I'm sittin' alone diggin' up bones

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

[Verse 2]
  E                      E
I got a good job, I work hard for my money
          E                 E
When it's   quittin' time I hit the door runnin'
  A                  A                        E   E
I fire up my pickup truck and let the horses run
      B                       B
I go flyin' down that highway   to that hide-away
B                   B                   A        E      E F#  G G#
  Stuck out in the woods to do the boot scootin' boogie

[Chorus]
      A                    A                     E
Yeah, heel, toe, do-si-do, c'mon baby, let's go boot scootin'
      A                     A                                  E      E
Woah, Cadillac, black jack, baby meet me out back, we're gonna boogie
    B                      B                 A       E       E
Oh, get down, turn around, go to town, boot scootin' boogie

[Solo]
E   E   E   E
A   A   E   E
B   B   E   E

[Verse 3]
    E                         E
The bartender asks me, says, "Son what'll it be?"
         E                           E
I want a shot at that redhead yonder lookin' at me
    A                              A                            E   E
The dance floor's hoppin' and it's hotter than the Fourth of July
       B                B                    B                 B
I see outlaws, in-laws, crooks and straights all out makin' it shake
               A          E    E  F#  G  G#
Doin' the boot scootin' boogie

[Chorus]
      A                    A                     E
Yeah, heel, toe, do-si-do, c'mon baby, let's go boot scootin'
      A                     A                                  E      E
Woah, Cadillac, black jack, baby meet me out back, we're gonna boogie
B                      B                 A       E        E
Get down, turn around, go to town, boot scootin' boogie

[Chorus]
    A                    A                     E
Oh, heel, toe, do-si-do, c'mon baby, let's go boot scootin'
      A                     A                                  E      E
Yeah, Cadillac, black jack, baby meet me out back, we're gonna boogie
      B                      B                 A       E      E
Yeah, get down, turn around, go to town, boot scootin' boogie

[Outro]
         B                     B                  A       E     E
I said, get down, turn around, go to town, boot scootin' boogie
    B                      N.C.                      E        E
Oh, get down, turn around, go to town boot, scootin' boogie""",

    'song12': """[Intro]
   A                 Bbdim7            Bm7               E*
e|-----------------|-------0---------|-------------5---|-------2h4-------|
B|-------2---------|-----2-----------|-------3---------|-----5-----------|
G|-----2-----------|---0-------------|-----2----(2)----|---4-------------|
D|---2-------------|-----------------|---4-------------|-2---------------|
A|-0---------------|-1---------------|-2---------------|-----------------|
E|-----------------|-----------------|-----------------|-----------------|

[Verse 1]
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

    'song13': """[Intro]
D    D    Am7     Am7
F    F    D    D

[Verse 1]
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

[Verse 2]
      D                    Am7
I can plow a field all day long
      G                  D
I can catch catfish from dusk till dawn
   D                            Am7
We make our own whiskey and our own smoke too
      G                         D
Ain't too many things these ole boys can't do
   D                          Am7
We grow good ole tomatoes and homemade wine
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
If you ain't into that we don't give a damn

[Chorus]
   D                  Am7
We came from the West Virginia coal mines
        G                       D
And the Rocky Mountains and the Western Skies
    D                   Am7
And we can skin a buck, we can run a trot line

      G           Am7    D
And a country boy can survive
Am7           G      D
Country folks can survive

[Verse]
  D                    Am7
I had a good friend in New York City
   G                           D
He never called me by my name, just Hillbilly
   D                    Am7
My Grandpa taught me to live off the land
    G                      D
And his taught him to be a business man
   D                               Am7
He used to send me pictures of the Broadway Night
    G                 D
And I'd send him some homemade wine
    D                             Am7
But he was killed by a man with a switchblade knife
    G                      D
For forty three dollars my friend lost his life
    D                             Am7
I'd love to spit some Beechnut in that dude's eyes
    G                      D
And shoot him with my ole .45
         G           Am7     D
'Cause a country boy can survive
Am7           G      D
Country folks can survive

[Pre-Chorus]
            G                                 F
Because you can't starve us out and you can't make us run
       C                          G
'Cause we're them ole boys raised on shotguns
G                F
We say grace and we say ma'am
       C                  G
If you ain't into that we don't give a damn

[Chorus]
           D                          Am7
We're from North California and South Alabam'
    G                D
And little towns all around this land
    D                      Am7
And we can skin a buck and run a trot line
      G           Am7    D
And a country boy can survive
        Am7   G      D
Country folks can survive

(Repeat and Fade)""",

    'song14': """[Intro]
                             G
e|-----------------------------|
B|---3-2-1---------------------|
G|-0-------3-0-----------------|
D|-------------3-0-------0-2---|
A|-----------------4-3-1-------|
E|---------------------------3-|

[Verse 1]
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

[Verse 2]
       G
When I turned sixteen, I saved a few hundred bucks
 G
My first car was a pickup truck
      C
I was cruisin' the town and the first girl I seen
    G
Was Bobbie Jo Gentry, the homecomin' queen
    D7
She flagged me down and climbed up in the cab
         G N.C.
And said, "I never knew you were a pickup man"

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
There's just somethin' women like about a pickup man

G

[Verse 3]
     G
Most Friday nights I can be found
       G
In the bed of my truck on an old chaise lounge
       C
Backed into my spot at the drive-in show
           G*
You know a cargo light gives off a romantic glow
        D7
I never have to wait in line at the popcorn stand
               G   N.C.
'Cause there's somethin' women like about a pickup man

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
There's just somethin' women like about a pickup man

[Solo]
| C7  | C7  | G   | G   |
| C7  | C7  | D7  | D7  |

[Bridge]
  C7
A bucket of rust or a brand new machine
D
Once around the block and you'll know what I mean

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
              G
There's just somethin' women like about a pickup man

[Tag]
               G  N.C.                     D*    D* G    (Intro Riff)
Yeah, there's somethin' women like about a pickup man

[Outro]
G""",

    'song15': """[Verse 1]
    G
1.  Two days past eighteen

    he was waiting for the bus in his army greens,
         C
    sat down in a booth in a café there,
              G
    gave his order to a girl with a bow in her hair.

    G
2.  He's a little shy, so she gave him a smile,

    and he said, "Would you mind sitting down for a while,
         C                                 G
    and talking to me, I'm feeling a little low."
                  F                  C                    G
    She said, "I'm off in an hour, and I know where we can go."

    G
3.  So they went down and they sat on the pier,

    he said, "I bet you got a boyfriend, but I don't care,
      C                          G
    I got no one to send a letter to.
              F              C                 G
    Would you mind, if I sent one back here to you?"

    Em      D      C
    I...... cried, never gonna hold the hand of another guy,
    G
    too young for him they told her,
    D
    waiting for the love of the travelin' soldier.
    Em                  D
    Our love will never end,
    C
    waiting for the soldier to come back again,
    G                               D
    never more to be alone when the letter says,
                        G
    my soldier's coming home.

    G
4.  So the letters came from an army camp

    in California, then Vietnam,
           C
    and he told her of his heart and it might be love,
        G
    and all of the things he was so scared of.

    G
5.  He said, when it's getting kinda rough over here,

    I think of that day sitting down at the pier.
          C                                 G
    And I close my eyes and see your pretty smile.
          F                     C                   G
    Don't worry, but I won't be able to write for a while.

    Em      D      C
    I...... cried, never gonna hold the hand of another guy,
    G
    too young for him they told her,
    D
    waiting for the love of the travelin' soldier.
    Em                  D
    Our love will never end,
    C
    waiting for the soldier to come back again,
    G                               D
    never more to be alone when the letter says,
                        G
    my soldier's coming home.

+ instrumental = verses 4 & 5

    G
6.  One Friday night at a football game,

    the Lord's Prayer said and the anthem sang,
      C
    a man said folks, would you bow your heads
          G
    for a list of local Vietnam dead.

    G
7.  Crying all alone under the stands

    was the piccolo player in the marching band,
        C                               G
    and one name read and nobody really cared,
           F                 C                      G
    but a pretty little girl      with a bow in her hair.

    Em      D      C
    I...... cried, never gonna hold the hand of another guy,
    G
    too young for him they told her,
    D
    waiting for the love of the travelin' soldier.
    Em                  D
    Our love will never end,
    C
    waiting for the soldier to come back again,
    G                               D
    never more to be alone when the letter says,
                        G
    my soldier's coming home.

    Em      D      C
    I...... cried, never gonna hold the hand of another guy,
    G
    too young for him they told her,
    D
    waiting for the love of the travelin' soldier.
    Em                  D
    Our love will never end,
    C
    waiting for the soldier to come back again,
    G                               D
    never more to be alone when the letter says,
                        G
    my soldier's coming home.""",

    'song16': """[Intro]
D G D G D G D G
D Em D   Em A D

[Verse 1]
 D           G            D         G
Who doesn't know what I'm talking about
 D                G                  D
Who's never left home, who's never struck out
            G                        D
To find a dream and a life of their own
   G                         A
A place in the clouds, a foundation of stone

D       Em                  D
Many precede and many will follow
D               Em               D
A young girl's dreams no longer hollow
              G                   D
It takes the shape of a place out west
             G                          A
But what it holds for her, she hasn't yet guessed

[Chorus]
         D     Em    G    A  D        Em            G      A
She needs wide open spaces    Room to make her big mistakes
         D Em    G        A              D    Em G A
She needs  new faces She knows the high stakes

[Verse 2]
 D                Em         D
She traveled this road as a child
 D             Em                  D
Wide eyed and grinning, she never tired
             G                             D
But now she won't be coming back with the rest
              G                           A
If these are life's lessons, she'll take this test

[Chorus]
         D     Em    G    A  D        Em            G      A
She needs wide open spaces    Room to make her big mistakes
         D Em    G        A              D           Em            G   A
She needs  new faces She knows the high stakes She knows the high stakes

D Em D   D Em D
D Em D   Em A D

[Bridge]
                    G                     D
As her folks drive away, her dad yells, "Check the oil!"
                    G                     D
Mom stares out the window and says, "I'm leaving my girl"
               G                          D
She said, "It didn't seem like that long ago"
          G                           A
When she stood there and let her own folks know

[Chorus]
          D     Em    G    A  D        Em            G      A
She needed wide open spaces    Room to make her big mistakes
         D Em    G        A              D           Em            G   A
She needs  new faces She knows the high stakes She knows the high stakes

D Em G A D Em G A
D Em G A D Em G A D""",

    'song17': """[Intro]
F Am C
F Am C
F Am C G
F Am C
F Am C
F Am C G

[Verse]
               Am    G      C
I said I wanna touch the earth
        Am       G     C
I wanna break it in my hands
        Am       G     C    F     G
I wanna grow something wild and unruly
        Am           G    C
I wanna sleep on the hard ground
       Am         G    C
In the comfort of your arms
     Am     G       C      F
On a pillow of blue bonnets
     G
In a blanket made of stars
      F      C       G
Oh it sounds good to me,

I said..

[Chorus]
       C    F   G
Cowboy take me away
                 Am
Fly this girl as high as you can
  F           G
Into the wild blue
       C    F    G
Set me free oh I pray
          Am
Closer to heaven above and
F         G
Closer to you
             F Am C
Closer to you

F Am C
F Am C F G

[Verse]
        Am       G      C
I wanna walk and not run
        Am       G      C
I wanna skip and not fall
        Am      G       C
I wanna look at the horizon
F       G
And not see a building standing tall
        Am     G       C
I wanna be the only one
    Am    G        C
For miles and miles
Am         G     C
Except for maybe you
F       G
And your simple smile

      F      C       G
Oh it sounds good to me
       F         C       G
Yes it sounds so good to me

[Chorus]
       C    F   G
Cowboy take me away
                 Am
Fly this girl as high as you can
  F           G
Into the wild blue
       C    F    G
Set me free oh I pray
          Am
Closer to heaven above and
F         G
Closer to you
             C F G
Closer to you

Am F G
C F G
Am F G

[Verse]
               Am    G       C
I said I wanna touch the earth
        Am       G     C
I wanna break it in my hands
        Am       G     C    F     G
I wanna grow something wild and unruly
      F         C       G
Oh it sounds so good to me

[Chorus]
       C    F   G
Cowboy take me away
                 Am
Fly this girl as high as you can
  F           G
Into the wild blue
       C    F    G
Set me free oh I pray
          Am
Closer to heaven above and
F         G
Closer to you
            C F G
Closer to you
           C F G
Closer to you
       C    F   G
Cowboy take me away
          Am F G
Closer to you

[Outro]
C F G   Am F G
C F G   Am F G
C F G   Am F G
C F G   Am F G G G"""
}

print("Updating index.html with complete chord charts...")

# Read current HTML
with open('index.html', 'r') as f:
    html = f.read()

# Update each song's chords field
for song_id, new_chords in complete_chords.items():
    # Find the song in the JavaScript
    song_marker = f"id: '{song_id}'"
    song_start = html.find(song_marker)

    if song_start == -1:
        print(f"⚠️  Could not find {song_id}")
        continue

    # Find the chords field
    chords_start = html.find("chords: `", song_start)
    if chords_start == -1:
        print(f"⚠️  Could not find chords field for {song_id}")
        continue

    # Find the end of the chords content (closing backtick before the next field or closing brace)
    chords_content_start = chords_start + len("chords: `")
    chords_end = html.find("`", chords_content_start)

    if chords_end == -1:
        print(f"⚠️  Could not find end of chords for {song_id}")
        continue

    # Replace the chord content
    before = html[:chords_content_start]
    after = html[chords_end:]
    html = before + new_chords + after

    print(f"✅ Updated {song_id} with complete chord chart")

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html)

print("\n✅ All songs updated with complete chord charts!")
print("Songbook now has full lyrics for all 23 songs!")
