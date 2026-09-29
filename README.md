# Te Wa – Kiribati Canoe Fishing 🛶🇰🇮

A small fishing game set in Kiribati. Sail your canoe (*te wa*) across the lagoon, drop your line and catch
*te baneawa* (milkfish), *te ati* (skipjack tuna) and *te onauti* (flying fish) before the sun sets.
Keep away from *te bakoa* (sharks), which cut your line. Hook plastic rubbish to clean the ocean for bonus points.

## Why it suits Kiribati
- **Works offline.** After the first visit, a service worker keeps the game on the phone, so it needs no data.
- **Tiny download.** About 30 KB in total, with no images, libraries or sound files to download.
- **Runs on cheap phones.** Plain HTML5 canvas, and screen resolution is capped to save battery.
- **Two languages.** Te taetae ni Kiribati and English, switched from the menu.
- **Local culture.** Outrigger canoe, atoll with coconut palms, the frigatebird (*te eitei*) from the flag, and facts about Kiribati.
- **Installable.** "Add to Home Screen" makes it open like a normal app.

## Controls
| Action | Phone | Keyboard |
|---|---|---|
| Move canoe | Drag left/right | ← → or A D |
| Drop line | Tap | Space or ↓ |
| Pause | ⏸ button | P or Esc |

## Run it
Put the files on any web host (GitHub Pages works) and open `index.html`. To test locally:
```
python3 -m http.server 8000   # then open http://localhost:8000
```
Opening `index.html` straight from disk also works, but offline caching only turns on when it is served over http(s).

## Help wanted
The Gilbertese text is a best effort. Please send corrections from native speakers. Ko rabwa!
