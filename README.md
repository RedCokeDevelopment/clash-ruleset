## Rule Providers

Add the following to your Clash config:

```yaml
rule-providers:
  cloudflare:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/RedCokeDevelopment/clash-ruleset/master/services/cloudflare.yaml"
    path: ./ruleset/cloudflare.yaml
    interval: 86400

  discord:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/RedCokeDevelopment/clash-ruleset/master/services/discord.yaml"
    path: ./ruleset/discord.yaml
    interval: 86400

  escapefromtarkov:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/RedCokeDevelopment/clash-ruleset/master/services/escapefromtarkov.yaml"
    path: ./ruleset/escapefromtarkov.yaml
    interval: 86400

  battle-eye:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/RedCokeDevelopment/clash-ruleset/master/services/battle_eye.yaml"
    path: ./ruleset/battle_eye.yaml
    interval: 86400

  google:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/RedCokeDevelopment/clash-ruleset/master/services/google.yaml"
    path: ./ruleset/google.yaml
    interval: 86400
```

## Usage in Rules

```yaml
rules:
  - RULE-SET,cloudflare,lowlatency
  - RULE-SET,discord,lowlatency

  # Escape from Tarkov
  - RULE-SET,escapefromtarkov,lowlatency
  - RULE-SET,battle-eye,lowlatency

  # Google
  - RULE-SET,google,lowlatency
  - GEOSITE,google,lowlatency
  - GEOSITE,youtube,generic

  # China mainland traffic
  - GEOSITE,cn,DIRECT
  - GEOIP,CN,DIRECT
  # Default Fallback
  - MATCH,generic
```