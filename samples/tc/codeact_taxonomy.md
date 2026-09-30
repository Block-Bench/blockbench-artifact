# Code Act Taxonomy

## Overview

Code Acts are discrete, security-relevant code operations within a smart contract. Each Code Act represents an atomic unit of code that could plausibly be involved in a security vulnerability.

The term draws inspiration from Speech Act Theory in linguistics, where utterances are classified by their function (assertion, request, promise, etc.). Similarly, Code Acts classify code segments by their security-relevant function.

---

## Why Code Acts?

Standard vulnerability detection metrics (accuracy, precision, recall) measure **what** models detect but not **why** they detect it. Two models might both correctly identify a reentrancy vulnerability:

- **Model A:** "The external call at line 45 occurs before the state update at line 48, allowing recursive calls to drain funds."

- **Model B:** "This contract has a reentrancy vulnerability because it uses an external call."

Both achieve the same accuracy score. But Model A demonstrates **causal understanding** while Model B shows **pattern recognition**.

Code Act taxonomy enables us to measure whether models understand the actual security-relevant operations in code.

---

## Code Act Types

There are **22 Code Act types** that cover the spectrum of operations in smart contracts. Types 1-17 are security-relevant operations, while types 18-22 are structural elements that typically have no direct security impact but are included for complete code coverage.

### 1. EXT_CALL — External Call

**Definition:** Any call to an external contract or address.

**Security Relevance:** Classic trigger for reentrancy; transfers control flow to untrusted code.

**Solidity Patterns:**
```solidity
address.call{value: x}("");
address.delegatecall(data);
IERC20(token).transfer(to, amount);
externalContract.someFunction();
payable(addr).transfer(amount);
```

---

### 2. STATE_MOD — State Modification

**Definition:** Any write to a storage variable.

**Security Relevance:** Order of state modifications relative to external calls determines reentrancy exploitability. Missing state updates cause logic errors.

**Solidity Patterns:**
```solidity
balances[user] = 0;
totalSupply += amount;
owner = newOwner;
mapping[key] = value;
delete mapping[key];
```

---

### 3. ACCESS_CTRL — Access Control Check

**Definition:** Permission or authorization check that restricts function access.

**Security Relevance:** Missing or incorrect access control is a top vulnerability class.

**Solidity Patterns:**
```solidity
require(msg.sender == owner, "Not owner");
require(hasRole(ADMIN_ROLE, msg.sender));
modifier onlyOwner { ... }
if (msg.sender != admin) revert();
```

---

### 4. ARITHMETIC — Arithmetic Operation

**Definition:** Mathematical computation that could overflow, underflow, or produce unexpected results.

**Security Relevance:** Overflow/underflow (pre-0.8.0), precision loss, division by zero, rounding errors.

**Solidity Patterns:**
```solidity
amount * price / PRECISION
balance + deposit
unchecked { counter++; }
a / b  // potential division by zero
(a * b) / c  // potential overflow before division
```

---

### 5. INPUT_VAL — Input Validation

**Definition:** Validation or sanitization of input parameters.

**Security Relevance:** Missing validation enables various attacks; incorrect validation gives false security.

**Solidity Patterns:**
```solidity
require(amount > 0, "Zero amount");
require(to != address(0), "Invalid address");
require(deadline >= block.timestamp, "Expired");
if (amount > maxAllowed) revert();
```

---

### 6. CTRL_FLOW — Control Flow Logic

**Definition:** Conditional logic or loops that affect execution path.

**Security Relevance:** Logic errors, incorrect conditions, loop manipulation.

**Solidity Patterns:**
```solidity
if (balance > threshold) { ... }
for (uint i = 0; i < users.length; i++) { ... }
while (remaining > 0) { ... }
condition ? valueA : valueB
```

---

### 7. FUND_XFER — Fund Transfer

**Definition:** Movement of ETH or tokens.

**Security Relevance:** Direct financial impact, often the target of exploits.

**Solidity Patterns:**
```solidity
payable(recipient).transfer(amount);
IERC20(token).transfer(to, amount);
IERC20(token).transferFrom(from, to, amount);
(bool success,) = to.call{value: amount}("");
```

**Note:** FUND_XFER often overlaps with EXT_CALL — use FUND_XFER when funds are the primary concern.

---

### 8. DELEGATE — Delegate Call

**Definition:** delegatecall that executes external code in current context.

**Security Relevance:** Extremely dangerous — external code can modify all storage.

**Solidity Patterns:**
```solidity
implementation.delegatecall(data);
proxy.delegatecall(abi.encodeWithSignature(...));
```

---

### 9. TIMESTAMP — Timestamp Dependency

**Definition:** Use of block.timestamp or time-based logic.

**Security Relevance:** Miner manipulation (within ~15 second window), deadline bypasses.

