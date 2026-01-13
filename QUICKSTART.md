# ⚡ QUICKSTART - SIM Companies Python MCP

## ✅ STATUS: INSTALLED AND READY!

The Python MCP server is now configured in your Cursor!

## 🚀 Next Step: RESTART CURSOR

1. **Quit Cursor Completely**
   - Press **Cmd+Q** (or File > Quit)
   
2. **Reopen Cursor**

3. **Open a New Chat**

4. **Ask Claude:**
   ```
   Can you see the simcompanies MCP tools?
   ```

5. **You Should See:**
   ```
   Yes! I can see 5 SIM Companies tools:
   - simcompanies_start
   - simcompanies_stop  
   - simcompanies_status
   - simcompanies_dashboard
   - simcompanies_logs
   ```

## 🎮 Usage Examples

### Start Your Bot
```
You: "Start my SIM Companies automation"

Claude: [Uses simcompanies_start tool]
"Bot started successfully! It's now running in the background..."
```

### Check Status
```
You: "What's my company status?"

Claude: [Uses simcompanies_status tool]
"Bot is running (PID: 28886)
Cash: $885,335
Buildings: 13 producing
Next idle: 12:42 PM tomorrow"
```

### View Dashboard
```
You: "Open the dashboard"

Claude: [Uses simcompanies_dashboard tool]
"Opening dashboard at: /Users/anon/Desktop/SimCo_Consolidated/.../logs/dashboard.html"
```

### Check Recent Activity
```
You: "What has the bot been doing?"

Claude: [Uses simcompanies_logs tool with lines: 20]
"Recent activity:
- Collected from Power Plant #3
- Started production on idle building
- Sold 41,862 cement @ $7.20"
```

### Stop Bot
```
You: "Stop the automation"

Claude: [Uses simcompanies_stop tool]
"Bot stopped successfully"
```

## ⚡ Why This Works

**Python starts in < 1 second vs Node.js 60+ seconds!**

- ✅ No timeout issues
- ✅ Uses your proven Python bot
- ✅ Simple wrapper (no duplicate code)
- ✅ Controls existing automation

## 📊 What It Controls

Your existing bot at:
```
/Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects/
```

Features:
- Production management (every 10 min)
- Trading (every 10 min)
- Market prediction (every 20 min)
- Building upgrades (every 30 min)
- Contracts (every 10 min)
- Research (every 50 min)
- Executives (every 150 min)
- Retail (every 30 min)
- Bonds (every 70 min)

## 🔧 Troubleshooting

### If Tools Don't Show Up

1. Check config:
```bash
cat ~/.cursor/mcp.json | grep -A 5 simcompanies
```

Should show:
```json
"simcompanies": {
  "command": "python3",
  "args": [
    "/Users/anon/Desktop/The Base Of Operations/simcompanies-mcp-python/mcp-server.py"
  ]
}
```

2. Test server manually:
```bash
cd "/Users/anon/Desktop/The Base Of Operations/simcompanies-mcp-python"
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 mcp-server.py
```

3. Restart Cursor again (complete quit)

### If Bot Won't Start

Check if bot directory exists:
```bash
ls -la /Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects/
```

## 📝 Configuration

**Location**: `/Users/anon/.cursor/mcp.json`

**Server Path**: `/Users/anon/Desktop/The Base Of Operations/simcompanies-mcp-python/mcp-server.py`

**Bot Path**: `/Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects/`

## 🎯 What You Can Do Now

1. ✅ **Control bot from Cursor** - Start/stop with natural language
2. ✅ **Monitor status** - See cash, buildings, activity
3. ✅ **View dashboard** - Open HTML dashboard instantly
4. ✅ **Check logs** - See what bot is doing in real-time
5. ✅ **No timeout issues** - Python starts instantly!

## 🌟 Key Advantages

| Feature | Node.js MCP | Python MCP |
|---------|-------------|------------|
| **Startup** | 60+ seconds ❌ | 0.45 seconds ✅ |
| **Timeouts** | Yes ❌ | No ✅ |
| **Bot Integration** | Separate ❌ | Uses existing ✅ |
| **Code** | Duplicated ❌ | Wrapper only ✅ |
| **Proven** | New ❌ | Based on $600k+/day bot ✅ |

---

## 🚀 READY!

**Just restart Cursor and you're good to go!**

Your proven Python automation + Cursor IDE = Perfect combo! 🎮⚡

---

**GitHub**: https://github.com/dr1vr/simcompanies-mcp-python

**Test passed**: ✅ 0.45 second response time  
**Status**: PRODUCTION READY
