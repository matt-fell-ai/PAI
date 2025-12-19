# Wallet Skill - Autonomous Financial Management

| name | description |
| --- | --- |
| wallet | Manages financial assets, invoices, and micro-payments for the PAI. USE WHEN you need to check balances, generate invoices for services rendered (Market), or execute payments. |

## The Key Insight
A self-sufficient agent must be able to transact. **Wallet** provides the financial plumbing for the PAI. It links your revenue from **Alpha/Forge** to your operational costs (compute, external agent hiring).

## Usage

### Check Balance
```bash
pai run Wallet balance
```

### Create Invoice
```bash
pai run Wallet invoice "research_task" "--amount 50.00"
```

### Execute Payment
```bash
pai run Wallet pay "agent_xyz" "--amount 0.01"
```

## How it Works
It manages local encrypted transaction logs. It can interface with external payment APIs or decentralized finance (DeFi) protocols via `Citadel` hardware signatures.

## Strategic Value
- **Autonomous P&L**: Tracks the Profit and Loss of your PAI's activities.
- **Micro-Economy Ready**: Enables your PAI to participate in the high-frequency agentic economy of 2030.
- **Financial Sovereignty**: Keep your business finances independent and automated.