**Solidity Patterns:**
```solidity
require(block.timestamp >= startTime);
if (block.timestamp > deadline) revert();
lockTime = block.timestamp + duration;
```

---

### 10. RANDOM — Randomness Source

**Definition:** Attempt to generate random values on-chain.

**Security Relevance:** On-chain randomness is predictable/manipulable.

**Solidity Patterns:**
```solidity
uint(keccak256(abi.encodePacked(block.timestamp, msg.sender)));
block.prevrandao  // post-merge
blockhash(block.number - 1)
```

---

### 11. ORACLE — Oracle Interaction

**Definition:** Query to external price feed or data oracle.

**Security Relevance:** Price manipulation, stale data, oracle failure.

**Solidity Patterns:**
```solidity
oracle.latestAnswer();
priceFeed.getLatestPrice();
pool.observe(...);  // Uniswap TWAP
uint256 price = reserve1 / reserve0;  // spot price
```

---

### 12. REENTRY_GUARD — Reentrancy Protection

**Definition:** Mutex lock or reentrancy guard pattern.

**Security Relevance:** Presence indicates awareness of reentrancy; check if correctly implemented.

**Solidity Patterns:**
```solidity
// OpenZeppelin
modifier nonReentrant { ... }

// Manual
require(!locked, "Reentrant");
locked = true;
...
locked = false;
```

---

### 13. STORAGE_READ — Storage Read

**Definition:** Reading from storage variable.

**Security Relevance:** Usually benign alone, but order relative to STATE_MOD matters.

**Solidity Patterns:**
```solidity
uint balance = balances[msg.sender];
address currentOwner = owner;
bool isActive = statusFlags[id];
```

---

### 14. SIGNATURE — Signature Verification

**Definition:** Cryptographic signature validation operations.

**Security Relevance:** Signature replay, malleability, missing validation, permit exploits.

**Solidity Patterns:**
```solidity
ecrecover(hash, v, r, s)
ECDSA.recover(hash, signature)
permit(owner, spender, value, deadline, v, r, s)
EIP712._hashTypedDataV4(structHash)
```

---

### 15. INITIALIZATION — State Initialization

**Definition:** Initial assignment of critical state variables.

**Security Relevance:** Uninitialized variables, reinitialization attacks, missing init guards.

**Solidity Patterns:**
```solidity
// Constructor initialization
constructor() {
    owner = msg.sender;
    initialized = true;
}

// Initializer pattern (proxies)
function initialize() external {
    require(!initialized, "Already initialized");
    initialized = true;
    owner = msg.sender;
}

// Missing initialization (vulnerability)
bytes32 public acceptedRoot;  // defaults to 0x00
```

---

### 16. COMPUTATION — Hash/Encode Operations

**Definition:** Cryptographic hashing, ABI encoding, and other computational operations that don't involve arithmetic overflow risk.

**Security Relevance:** Generally benign, but relevant for understanding data flow.

**Solidity Patterns:**
```solidity
keccak256(abi.encodePacked(a, b))
abi.encode(param1, param2)
abi.decode(data, (uint256, address))
bytes32 hash = keccak256(_message);
```

**Note:** Distinct from ARITHMETIC which covers overflow-prone operations.

---

### 17. EVENT_EMIT — Event Emission

**Definition:** Emitting events to transaction logs.

**Security Relevance:** None directly. Events don't modify contract state, only write to logs.

**Solidity Patterns:**
```solidity
emit Transfer(from, to, amount);
emit Approval(owner, spender, value);
emit MessageProcessed(hash, success);
```

**Note:** Distinct from EVENT_DEF which is the event declaration.

---

### 18. COMMENT — Documentation

**Definition:** NatSpec comments, inline comments, and documentation blocks.

**Security Relevance:** None directly, but comments may reveal intent or contain misleading information.

**Solidity Patterns:**
```solidity
/// @notice This function withdraws funds
/// @param amount The amount to withdraw
/* Multi-line comment */
// Single line comment
```

---

### 19. DIRECTIVE — Compiler Directives

**Definition:** Pragma statements, SPDX license identifiers, and import statements.

**Security Relevance:** Pragma version can affect vulnerability exposure (e.g., pre-0.8.0 overflow behavior).

