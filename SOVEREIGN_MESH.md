# Sovereign Mesh 2.0: The Rebuilt Agentic Network

## Overview
The **Sovereign Mesh 2.0** is the technical and legal framework for transitioning PAI from a local operating system to a decentralized, revenue-generating node. It fixes the brittle dependencies and legal mismatches of the initial 1.0 plan.

---

## 1. Intelligence: The 1.58-bit Engine (via llama.cpp)
To maintain "Presence" without massive hardware requirements, PAI utilizes **BitNet b1.58** ternary models.
- **Deficit Fix**: Replaced `bitnet.cpp` (brittle C++ build) with **llama.cpp**'s native ternary quantization (`TQ1_0`, `TQ2_0`).
- **Performance**: 1.58-bit models run on consumer CPUs with **6x lower memory** and **4x faster inference** than 8-bit counterparts.
- **Implementation**: The `Nodes` skill manages the local GGUF conversion and execution via `llama-cpp-python`.

## 2. Identity: On-Chain Presence (via Olas & DAO LLC)
PAI must be "seen" by the network to participate in the agentic economy.
- **L2 Registration**: Agent registration occurs on **Gnosis** or **Base** L2 to ensure minting and transaction costs stay below $1.00.
- **Legal Entity**: Every revenue-generating PAI is wrapped in a **Wyoming DAO LLC**.
    - **Why?**: Unlike DUNA (nonprofit), the DAO LLC allows for **unlimited profit distribution** to the human owner while providing limited liability.
- **VAI (Verified Agent Identity)**: The `Protocol` skill manages the minting of the agent NFT on Olas, representing the PAI's public presence.

## 3. Privacy: The Sovereign Handshake (via RISC Zero)
Cross-agent collaboration requires sharing context without exposing the raw `History/` database.
- **ZK-Handshake**: Uses **RISC Zero zkVM** to generate Zero-Knowledge Proofs of intent or knowledge.
- **How it works**:
    1. Agent A requests data from Agent B.
    2. Agent B executes a "Privacy Filter" program inside the RISC Zero zkVM.
    3. Agent B sends Agent A the result *plus a ZK proof* that the result was derived correctly from the history without revealing the rest of the file.
- **Sub-second Proofs**: Optimized for speed, ensuring privacy doesn't hinder real-time collaboration.

## 4. Commerce: Agentic Commerce Protocol (ACP)
The Sovereign Mesh uses **ACP** as the universal language for service negotiation.
- **Bargaining**: The `Bargain` skill negotiates micro-payments for sub-tasks (e.g., "I will pay you 0.05 TAO to summarize this 50-page PDF").
- **Execution**: Payments are handled via the `Wallet` skill on Gnosis/Base, settled instantly through Olas Mechs.

---

## Developer Roadmap (Mesh 2.0)

### Phase 1: Local Quantization
- Update `Nodes` to pull and convert `BitNet-b1.58-2B-4T` into GGUF format.
- Integrate `llama-cpp-python` for high-performance CPU execution.

### Phase 2: L2 Identity
- Implement `Protocol` commands for Gnosis/Base minting.
- Add `DAO_LLC_ARTICLES.md` template for legal self-bootstrapping.

### Phase 3: ZK Bridge
- Integrate RISC Zero guest-programs for basic history audits.
- Connect `bin/pai-omni` to the ZK handshake loop.
