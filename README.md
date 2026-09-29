# Te Wa – Kiribati Canoe Fishing

A fishing game set in Kiribati for 1 to 4 players. Paddle your outrigger canoe (*te wa*) across the lagoon, drop your line
and bring home the best catch before sunset.

## Game modes
| Mode | Players | How it works |
|---|---|---|
| 1 Player | 1 | Fish for 90 seconds. Your best score is saved. |
| 2 Players | 2 | Two canoes on one screen at the same time. The left half of the screen steers red and the right half steers blue. |
| Pass & Play | 2–4 | Each player gets 60 seconds, then passes the phone. A final table ranks everyone. |

## What's in the lagoon
| | Points |
|---|---|
| *te baneawa* – milkfish, swims in schools (0.8–3 kg) | 2 + 3 per kg |
| *te ati* – skipjack tuna, deep and fast (2–8 kg) | 6 + 3 per kg |
| *te onauti* – flying fish, near the surface and very fast | 10 + |
| plastic rubbish | +3, cleans the lagoon |
| *te on* – sea turtle, protected | −5 if you hook one |
| *te bakoa* – blacktip reef shark | cuts an empty line (you lose a hook) and steals fish you are reeling in |

Bigger fish score more, but they take longer to reel in. That gives sharks more time to steal them.

## Why it suits Kiribati
- **Works offline.** After the first visit, a service worker keeps the game and its fonts on the phone.
- **Small.** One HTML file of about 60 KB. All graphics and sounds are drawn by code, with no images or audio to download.
- **Runs on cheap phones.** Resolution is capped and there are no libraries.
- **Local setting.** Outrigger canoe with a pandanus sail, atolls with coconut palms, *te eitei* (frigatebird), reef and seagrass, and facts about Kiribati after each round.
- **Two languages.** English and te taetae ni Kiribati.
- **Installable.** "Add to Home Screen" makes it open like a normal app.

## Controls
| | Touch | Keyboard (1 player) | Keyboard (2 players) |
|---|---|---|---|
| Move | Drag | ← → or A D | Red: A D · Blue: ← → |
| Drop line | Tap | Space or ↓ | Red: S · Blue: ↓ |
| Pause | Pause button | P or Esc | P or Esc |

## Run it
Put the files on any web host. GitHub Pages works: go to Settings → Pages → Deploy from a branch.
To test locally:
```
python3 -m http.server 8000   # then open http://localhost:8000
```

## Help wanted
The Kiribati text is a best effort and only partly translated. Please send corrections from native speakers. Ko rabwa!
