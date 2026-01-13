# SIM Companies MCP Server - Python Edition ⚡

**Ultra-fast MCP server that controls your existing Python bot!**

## Why This Version?

- ✅ **Instant Startup** - Python starts in milliseconds vs Node.js seconds
- ✅ **Uses Your Working Bot** - Controls your proven $600k+/day automation
- ✅ **No Duplicated Code** - Wrapper around existing Python bot
- ✅ **No Timeout Issues** - Fast enough for Cursor's MCP system

## Features

### Tools
1. **`simcompanies_start`** - Start your Python bot in background
2. **`simcompanies_stop`** - Stop the bot
3. **`simcompanies_status`** - Get live status and statistics
4. **`simcompanies_dashboard`** - View HTML dashboard
5. **`simcompanies_logs`** - Get recent activity logs

### Resources
1. **`simcompanies://knowledge-base`** - Your existing START_HERE.md guide
2. **`simcompanies://status`** - Live JSON status feed

## Installation

### 1. Add to Cursor MCP Config

Edit `/Users/anon/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "simcompanies": {
      "command": "python3",
      "args": [
        "/Users/anon/Desktop/The Base Of Operations/simcompanies-mcp-python/mcp-server.py"
      ],
      "env": {}
    }
  }
}
```

### 2. Test It

```bash
cd "/Users/anon/Desktop/The Base Of Operations/simcompanies-mcp-python"

# Test the server
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python3 mcp-server.py
```

**Should respond instantly with server info!**

### 3. Restart Cursor

Quit Cursor (Cmd+Q) and reopen.

## Usage in Cursor

### Start Your Bot
```
You: "Start my SIM Companies automation"

Claude: *uses simcompanies_start tool*
"I've started your Python bot in the background..."
```

### Check Status
```
You: "What's my company status?"

Claude: *uses simcompanies_status tool*
"Your bot is running (PID: 12345). Company has $885,335 cash..."
```

### View Dashboard
```
You: "Show me the dashboard"

Claude: *uses simcompanies_dashboard tool*
"Dashboard available at: [path]. Opening it now..."
```

### View Logs
```
You: "What has the bot been doing?"

Claude: *uses simcompanies_logs tool*
"Recent activity: Collected from 3 buildings, started production..."
```

### Stop Bot
```
You: "Stop the automation"

Claude: *uses simcompanies_stop tool*
"Bot stopped successfully"
```

## How It Works

```
┌─────────────────────┐
│   Cursor + Claude   │
│  (Your commands)    │
└──────────┬──────────┘
           │ MCP Protocol
           │
┌──────────▼──────────┐
│  Python MCP Server  │  ← This file (instant startup!)
│  (mcp-server.py)    │
└──────────┬──────────┘
           │ Shell commands
           │
┌──────────▼──────────┐
│  Your Python Bot    │  ← Existing automation
│  (perfect_ai_manager)│     (already working!)
└─────────────────────┘
```

## Advantages Over Node.js Version

| Feature | Node.js MCP | Python MCP |
|---------|-------------|------------|
| Startup Time | 60+ seconds ❌ | < 1 second ✅ |
| Timeout Issues | Yes ❌ | No ✅ |
| Uses Existing Bot | No ❌ | Yes ✅ |
| Code Duplication | High ❌ | None ✅ |
| Maintenance | Complex ❌ | Simple ✅ |

## Files

- `mcp-server.py` - The MCP server (this controls everything)
- `README.md` - This file

## Troubleshooting

### Server Not Showing in Cursor

1. Check config: `cat ~/.cursor/mcp.json | grep simcompanies`
2. Test server: `echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python3 mcp-server.py`
3. Restart Cursor completely

### Bot Not Starting

Check if bot directory exists:
```bash
ls -la /Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects/
```

### Want to See What's Happening

Check bot logs directly:
```bash
tail -f /Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects/logs/simco_ultimate.log
```

## Benefits

1. **No Timeout** - Python starts instantly, Cursor is happy
2. **Proven Bot** - Uses your working automation (no rewrite needed)
3. **Simple** - Just a thin wrapper, easy to maintain
4. **Reliable** - No Node.js/Puppeteer complexity

---

**Your $600k+/day Python bot + Cursor IDE integration = Perfect! 🚀**
