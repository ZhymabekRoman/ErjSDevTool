# Google Translate Debug Framework

1. CDP websocket reverse-proxy: mitmproxy --mode reverse:http://localhost:9222 -w +mitmit.rutopa
2. Helper proxy-server: python3 -m ErjSDev-framework
3. Chrome with debugger: chromium --remote-debugging-port=9222  --remote-allow-origins="*" --user-data-dir=/tmp/ch5 --no-first-run --no-default-browser-check --proxy-server="localhost:7030" --js-flags="--jitless"
