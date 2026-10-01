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

## Coins, market and gear (a fisher's career)
**Earn coins**
- Sell your catch at the **fish market** after every trip. Each fish sells by weight (kg × price per kg), and the market screen shows the maths.
- Touch **gold coins** in the water with your line (worth 1, or 5 for big coins).
- Get **+2 coins** for each correct quiz answer and **+5 coins** for each new Fish Book discovery.

**Market prices** (coins per kg): milkfish 2, skipjack 3, flying fish 8, bonefish 3, giant trevally 2, yellowfin 4, mahi-mahi 3.

**Spend coins in the Shop**
| Gear | Price | What it does |
|---|---|---|
| Hand line | free | lands fish up to 5 kg |
| Bamboo rod | 40 | up to 12 kg |
| Fibreglass rod | 150 | up to 30 kg |
| Big-game reel | 400 | up to 80 kg |
| Paddle canoe | free | Lagoon only |
| Sailing canoe | 120 | faster, reaches the Reef edge |
| Fibreglass boat | 300 | strong enough for the Open ocean (needs a motor) |
| 15 hp outboard | 200 | reaches the Open ocean; fuel 6 coins a trip |
| 40 hp outboard | 450 | much faster; fuel 10 coins a trip |
| Extra hook / Fast reel | 80 / 120 | 4 hooks per round / reel 30% faster |
| Sails | 0–100 | Pandanus, Lagoon, Sunset, Kiribati flag, Golden |

If a fish is heavier than your rod can hold, the line snaps and the fish escapes. You need to save up for better gear.

**Fishing grounds** (chosen before each trip)
- **Lagoon:** milkfish, flying fish, small skipjack, bonefish.
- **Reef edge** (sailing canoe): bonefish and giant trevally up to 35 kg, on a shallow reef.
- **Open ocean** (fibreglass boat + motor, costs fuel): skipjack, yellowfin tuna up to 60 kg, mahi-mahi.

Players learn that **profit = sales − fuel**, and the quiz includes market maths questions.
These are game coins only. There is no real money.

## Learning features (for students and teachers)
- **Fish Book.** The first time a player catches or meets a creature, the game pauses and shows a fact card with an animated picture, its Kiribati name, its English name and three simple facts. Cards collect in the Fish Book on the menu, so children can try to find all 7.
- **Bonus quiz after every round.** 3 questions (4 in 2-player mode, where players take turns). Each correct answer is worth +10 points and shows a short explanation. There is always one maths question built from fishing, plus questions about Kiribati geography and culture, ocean life, protecting the environment, and Kiribati words.
- **Age levels.** *Age 6–9*: adding and subtracting, and easier questions. *Age 10–14*: multiplying, decimals, negative points, and harder science and history questions.
- **Practice quiz.** 5 questions from the Fish Book, with no game needed. Good for a quick class activity.

### Ideas for the classroom
- Use **Pass & Play** on one phone or tablet with groups of 2–4 students.
- Before playing, ask students to predict which creatures they will find. Afterwards, compare Fish Books.
- Use the maths questions as warm-ups, then ask students to write their own fishing word problems.
- Talk about the turtle and plastic cards: why are turtles protected, and what can we do about rubbish?

## Why it suits Kiribati
- **Works offline.** After the first visit, a service worker keeps the game and its fonts on the phone.
- **Small.** One HTML file of about 80 KB. All graphics and sounds are drawn by code, with no images or audio to download.
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

## Install on Windows
1. Open **https://teetamaribo7-cpu.github.io/game/** in **Microsoft Edge** or **Google Chrome**.
2. Edge: click the **App available / Install** icon in the address bar, or go to **⋯ → Apps → Install Te Wa**.
   Chrome: click the **Install** icon in the address bar, or go to **⋮ → Cast, save and share → Install page as app**.
3. Te Wa gets a Start menu entry and a desktop shortcut, opens in its own window and works offline.

## Run it
Put the files on any web host. GitHub Pages works: go to Settings → Pages → Deploy from a branch.
To test locally:
```
python3 -m http.server 8000   # then open http://localhost:8000
```

## Help wanted
The Kiribati text is a best effort and only partly translated. Please send corrections from native speakers. Ko rabwa!
