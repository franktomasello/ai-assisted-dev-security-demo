<div align="center">

# 🛡️ AI-Assisted Dev Security Demo

**Demonstrating how GitHub Advanced Security catches vulnerabilities in AI-generated code.**

[![GitHub Advanced Security](https://img.shields.io/badge/GitHub-Advanced%20Security-blue?logo=github&logoColor=white)](https://github.com/features/security)
[![CodeQL](https://img.shields.io/badge/CodeQL-Enabled-brightgreen?logo=github)](https://codeql.github.com/)
[![Secret Scanning](https://img.shields.io/badge/Secret%20Scanning-Active-orange?logo=github)](https://docs.github.com/en/code-security/secret-scanning)
[![Dependabot](https://img.shields.io/badge/Dependabot-Enabled-yellow?logo=dependabot)](https://github.com/features/security)

</div>

---

## 📖 Overview

As AI-powered coding assistants become central to modern software development, they can inadvertently introduce security vulnerabilities—SQL injection, hardcoded secrets, insecure dependencies, and more. This repository demonstrates how **GitHub Advanced Security (GHAS)** acts as a safety net, automatically detecting and surfacing those risks before they reach production.

> 💡 **The goal:** Show that even fast, AI-generated code can be made secure with the right toolchain in place.

---

## 🔍 What This Demo Covers

| Feature | Description |
|---|---|
| 🔬 **CodeQL Analysis** | Static analysis that finds logic flaws and security vulnerabilities (e.g. SQL injection, XSS, path traversal) in AI-generated code |
| 🔑 **Secret Scanning** | Detects accidentally committed API keys, tokens, and credentials that AI may suggest inline |
| 📦 **Dependency Review** | Flags vulnerable packages that AI assistants might recommend |
| 🤖 **Dependabot Alerts** | Continuous monitoring of dependencies for newly disclosed CVEs |

---

## 🚀 How It Works

```
Developer uses AI assistant
         │
         ▼
  AI generates code  ──────────────────────────────────┐
         │                                             │
         ▼                                             ▼
  Opens Pull Request                        May contain vulnerabilities:
         │                                  • SQL Injection
         ▼                                  • Hardcoded secrets
  GitHub Advanced Security                  • Insecure dependencies
  automatically scans:                      • XSS / Path traversal
         │
         ▼
  Vulnerabilities surfaced in PR
  before merge ✅
```

---

## 🛠️ GitHub Advanced Security Features in Action

### 🔬 CodeQL — Catching Logic & Security Bugs

CodeQL treats code as data and runs queries against it to find vulnerabilities. It catches patterns that are common in AI-generated code, such as:

- **SQL Injection** — unsanitized user input passed directly into queries
- **Cross-Site Scripting (XSS)** — unescaped output rendered in the browser
- **Path Traversal** — user-controlled file paths accessing unintended directories

### 🔑 Secret Scanning — Stopping Leaked Credentials

AI assistants sometimes suggest code snippets that include placeholder tokens or real-looking credentials. GitHub Secret Scanning:

- Detects over **200+ secret patterns** from major providers
- Alerts immediately when a secret is pushed
- Supports **push protection** to block commits containing secrets

### 📦 Dependency Review — Safe Package Recommendations

AI models are trained on potentially outdated data and may suggest packages with known CVEs. Dependency Review:

- Compares dependencies in a PR against the GitHub Advisory Database
- Blocks merging of PRs that introduce vulnerable packages
- Shows severity ratings inline in the pull request diff

---

## ⚙️ Setup

This demo works out of the box with GitHub Advanced Security enabled on any repository. To replicate the setup:

1. **Enable GitHub Advanced Security** on your repository *(Settings → Security & analysis)*
2. **Enable CodeQL Analysis** — add `.github/workflows/codeql.yml`
3. **Enable Secret Scanning** — toggle in Security settings
4. **Enable Dependabot** — add `.github/dependabot.yml`

---

## 📚 Resources

- [GitHub Advanced Security Documentation](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
- [CodeQL Documentation](https://codeql.github.com/docs/)
- [Secret Scanning Documentation](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
- [Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)
- [GitHub Security Lab](https://securitylab.github.com/)

---

## 🤝 Contributing

Found a new vulnerability pattern worth demonstrating? Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-vuln-demo`
3. Commit your changes: `git commit -m 'Add: demonstrate [vulnerability type]'`
4. Push and open a Pull Request

---

<div align="center">

Made with ❤️ to help developers ship **secure** AI-assisted code.

⭐ Star this repo if you found it useful!

</div>
