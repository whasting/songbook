# 🎸 90s Country Songbook

A password-protected accordion-style songbook website with 17 classic country songs.

## 🔐 Access

- **Password**: `country2026`
- Change password in `index.html` line (search for `correctPassword`)

## 🎵 How to Use

1. Open `index.html` in any browser
2. Enter password: `country2026`
3. Click any song button to expand and view chords
4. Click again to collapse
5. Only one song opens at a time (auto-closes others)

## 📝 Song List

**Your Original Favorites (10 songs):**
1. I Should Have Been a Cowboy - Toby Keith
2. I Love This Bar - Toby Keith
3. How Do You Like Me Now - Toby Keith
4. Chattahoochee - Alan Jackson
5. Gone Country - Alan Jackson
6. Drive (For Daddy Gene) - Alan Jackson
7. Hey Good Lookin' - Hank Williams
8. Family Tradition - Hank Williams Jr.
9. All My Exes Live in Texas - George Strait
10. Diggin' Up Bones - Randy Travis

**New Additions (4 songs):**
11. Boot Scootin' Boogie - Brooks & Dunn
12. Friends in Low Places - Garth Brooks
13. A Country Boy Can Survive - Hank Williams Jr.
14. Pickup Man - Joe Diffie

**Dixie Chicks (3 songs):**
15. Travelin' Soldier
16. Wide Open Spaces
17. Cowboy Take Me Away

## 🎨 Features

- ✅ Password protected
- ✅ Accordion-style collapsible buttons
- ✅ Mobile responsive
- ✅ Clean, readable chord charts
- ✅ Monospace font for chord alignment
- ✅ Auto-closes other songs when opening new one
- ✅ Smooth animations
- ✅ Easy to print (expand song and print)

## 🌐 Hosting Options

### Option 1: Local Use
Just open `index.html` in your browser

### Option 2: GitHub Pages
```bash
cd ~/Projects/country-songbook
git init
git add .
git commit -m "Initial songbook"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/country-songbook.git
git push -u origin main
```

Then enable GitHub Pages in repository settings.

### Option 3: Simple HTTP Server
```bash
cd ~/Projects/country-songbook
python3 -m http.server 8080
```
Visit: http://localhost:8080

## 🔧 Customization

### Change Colors
Edit the CSS gradient at line 16:
```css
background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);
```

### Change Font Size
Edit line 183:
```css
font-size: 14px;  /* Change to 16px for larger text */
```

### Change Password
Search for `correctPassword` in the JavaScript and change:
```javascript
const correctPassword = 'country2026';  // Change this
```

## 📱 Usage Tips

1. **For Practice**: Keep it open on your phone/tablet while playing
2. **For Printing**: Expand the song you want and print that section
3. **For Sharing**: Send the HTML file + password to friends
4. **For Backup**: Keep copies on multiple devices

## 📂 File Structure

```
country-songbook/
├── index.html              # Main songbook file (accordion style)
├── index.html.backup       # Original template (if needed)
├── populate_songs.py       # Script used to populate songs
└── README.md               # This file
```

## 🎵 Technical Details

- Pure HTML/CSS/JavaScript (no dependencies)
- Accordion interface with smooth transitions
- Password overlay protection
- Gradient country/western theme
- Responsive design (works on all devices)
- Monospace font (Courier New) for proper chord spacing

---

**Note:** This songbook is for personal use only. All chord charts are from public sources (Ultimate Guitar).
