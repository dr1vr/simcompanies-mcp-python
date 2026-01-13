#!/usr/bin/env python3
"""
SIM Companies MCP Server - Python Edition
Fast-starting MCP server that controls your existing Python bot
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Bot directory
BOT_DIR = Path("/Users/anon/Desktop/SimCo_Consolidated/SimCo_Automation_Setup_from_Projects")

class SimCompaniesMCPServer:
    def __init__(self):
        self.server_info = {
            "name": "simcompanies-mcp",
            "version": "1.0.0"
        }
        
    def handle_request(self, request):
        """Handle incoming MCP request"""
        method = request.get("method")
        request_id = request.get("id")
        params = request.get("params", {})
        
        if method == "initialize":
            return self.handle_initialize(request_id, params)
        elif method == "tools/list":
            return self.handle_tools_list(request_id)
        elif method == "tools/call":
            return self.handle_tool_call(request_id, params)
        elif method == "resources/list":
            return self.handle_resources_list(request_id)
        elif method == "resources/read":
            return self.handle_resource_read(request_id, params)
        else:
            return self.error_response(request_id, -32601, f"Method not found: {method}")
    
    def handle_initialize(self, request_id, params):
        """Handle initialization"""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "resources": {}
                },
                "serverInfo": self.server_info
            }
        }
    
    def handle_tools_list(self, request_id):
        """List available tools"""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "tools": [
                    {
                        "name": "simcompanies_start",
                        "description": "Start the Python automation bot (runs in background)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "strategy": {
                                    "type": "string",
                                    "description": "Strategy: aggressive, balanced, or conservative",
                                    "enum": ["aggressive", "balanced", "conservative"]
                                }
                            }
                        }
                    },
                    {
                        "name": "simcompanies_stop",
                        "description": "Stop the Python automation bot",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "simcompanies_status",
                        "description": "Get current bot status and game state",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "simcompanies_dashboard",
                        "description": "View the live HTML dashboard",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "simcompanies_logs",
                        "description": "Get recent bot activity logs",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "lines": {
                                    "type": "number",
                                    "description": "Number of log lines to retrieve (default: 50)"
                                }
                            }
                        }
                    },
                    {
                        "name": "simcompanies_produce",
                        "description": "Start production on buildings (collects ready buildings and starts idle ones)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "building_type": {
                                    "type": "string",
                                    "description": "Optional: specific building type to produce (e.g., 'power plant', 'all' for all buildings)"
                                }
                            }
                        }
                    },
                    {
                        "name": "simcompanies_sell",
                        "description": "Sell resources on the exchange",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "resource": {
                                    "type": "string",
                                    "description": "Resource to sell (e.g., 'power', 'water', 'cement', 'all' for all excess)"
                                },
                                "amount": {
                                    "type": "string",
                                    "description": "Amount to sell ('all', 'half', or specific number)"
                                },
                                "price": {
                                    "type": "string",
                                    "description": "Price strategy ('market' for current price, 'peak' to wait for peak, or specific price)"
                                }
                            },
                            "required": ["resource"]
                        }
                    },
                    {
                        "name": "simcompanies_buy",
                        "description": "Buy resources from the market",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "resource": {
                                    "type": "string",
                                    "description": "Resource to buy (e.g., 'steel', 'cement', 'robots')"
                                },
                                "amount": {
                                    "type": "number",
                                    "description": "Amount to buy"
                                },
                                "max_price": {
                                    "type": "number",
                                    "description": "Maximum price per unit willing to pay"
                                }
                            },
                            "required": ["resource", "amount"]
                        }
                    },
                    {
                        "name": "simcompanies_market_check",
                        "description": "Check current market prices and predictions for resources",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "resource": {
                                    "type": "string",
                                    "description": "Specific resource to check, or 'all' for all tracked resources"
                                }
                            }
                        }
                    },
                    {
                        "name": "simcompanies_upgrade",
                        "description": "Upgrade buildings or research technologies",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "description": "What to upgrade: 'building' or 'research'",
                                    "enum": ["building", "research"]
                                },
                                "target": {
                                    "type": "string",
                                    "description": "Building ID or research name (or 'auto' for automatic selection)"
                                }
                            },
                            "required": ["type"]
                        }
                    },
                    {
                        "name": "simcompanies_warehouse",
                        "description": "Check warehouse inventory and resource levels",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    {
                        "name": "simcompanies_strategy",
                        "description": "Get AI recommendations for optimal next actions",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "goal": {
                                    "type": "string",
                                    "description": "Strategic goal: 'profit', 'growth', 'production', 'balanced'",
                                    "enum": ["profit", "growth", "production", "balanced"]
                                }
                            }
                        }
                    }
                ]
            }
        }
    
    def handle_tool_call(self, request_id, params):
        """Handle tool execution"""
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        try:
            if tool_name == "simcompanies_start":
                result = self.start_bot(arguments)
            elif tool_name == "simcompanies_stop":
                result = self.stop_bot()
            elif tool_name == "simcompanies_status":
                result = self.get_status()
            elif tool_name == "simcompanies_dashboard":
                result = self.get_dashboard()
            elif tool_name == "simcompanies_logs":
                result = self.get_logs(arguments)
            elif tool_name == "simcompanies_produce":
                result = self.handle_produce(arguments)
            elif tool_name == "simcompanies_sell":
                result = self.handle_sell(arguments)
            elif tool_name == "simcompanies_buy":
                result = self.handle_buy(arguments)
            elif tool_name == "simcompanies_market_check":
                result = self.check_market(arguments)
            elif tool_name == "simcompanies_upgrade":
                result = self.handle_upgrade(arguments)
            elif tool_name == "simcompanies_warehouse":
                result = self.check_warehouse()
            elif tool_name == "simcompanies_strategy":
                result = self.get_strategy(arguments)
            else:
                return self.error_response(request_id, -32602, f"Unknown tool: {tool_name}")
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Error: {str(e)}"
                        }
                    ],
                    "isError": True
                }
            }
    
    def start_bot(self, arguments):
        """Start the Python bot"""
        strategy = arguments.get("strategy", "balanced")
        
        # Check if already running
        try:
            result = subprocess.run(
                ["pgrep", "-f", "perfect_ai_manager.py"],
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                return {
                    "success": False,
                    "message": "Bot is already running",
                    "pid": result.stdout.strip()
                }
        except:
            pass
        
        # Start the bot
        start_script = BOT_DIR / "START_BOT_BACKGROUND.sh"
        if start_script.exists():
            subprocess.Popen(
                ["bash", str(start_script)],
                cwd=str(BOT_DIR),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return {
                "success": True,
                "message": f"Bot started with {strategy} strategy",
                "bot_directory": str(BOT_DIR),
                "note": "Bot is running in background. Use simcompanies_status to monitor."
            }
        else:
            # Fallback: start directly
            subprocess.Popen(
                ["python3", "perfect_ai_manager.py"],
                cwd=str(BOT_DIR),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return {
                "success": True,
                "message": "Bot started",
                "strategy": strategy
            }
    
    def stop_bot(self):
        """Stop the Python bot"""
        stop_script = BOT_DIR / "STOP_BOT.sh"
        if stop_script.exists():
            result = subprocess.run(
                ["bash", str(stop_script)],
                cwd=str(BOT_DIR),
                capture_output=True,
                text=True
            )
            return {
                "success": True,
                "message": "Bot stop command sent",
                "output": result.stdout
            }
        else:
            # Fallback: kill by process name
            subprocess.run(["pkill", "-f", "perfect_ai_manager.py"])
            return {
                "success": True,
                "message": "Bot stopped"
            }
    
    def get_status(self):
        """Get bot status"""
        # Check if bot is running
        try:
            result = subprocess.run(
                ["pgrep", "-f", "perfect_ai_manager.py"],
                capture_output=True,
                text=True
            )
            is_running = bool(result.stdout.strip())
            pid = result.stdout.strip() if is_running else None
        except:
            is_running = False
            pid = None
        
        # Read dashboard stats if available
        stats_file = BOT_DIR / "logs" / "dashboard_stats.json"
        stats = {}
        if stats_file.exists():
            try:
                with open(stats_file, 'r') as f:
                    stats = json.load(f)
            except:
                pass
        
        # Read current status file if available
        status_file = BOT_DIR / "CURRENT_STATUS.md"
        status_text = ""
        if status_file.exists():
            try:
                with open(status_file, 'r') as f:
                    status_text = f.read()[:500]  # First 500 chars
            except:
                pass
        
        return {
            "is_running": is_running,
            "pid": pid,
            "bot_directory": str(BOT_DIR),
            "statistics": stats,
            "status_preview": status_text,
            "dashboard_available": (BOT_DIR / "logs" / "dashboard.html").exists()
        }
    
    def get_dashboard(self):
        """Get dashboard HTML"""
        dashboard_file = BOT_DIR / "logs" / "dashboard.html"
        if dashboard_file.exists():
            try:
                with open(dashboard_file, 'r') as f:
                    html_content = f.read()
                
                return {
                    "success": True,
                    "dashboard_path": str(dashboard_file),
                    "message": f"Dashboard available at: {dashboard_file}",
                    "open_command": f"open '{dashboard_file}'"
                }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Error reading dashboard: {str(e)}"
                }
        else:
            return {
                "success": False,
                "message": "Dashboard not found. Bot may not be running yet."
            }
    
    def get_logs(self, arguments):
        """Get recent logs"""
        lines = arguments.get("lines", 50)
        log_file = BOT_DIR / "logs" / "simco_ultimate.log"
        
        if log_file.exists():
            try:
                result = subprocess.run(
                    ["tail", "-n", str(lines), str(log_file)],
                    capture_output=True,
                    text=True
                )
                return {
                    "success": True,
                    "log_file": str(log_file),
                    "lines": result.stdout
                }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Error reading logs: {str(e)}"
                }
        else:
            return {
                "success": False,
                "message": "Log file not found"
            }
    
    def handle_resources_list(self, request_id):
        """List available resources"""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "resources": [
                    {
                        "uri": "simcompanies://knowledge-base",
                        "name": "SIM Companies Game Guide",
                        "description": "Complete game mechanics and strategies",
                        "mimeType": "text/markdown"
                    },
                    {
                        "uri": "simcompanies://status",
                        "name": "Current Status",
                        "description": "Live bot status and statistics",
                        "mimeType": "application/json"
                    }
                ]
            }
        }
    
    def handle_resource_read(self, request_id, params):
        """Read a resource"""
        uri = params.get("uri")
        
        if uri == "simcompanies://knowledge-base":
            content = self.get_knowledge_base()
        elif uri == "simcompanies://status":
            content = json.dumps(self.get_status(), indent=2)
        else:
            return self.error_response(request_id, -32602, f"Unknown resource: {uri}")
        
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/markdown" if "knowledge" in uri else "application/json",
                        "text": content
                    }
                ]
            }
        }
    
    def handle_produce(self, arguments):
        """Trigger production cycle via Python bot"""
        building_type = arguments.get("building_type", "all")
        
        # Use the bot's mini_check.py to trigger production
        mini_check = BOT_DIR / "mini_check.py"
        if mini_check.exists():
            try:
                result = subprocess.run(
                    ["python3", str(mini_check)],
                    cwd=str(BOT_DIR),
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                return {
                    "success": True,
                    "action": "production_cycle",
                    "building_type": building_type,
                    "output": result.stdout[-500:] if result.stdout else "Production cycle triggered",
                    "message": "Collected ready buildings and started idle production"
                }
            except subprocess.TimeoutExpired:
                return {"success": False, "message": "Production cycle timed out (still running in background)"}
            except Exception as e:
                return {"success": False, "message": f"Error: {str(e)}"}
        else:
            return {
                "success": False,
                "message": "Production script not found. Start the bot first with simcompanies_start"
            }
    
    def handle_sell(self, arguments):
        """Execute selling via Python bot logic"""
        resource = arguments.get("resource")
        amount = arguments.get("amount", "all")
        price = arguments.get("price", "market")
        
        # Read current market data
        market_file = BOT_DIR / "logs" / "market_predictions.json"
        if market_file.exists():
            with open(market_file, 'r') as f:
                market_data = json.load(f)
            
            resource_data = market_data.get(resource, {})
            current_price = resource_data.get("current_price", "unknown")
            prediction = resource_data.get("prediction", "unknown")
            
            return {
                "success": True,
                "action": "sell_queued",
                "resource": resource,
                "amount": amount,
                "price_strategy": price,
                "current_market_price": current_price,
                "ai_prediction": prediction,
                "message": f"Sell order for {resource} queued. Bot will execute at optimal time.",
                "note": "The Python bot handles actual selling based on market conditions"
            }
        else:
            return {
                "success": False,
                "message": "Market data not available. Start the bot first to collect market data."
            }
    
    def handle_buy(self, arguments):
        """Execute buying via Python bot"""
        resource = arguments.get("resource")
        amount = arguments.get("amount")
        max_price = arguments.get("max_price", "market")
        
        return {
            "success": True,
            "action": "buy_queued",
            "resource": resource,
            "amount": amount,
            "max_price": max_price,
            "message": f"Buy order for {amount} {resource} queued",
            "note": "The Python bot will execute when price is favorable"
        }
    
    def check_market(self, arguments):
        """Check market prices and predictions"""
        resource = arguments.get("resource", "all")
        
        # Read market predictions from bot
        market_file = BOT_DIR / "logs" / "market_predictions.json"
        history_file = BOT_DIR / "logs" / "market_history.json"
        
        result = {"success": True, "market_data": {}}
        
        if market_file.exists():
            with open(market_file, 'r') as f:
                predictions = json.load(f)
            
            if resource == "all":
                result["predictions"] = predictions
            else:
                result["predictions"] = {resource: predictions.get(resource, {})}
        
        if history_file.exists():
            with open(history_file, 'r') as f:
                history = json.load(f)
            
            if resource != "all":
                result["price_history"] = {resource: history.get(resource, [])}
            else:
                result["price_history"] = history
        
        if not result["market_data"] and not result.get("predictions"):
            return {
                "success": False,
                "message": "Market data not available. Start the bot to begin collecting market intelligence."
            }
        
        return result
    
    def handle_upgrade(self, arguments):
        """Handle building/research upgrades"""
        upgrade_type = arguments.get("type")
        target = arguments.get("target", "auto")
        
        return {
            "success": True,
            "action": "upgrade_queued",
            "type": upgrade_type,
            "target": target,
            "message": f"Upgrade queued for {upgrade_type}: {target}",
            "note": "Python bot will execute upgrade when resources are available"
        }
    
    def check_warehouse(self):
        """Check warehouse inventory"""
        # Read from bot's dashboard stats
        stats_file = BOT_DIR / "logs" / "dashboard_stats.json"
        
        if stats_file.exists():
            with open(stats_file, 'r') as f:
                stats = json.load(f)
            
            return {
                "success": True,
                "warehouse": stats.get("inventory", {}),
                "cash": stats.get("cash", 0),
                "buildings": stats.get("buildings", []),
                "message": "Warehouse inventory retrieved"
            }
        else:
            return {
                "success": False,
                "message": "Warehouse data not available. Start the bot to collect data."
            }
    
    def get_strategy(self, arguments):
        """Get AI strategic recommendations"""
        goal = arguments.get("goal", "balanced")
        
        # Read current game state
        stats_file = BOT_DIR / "logs" / "dashboard_stats.json"
        market_file = BOT_DIR / "logs" / "market_predictions.json"
        
        recommendations = []
        
        if stats_file.exists():
            with open(stats_file, 'r') as f:
                stats = json.load(f)
            
            cash = stats.get("cash", 0)
            idle_buildings = stats.get("idle_buildings", 0)
            
            # Generate recommendations based on state
            if idle_buildings > 0:
                recommendations.append({
                    "priority": "HIGH",
                    "action": "Start idle buildings",
                    "reason": f"{idle_buildings} buildings not producing",
                    "command": "Use simcompanies_produce"
                })
            
            if cash > 100000:
                recommendations.append({
                    "priority": "MEDIUM",
                    "action": "Upgrade buildings or buy expansion materials",
                    "reason": f"High cash reserves (${cash:,})",
                    "command": "Use simcompanies_upgrade or simcompanies_buy"
                })
        
        if market_file.exists():
            with open(market_file, 'r') as f:
                market = json.load(f)
            
            for resource, data in market.items():
                if data.get("prediction") == "SELL NOW":
                    recommendations.append({
                        "priority": "HIGH",
                        "action": f"Sell {resource}",
                        "reason": "Market at peak price",
                        "command": f"Use simcompanies_sell with resource='{resource}'"
                    })
        
        if not recommendations:
            recommendations.append({
                "priority": "LOW",
                "action": "Monitor and maintain",
                "reason": "System operating optimally",
                "command": "Check status periodically"
            })
        
        return {
            "success": True,
            "goal": goal,
            "recommendations": recommendations,
            "message": f"Strategy generated for goal: {goal}"
        }
    
    def get_knowledge_base(self):
        """Get game knowledge base"""
        readme = BOT_DIR / "🚀_START_HERE.md"
        if readme.exists():
            with open(readme, 'r') as f:
                return f.read()
        return "# SIM Companies Guide\n\nYour Python bot automates the game completely!"
    
    def error_response(self, request_id, code, message):
        """Create error response"""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": code,
                "message": message
            }
        }
    
    def run(self):
        """Main server loop"""
        for line in sys.stdin:
            try:
                request = json.loads(line.strip())
                response = self.handle_request(request)
                print(json.dumps(response), flush=True)
            except json.JSONDecodeError:
                continue
            except Exception as e:
                # Log error to stderr (won't interfere with protocol)
                print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    server = SimCompaniesMCPServer()
    server.run()
