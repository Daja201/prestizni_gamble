# Prestige Gamble — run on your server

## Requirements
- Python 3 (already installed on most Linux servers/macOS; on Windows get it from python.org)
- Port 6767 open/allowed on the host (see firewall note below)

## Run it

1. Unzip this archive on the server.
2. From inside the unzipped folder, run:

   ```bash
   python3 server.py 6767
   ```

   (passing `6767` is optional since it's already the default — you can
   also just run `python3 server.py`)

3. You'll see:

   ```
   Serving gamble.html on all interfaces, port 6767
     Local:   http://localhost:6767/gamble.html
     Network: http://<your-server-ip>:6767/gamble.html
   ```

4. From any device on the network (or the public internet, if the host is
   publicly reachable and the port is open), open:

   ```
   http://<server-ip>:6767/gamble.html
   ```

   Replace `<server-ip>` with the actual IP address of the machine running
   the server (e.g. `http://203.0.113.10:6767/gamble.html`).

## Important: camera access needs HTTPS (except on localhost)

Browsers only allow camera access (`getUserMedia`, used for hand tracking)
on secure contexts: `https://`, or `http://localhost` / `http://127.0.0.1`.

- If you open the game via `http://<server-ip>:6767/...` from another
  device, most browsers will **block the camera** because that's a plain
  `http://` origin, not `localhost`.
- To use the camera from other devices, you need HTTPS. Easiest options:
  - Put a reverse proxy (nginx/Caddy) in front with a TLS certificate
    (e.g. via Let's Encrypt) and forward to `127.0.0.1:6767`.
  - Or use a tunnel like `ngrok http 6767` / Cloudflare Tunnel, which gives
    you an `https://` URL automatically.
- If you only play on the same machine that's running the server, just use
  `http://localhost:6767/gamble.html` — camera works fine there with no
  extra setup.

## Firewall

If the server has a firewall (ufw, firewalld, cloud security group, etc.),
make sure inbound TCP port 6767 is allowed, e.g.:

```bash
# ufw (Debian/Ubuntu)
sudo ufw allow 6767/tcp

# firewalld (RHEL/CentOS/Fedora)
sudo firewall-cmd --add-port=6767/tcp --permanent
sudo firewall-cmd --reload
```

## Running it in the background (optional)

```bash
nohup python3 server.py 6767 > server.log 2>&1 &
```

or set it up as a systemd service / use `screen`/`tmux` for persistence
across SSH sessions.
