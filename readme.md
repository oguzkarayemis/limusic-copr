# Limusic COPR Repository

This repository contains the RPM packaging files (`.spec` and `Makefile`) to distribute the official [Limusic](https://github.com/SimoHypers/limusic) desktop application for Fedora Linux via Copr.

Limusic is a desktop YouTube Music client written with Tauri, Rust, and SvelteKit — ad-free, with no Electron.

## Installation

You can easily install Limusic on Fedora by enabling this COPR repository:

```bash
sudo dnf copr enable oguzkarayemis/limusic
sudo dnf install limusic
```

## How it works

This repository utilizes COPR's `make_srpm` feature. The included `Makefile` automatically fetches the latest `.rpm` release from the upstream GitHub repository and wraps it into an SRPM, which COPR then builds for the supported `x86_64` Fedora chroots.

## Links

*   **Upstream Project:** [SimoHypers/limusic](https://github.com/SimoHypers/limusic)
*   **COPR Project Page:** [oguzkarayemis/limusic](https://copr.fedorainfracloud.org/coprs/oguzkarayemis/limusic/)