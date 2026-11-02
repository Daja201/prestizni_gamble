# Prestige Gamble — Docker Compose + automatic HTTPS

This runs two containers:
- `gamble` — the Python static server serving gamble.html on port 6767
  internally (not exposed to the host directly).
- `caddy`  — a reverse proxy that terminates HTTPS for `gamble.daveza.eu`
  and automatically gets/renews a Let's Encrypt certificate.

## Before you start

1. DNS: make sure `gamble.daveza.eu` has an A record pointing at this
   server's public IP (and AAAA if you use IPv6). Caddy needs this to
   issue the certificate.
2. Firewall: open ports 80 and 443 (both are required — 80 for the
   Let's Encrypt HTTP challenge / redirect, 443 for HTTPS).
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
3. If anything else on the host is already using ports 80/443 (another
   nginx, apache, etc.), stop it first or change the `ports:` mapping in
   docker-compose.yml.

## Run it

```bash
docker compose up -d --build
```

Check logs if needed:

```bash
docker compose logs -f caddy
docker compose logs -f gamble
```

Caddy will automatically request the certificate for `gamble.daveza.eu`
the first time it starts (as long as DNS already points here and 80/443
are reachable from the internet). After that, open:

```
https://gamble.daveza.eu
```

Camera access will work since it's served over real HTTPS.

## Updating the game

Replace `gamble.html` with a new version, then:

```bash
docker compose up -d --build
```

## Stopping / removing

```bash
docker compose down          # stop and remove containers, keep certs
docker compose down -v       # also wipe the stored Caddy certs
```

## Changing the domain

Edit `Caddyfile` and replace `gamble.daveza.eu` with your domain, then
`docker compose up -d` again.
