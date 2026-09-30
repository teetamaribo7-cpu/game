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

## Coins and Shop
- **Gold coins** float in the lagoon. Touch one with your fishing line to collect it. Most coins are worth 1, and big glowing coins deeper down are worth 5.
- You also earn **+2 coins** for each correct quiz answer and **+5 coins** for each new Fish Book discovery.
- Coins are saved in a wallet on the device and spent in the **Shop**:
  - **Sails:** Pandanus (free), Lagoon (20), Sunset (40), Kiribati flag (60), Golden (100).
  - **Upgrades:** Extra hook, 4 hooks per round (80). Fast reel, reel in 30% faster (120).
- These are game coins only. There is no real money and nothing to buy, so the game stays safe for children.

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

## Run it
Put the files on any web host. GitHub Pages works: go to Settings → Pages → Deploy from a branch.
To test locally:
```
python3 -m http.server 8000   # then open http://localhost:8000
```

## Help wanted
The Kiribati text is a best effort and only partly translated. Please send corrections from native speakers. Ko rabwa!

## HPE Revision app (`hpe/`)
A separate revision app for St Louis High School students in KCSE **Health and Physical Education, Years 10 and 11**. Open `hpe/index.html`.
- **Notes** for all 30 Year 10 and Year 11 syllabus topics, with exam-style questions and model answers.
- **Multiple-choice quizzes**: 250 questions. There are topic quizzes, timed tests, a Quick Quiz, a 40-question Mock Exam, Year 10 and Year 11 mixed quizzes, and My Mistakes.
- **Past papers**: the full KCSE 2024 and 2025 papers with solutions. Students can show the answers one question at a time or all together.
- A search box covers the notes, questions and answers. My Progress shows the best score for each topic.
- **Offline**:
  - When hosted, it installs to the home screen and then works without internet (it uses a service worker).
  - `hpe/st-louis-hpe-offline.html` is a single file with everything built in. Share it by WhatsApp or Bluetooth and open it in Chrome.
- Questions are in `hpe/questions.js` and notes are in `hpe/notes.js`. After editing either, run `python3 hpe/build.py` to rebuild the offline file.
