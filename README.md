# Prestige Gamble — own port, self-signed HTTPS (no conflict with existing Caddy)

This setup runs entirely on port 8443, so it won't touch whatever is
already using 80/443 on your server (e.g. your b1tm4p site).

## 1. DNS

Make sure gamble.daveza.eu has an A record pointing at this server's IP
(same as before — only the port changes, not the domain setup).

## 2. Firewall

Open 8443 instead of 80/443:

```bash
sudo ufw allow 8443/tcp
```

## 3. Run it

```bash
docker compose up -d --build
```

## 4. Open it

```
https://gamble.daveza.eu:8443
```

The certificate is self-signed (generated locally by Caddy, valid for any
hostname), so your browser will show a "connection is not private" /
"not secure" warning the first time. Click through it
("Advanced" -> "Proceed anyway" in Chrome, "Accept the Risk" in Firefox).
After you click through, it IS a real HTTPS connection — camera access
works fully, same as with a trusted cert. You (and anyone else playing)
just needs to accept the warning once per browser.

## If you want a real trusted cert instead (no warning)

That requires Let's Encrypt to verify you own the domain. Since ports
80/443 are taken by your other site's Caddy, the only way to do that
without touching the existing setup is a DNS-01 challenge, which needs
API access to whoever manages your DNS (e.g. Cloudflare). That's more
setup (a Caddy build with a DNS provider plugin + an API token) — let me
know if you want that instead and which DNS provider you use.

The other alternative, giving you a fully trusted cert with no extra
setup, is adding a site block to your EXISTING b1tm4p Caddy container so
it issues the cert for gamble.daveza.eu the normal way over port 443 —
that's the approach from before, just needs your Caddyfile path.
