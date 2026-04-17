# Workspace

## Overview

pnpm workspace monorepo using TypeScript, plus a Python Telegram bot.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: SQLite via `node:sqlite` built-in (API server reads `bot/facecoin.db`)
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)

## FaceBot — Telegram Mini App

### Bot structure
```
bot/
├── main.py          — Entry point, webhook/polling, aiohttp health server
├── database.py      — SQLite DB (aiosqlite), all CRUD helpers
├── games.py         — Coin flip, dice, chest game logic
├── keyboards.py     — All inline & reply keyboards
├── handlers/
│   ├── admin.py          — Admin panel
│   ├── battles.py        — Battle create/join/vote/finish flow
│   ├── buy_coins.py      — Coin purchase relay
│   ├── buy_premium.py    — Premium subscription flow
│   ├── games_handler.py  — Mini-game callbacks
│   └── profile.py        — Profile, shop, leaderboard, daily bonus
└── facecoin.db      — SQLite database (auto-created)
```

### Mini App (React + Vite)
Located at `artifacts/facebot/`. Served at `/facebot/` path.

### API Server (Express)
Located at `artifacts/api-server/`. Served at `/api/` path.
Reads SQLite database from `bot/facecoin.db`.

### Features
- **Photo Battles** — 2-6 players, open or private, 5-minute voting timer
- **FaceCoin economy** — starts at 100, earned via battles/games/daily bonus
- **Mini-games** — Coin flip, Dice roll, Chest/loot-box (7% house commission)
- **Shop** — Frames, badges, statuses, boosts purchasable with FaceCoins
- **Profiles** — Stats, achievements, XP/levelling, leaderboard
- **Premium subscriptions** — 👑 badge, 150 FC daily, +30% battle winnings

### Required secrets
- `TELEGRAM_BOT_TOKEN` — from @BotFather on Telegram

### Running

| Workflow | Command |
|----------|---------|
| `FaceBot` | `python -m bot.main` |
| `artifacts/facebot: web` | `pnpm --filter @workspace/facebot run dev` |
| `artifacts/api-server: API Server` | `pnpm --filter @workspace/api-server run dev` |

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
