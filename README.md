# AIO-Core Alpha

An experimental Python desktop-companion and worker-node project. The repository includes a Qt companion, modular core components, and a small TCP worker example.

## Current implementation

- `loki_companion/loki_companion_public.py` integrates camera input, microphone input, speech recognition, text-to-speech, desktop UI, and a local Ollama generation endpoint.
- `core/node_worker_public.py` is a minimal TCP listener example.
- `core/` contains prototype modules for task handling, knowledge, and learning.

## Privacy and network safety

**Review this code before running it.** The companion accesses the camera and microphone and calls Google's speech-recognition service for recognized audio. Its text-generation endpoint defaults to local Ollama.

The worker binds to `0.0.0.0:4444` and has no authentication. Do not run it on an untrusted network or expose the port to the internet. This is a prototype, not a hardened remote worker service.

Install the listed Python dependencies from the repository root with `python -m pip install -r requirements.txt`. The desktop companion entry point is `python loki_companion/loki_companion_public.py`; local camera, microphone, audio, and Ollama setup may also be required.

## Research topics and search terms

Relevant topics include **AI learning experiments**, **AI evolution prototype components**, **AI agents**, **local LLM/Ollama integration**, and multimodal desktop companions. Learning/evolution modules are experimental; this repository does not establish a tested, autonomous self-improvement capability.
## Fenrir-Alpha

A separate, private AI-orchestration project has a limited [public overview](https://github.com/Loki-Der-Wahnsinn/EvoLoki_SuperKI/blob/main/FENRIR_ALPHA_OVERVIEW.md). The implementation and operational data remain private.

## Related public experiments

- [EvoLoki SuperKI](https://github.com/Loki-Der-Wahnsinn/EvoLoki_SuperKI) — experimental agent, model-provider, and Ollama-worker components.
- [FreedomAI](https://github.com/Loki-Der-Wahnsinn/FreedomAI) — small Python team-orchestration prototype.

## License

No license is currently provided. Public visibility allows you to view this repository; it does not grant permission to reuse, modify, or distribute its contents.