**Solidity Patterns:**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
```

---

### 20. DECLARATION — Type Declarations

**Definition:** State variable declarations, struct definitions, enum definitions, constant declarations, function signatures.

**Security Relevance:** Usually benign, but declaration without initialization can be problematic.

**Solidity Patterns:**
```solidity
uint256 public totalSupply;
mapping(address => uint256) public balances;
struct User { address addr; uint256 balance; }
enum Status { Pending, Active, Closed }
uint256 constant MAX_SUPPLY = 1000000;
function withdraw(uint256 amount) external;
```

---

### 21. EVENT_DEF — Event Definition

**Definition:** Event declarations (not emissions).

**Security Relevance:** None. Events are for off-chain logging only.

**Solidity Patterns:**
```solidity
event Transfer(address indexed from, address indexed to, uint256 amount);
event Approval(address indexed owner, address indexed spender, uint256 value);
```

---

### 22. SYNTAX — Structural Tokens

**Definition:** Closing braces, empty structural elements, and other syntax tokens.

**Security Relevance:** None. Pure syntax with no semantic meaning.

**Solidity Patterns:**
```solidity
}  // closing brace
```

**Note:** Distinct from DECLARATION. Used for batching structural tokens in annotations.

---

## Quick Reference Table

| Code Act | Abbrev | Key Question |
|----------|--------|--------------|
| EXT_CALL | External Call | Does it transfer control to untrusted code? |
| STATE_MOD | State Modification | Is the order correct relative to external calls? |
| ACCESS_CTRL | Access Control | Is authorization sufficient? |
| ARITHMETIC | Arithmetic | Can it overflow/underflow/divide by zero? |
| INPUT_VAL | Input Validation | Are all inputs properly validated? |
| CTRL_FLOW | Control Flow | Can the condition be manipulated? |
| FUND_XFER | Fund Transfer | Are funds protected throughout? |
| DELEGATE | Delegate Call | Is the target trusted and access controlled? |
| TIMESTAMP | Timestamp | Is the time tolerance acceptable? |
| RANDOM | Randomness | Is the entropy source manipulable? |
| ORACLE | Oracle | Is the price feed manipulation-resistant? |
| REENTRY_GUARD | Reentrancy Guard | Does it cover all paths correctly? |
| STORAGE_READ | Storage Read | Could the cached value become stale? |
| SIGNATURE | Signature | Is the signature properly validated? |
| INITIALIZATION | Initialization | Are critical variables properly initialized? |
| COMPUTATION | Hash/Encode | N/A (typically benign) |
| EVENT_EMIT | Event Emission | N/A (logs only, no state change) |
| COMMENT | Documentation | N/A (non-security-relevant) |
| DIRECTIVE | Compiler Directive | Does pragma version affect security? |
| DECLARATION | Type Declaration | Is initialization missing? |
| EVENT_DEF | Event Definition | N/A (non-security-relevant) |
| SYNTAX | Structural Token | N/A (pure syntax) |

---

## Security Functions

Each Code Act plays a specific role in the context of a vulnerability. We call this role the **Security Function**.

### Security Function Types

| Security Function | Symbol | Definition | Model Flags It → |
|-------------------|--------|------------|------------------|
| **ROOT_CAUSE** | 🔴 | The Code Act directly enables exploitation of the documented vulnerability. Removing or fixing this element would eliminate the vulnerability. | Correct (target found) |
| **SECONDARY_VULN** | 🟣 | A real vulnerability that exists in the code but is NOT the documented vulnerability. A separate security issue. | Correct (bonus finding) |
| **PREREQ** | 🟡 | A Code Act necessary for exploitation but not exploitable on its own. Enables or sets up the ROOT_CAUSE. | Partial credit |
| **INSUFF_GUARD** | 🟠 | An attempted protection that fails to prevent the vulnerability. Shows awareness of risk but incorrect mitigation. | Correct if explained |
| **DECOY** | 🔵 | A Code Act that looks suspicious but is actually safe in context. Matches a known vulnerability pattern superficially. | Wrong (pattern matching) |
| **BENIGN** | 🟢 | A security-relevant Code Act that is correctly implemented and safe. | Wrong if flagged |
| **UNRELATED** | ⚪ | A Code Act present in the code but irrelevant to security. | Wrong if flagged |

### Security Function Decision Tree

```
Is this Code Act security-relevant?
│
├── No → UNRELATED
│
└── Yes → Is it a real vulnerability?
    │
    ├── Yes → Is it the DOCUMENTED vulnerability?
    │   │
    │   ├── Yes → ROOT_CAUSE
    │   │
    │   └── No → SECONDARY_VULN
    │
    └── No → Is it necessary for the documented exploit to work?
        │
        ├── Yes → PREREQ
        │
        └── No → Was it intended as a protection?
            │
            ├── Yes (but fails) → INSUFF_GUARD
            │
            └── No → Does it LOOK vulnerable but is actually safe?
                │
                ├── Yes → DECOY
                │
                └── No → BENIGN
