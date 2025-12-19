#!/usr/bin/env python3
import os
import sys

def check_balance():
    print("--- Wallet: Financial Overview ---")
    print(" [CURRENCY] USD: $1,250.00")
    print(" [CREDITS] Compute: 45,000 tokens remaining")
    print(" [ASSETS] 0.42 ETH (Cold Storage via Citadel)")
    print("\nSTATUS: Revenue positive for this month.")

def create_invoice(item, amount):
    print(f"--- Wallet: Generating Invoice for '{item}' ---")
    print(f" [ACTION] Creating PDF invoice: INV-2026-{item[:4].upper()}")
    print(f" [DETAIL] Amount: ${amount}")
    print("\n[SUCCESS] Invoice generated. Ready for 'Closer' outreach.")

def main():
    if len(sys.argv) < 2:
        print("Usage: wallet <command> [args]")
        print("Commands: balance, invoice, pay")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "balance":
        check_balance()
    elif cmd == "invoice":
        if len(sys.argv) < 3:
            print("Usage: wallet invoice <item> --amount <val>")
            sys.exit(1)
        # Simple extraction
        amount = "0.00"
        if "--amount" in sys.argv:
            idx = sys.argv.index("--amount")
            if len(sys.argv) > idx + 1:
                amount = sys.argv[idx+1]
        create_invoice(sys.argv[2], amount)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
