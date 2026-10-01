// Offline cache: the game works with no internet after the first visit.
const CACHE = 'tewa-v8';
const FILES = ['./', './index.html', './manifest.json', './icon.svg', './icon-192.png', './icon-512.png', './apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Pages: try the network first so updates show up, fall back to the cache when offline.
// Other files (icons, fonts): cache first, and keep anything fetched for offline play.
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const save = res => {
    if (res.ok || res.type === 'opaque') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }
    return res;
  };
  if (e.request.mode === 'navigate' || e.request.destination === 'document' || e.request.url.endsWith('manifest.json')) {
    e.respondWith(fetch(e.request).then(save).catch(() => caches.match(e.request).then(hit => hit || caches.match('./index.html'))));
    return;
  }
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(save)));
});