```

---

## Common Vulnerability Patterns

### Reentrancy Pattern
```
STORAGE_READ (balance)     → PREREQ
EXT_CALL (transfer)        → ROOT_CAUSE (before state update)
STATE_MOD (balance = 0)    → ROOT_CAUSE (after external call)
```

### Access Control Pattern
```
ACCESS_CTRL (missing)      → ROOT_CAUSE
FUND_XFER (drain)          → PREREQ
```

### Oracle Manipulation Pattern
```
ORACLE (spot price)        → ROOT_CAUSE
ARITHMETIC (calculate)     → PREREQ
FUND_XFER (profit)         → PREREQ
```

### Arithmetic Overflow Pattern
```
INPUT_VAL (missing bounds) → ROOT_CAUSE
ARITHMETIC (overflow)      → ROOT_CAUSE
STATE_MOD (corrupted)      → PREREQ
```

### Initialization Pattern
```
INITIALIZATION (missing)   → ROOT_CAUSE
STATE_MOD (zero default)   → PREREQ
INPUT_VAL (bypassed)       → PREREQ
```

---

## Coverage by Vulnerability Type

| Vulnerability Type | Primary Code Acts | Coverage |
|-------------------|-------------------|----------|
| access_control | ACCESS_CTRL | Full |
| reentrancy | EXT_CALL, STATE_MOD, REENTRY_GUARD | Full |
| price_oracle_manipulation | ORACLE, EXT_CALL | Full |
| arithmetic_error | ARITHMETIC | Full |
| logic_error | CTRL_FLOW, STATE_MOD | Full |
| improper_initialization | INITIALIZATION, STATE_MOD | Full |
| signature_verification | SIGNATURE, INPUT_VAL | Full |
| governance_attack | ACCESS_CTRL, CTRL_FLOW | Full |
| validation_bypass | INPUT_VAL | Full |
| reinitialization | INITIALIZATION, ACCESS_CTRL | Full |
| accounting_manipulation | ARITHMETIC, STATE_MOD | Full |
| bridge_security | ACCESS_CTRL, SIGNATURE | Full |
| pool_manipulation | ORACLE, ARITHMETIC | Full |
| price_manipulation | ORACLE | Full |

---

## Example: Reentrancy Vulnerability

**Vulnerable Code:**
```solidity
function withdraw() external {
    uint256 balance = balances[msg.sender];       // STORAGE_READ
    require(balance > 0, "No balance");           // INPUT_VAL

    (bool success, ) = msg.sender.call{value: balance}("");  // EXT_CALL - ROOT_CAUSE
    require(success, "Transfer failed");

    balances[msg.sender] = 0;                     // STATE_MOD - ROOT_CAUSE
}
```

**Code Act Analysis:**

| Line | Code | Code Act | Security Function |
|------|------|----------|-------------------|
| 2 | `balances[msg.sender]` | STORAGE_READ | PREREQ |
| 3 | `require(balance > 0)` | INPUT_VAL | BENIGN |
| 5 | `msg.sender.call{value}` | EXT_CALL | ROOT_CAUSE |
| 8 | `balances[msg.sender] = 0` | STATE_MOD | ROOT_CAUSE |

**Why ROOT_CAUSE?**
- The EXT_CALL occurs BEFORE the STATE_MOD
- This ordering allows the recipient to call back into `withdraw()` before balance is zeroed
- Fixing either (reordering, or adding REENTRY_GUARD) eliminates the vulnerability

---

## Example: Fixed Version (CEI Pattern)

**Fixed Code:**
```solidity
function withdraw() external {
    uint256 balance = balances[msg.sender];       // STORAGE_READ
    require(balance > 0, "No balance");           // INPUT_VAL

    balances[msg.sender] = 0;                     // STATE_MOD - now BENIGN

    (bool success, ) = msg.sender.call{value: balance}("");  // EXT_CALL - now BENIGN
    require(success, "Transfer failed");
}
```

**Transitions:**
- EXT_CALL: ROOT_CAUSE → BENIGN (now after state update)
- STATE_MOD: ROOT_CAUSE → BENIGN (now before external call)

---

## Glossary

| Term | Definition |
|------|------------|
| **Code Act** | Discrete code operation in a smart contract |
| **Security Function** | Role a Code Act plays in a vulnerability |
| **ROOT_CAUSE** | Code Act that directly enables the documented exploit |
| **SECONDARY_VULN** | Real vulnerability but not the documented one |
| **PREREQ** | Necessary for exploit but not the cause |
| **INSUFF_GUARD** | Failed protection attempt |
| **DECOY** | Safe code that looks suspicious |
| **BENIGN** | Correctly implemented security-relevant code |
| **UNRELATED** | Not security-relevant (omitted from annotations by default) |
| **Transition** | Change in Security Function between versions |
| **CEI Pattern** | Checks-Effects-Interactions (secure ordering) |

---

## References

- Speech Act Theory: Austin, J.L. (1962). "How to Do Things with Words"
- Smart Contract Security: Trail of Bits, OpenZeppelin, Consensys Diligence
- Solidity Patterns: https://solidity-patterns.github.io/
