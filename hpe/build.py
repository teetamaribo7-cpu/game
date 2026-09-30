"""Build single-file copies of the HPE app.

  python3 build.py              -> st-louis-hpe-offline.html (open straight from a phone, no internet needed)
  python3 build.py --embed OUT  -> also writes OUT, a version without the <html>/<head>/<body> wrapper for embedding
"""
import base64, re, sys
from pathlib import Path

here = Path(__file__).parent
page = (here / 'index.html').read_text()
for js in ('questions.js', 'notes.js'):
    page = page.replace(f'<script src="{js}"></script>', '<script>\n' + (here / js).read_text() + '\n</script>')
for png in ('crest.png', 'icon-192.png'):
    uri = 'data:image/png;base64,' + base64.b64encode((here / png).read_bytes()).decode()
    page = page.replace(f'src="{png}"', f'src="{uri}"').replace(f'href="{png}"', f'href="{uri}"')
page = re.sub(r'<link rel="manifest"[^>]*>\n', '', page)
page = re.sub(r"if \('serviceWorker'.*\n", '', page)
page = page.replace('<title>HPE Revision</title>', '<title>St Louis HPE Revision</title>')
page = page.replace("t === 'HPE Revision' ? t : t + ' · HPE Revision'", "t === 'HPE Revision' ? 'St Louis HPE Revision' : t + ' · St Louis HPE Revision'")
(here / 'st-louis-hpe-offline.html').write_text(page)

if len(sys.argv) == 3 and sys.argv[1] == '--embed':
    embed = page
    for tag in ('<!doctype html>\n', '<html lang="en">\n', '<head>\n', '</head>\n', '<body>\n', '</body>\n', '</html>\n'):
        embed = embed.replace(tag, '')
    embed = re.sub(r'<meta (charset|name="viewport")[^>]*>\n', '', embed)
    embed = re.sub(r'<link rel="(icon|apple-touch-icon)"[^>]*>\n', '', embed)
    Path(sys.argv[2]).write_text(embed)
