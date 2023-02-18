from lona.static_files import StyleSheet, Script, SORT_ORDER


class PicocssNode:
    STATIC_FILES = [
        StyleSheet(
            name='pico.min.css',
            path='../static/lona-picocss/dist/pico/css/pico.min.css',
            url='/lona-picocss/dist/pico/css/pico.min.css',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        StyleSheet(
            name='lona-picocss.css',
            path='../static/lona-picocss/lona-picocss.css',
            url='/lona-picocss/lona-picocss.css',
            sort_order=SORT_ORDER.LIBRARY,
        ),
        Script(
            name='picocss-widgets.js',
            path='../static/lona-picocss/picocss-widgets.js',
            url='/lona-picocss/picocss-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]
