# HPE Revision – Android app

Wraps the web app in `../hpe` as an installable Android app (APK) using Capacitor.
The generated `android/` project is not committed. The release workflow (`.github/workflows/hpe-release.yml`) builds it fresh each time.

Build locally (needs Node 18+, JDK 17 and the Android SDK):

```
cd android-app
npm install
mkdir -p www && cp ../hpe/{index.html,questions.js,notes.js,manifest.json,sw.js,*.png} www/
npx cap add android
cp -r icons/* android/app/src/main/res/ && rm -rf android/app/src/main/res/mipmap-anydpi-v26
npx cap sync android
cd android && ./gradlew assembleDebug
```
The APK is written to `android/app/build/outputs/apk/debug/app-debug.apk`.
