#!/usr/bin/env python3
"""Check the bundled design skill in isolation, without a local design export."""
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'plugins/hsc-design/skills/hsc-design'


def validate(skill):
    import zipfile
    source = skill / 'references/original/260218_STYLEGUIDE_MIKROTYPOGRAPHIE_HSC.docx'
    with zipfile.ZipFile(source) as archive:
        assert archive.testzip() is None
        assert 'word/document.xml' in archive.namelist()
    import xml.etree.ElementTree as ET
    template = skill / 'assets/word/HSC-Word-Vorlage.docx'
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with zipfile.ZipFile(template) as archive:
        assert archive.testzip() is None
        assert not any('comments' in name for name in archive.namelist())
        fonts = [name for name in archive.namelist() if name.startswith('word/fonts/')]
        assert len(fonts) == 4, 'Missing embedded fonts'
        footer = ET.fromstring(archive.read('word/footer1.xml'))
        fields = {field.get('{'+ns['w']+'}instr').strip() for field in footer.findall('.//w:fldSimple', ns)}
        assert {'PAGE', 'NUMPAGES'} <= fields
        body = ET.fromstring(archive.read('word/document.xml'))
        assert body.find('.//w:tbl', ns) is not None
        for name in ('word/document.xml', 'word/footer1.xml'):
            assert 'IBAN' not in archive.read(name).decode()
    system = skill / 'assets/design-system'
    assert len(list((system / 'assets').glob('Montserrat-*.ttf'))) == 6
    for name in ('hsc-logo.png', 'OFL-Montserrat.txt'):
        assert (system / 'assets' / name).is_file(), name
    templates = list((system / 'templates').glob('*.html'))
    assert len(templates) == 5
    for path in skill.rglob('*'):
        if path.suffix not in {'.md', '.html', '.css'}:
            continue
        content = path.read_text()
        if path.suffix == '.md':
            links = re.findall(r'\]\(([^)]+)\)', content)
        else:
            links = re.findall(r'(?:src|href)=["\']([^"\']+)', content)
            links += re.findall(r'url\(["\']?([^\)"\']+)', content)
        for link in links:
            if link.startswith(('https:', 'http:', 'data:', 'mailto:', 'tel:', '#')):
                continue
            target = (path.parent / unquote(link.split('#')[0])).resolve()
            assert target.is_relative_to(skill.resolve()), f'Outside package: {path}: {link}'
            assert target.is_file(), f'Missing file: {path}: {link}'
    for path in templates:
        content = path.read_text()
        assert '[[TEXT_' in content, f'No placeholders: {path}'
        for demo in ('83 %', 'n = 112', 'Strategie 2027', 'Dr.<sup>in</sup> Muster'):
            assert demo not in content, f'Demo content: {path}: {demo}'
    css = '\n'.join(p.read_text() for p in system.glob('*.css'))
    defined = set(re.findall(r'(--[\w-]+)\s*:', css))
    used = set(re.findall(r'var\((--[\w-]+)', css))
    assert not used - defined, f'Undefined tokens: {used - defined}'
    print('Design bundle valid: portable links, 6 fonts, logo, license, 5 templates, CSS tokens.')


if __name__ == '__main__':
    with tempfile.TemporaryDirectory(prefix='hsc-plugin-check-') as directory:
        copied = Path(directory) / 'skill'
        shutil.copytree(SOURCE, copied)
        validate(copied)
