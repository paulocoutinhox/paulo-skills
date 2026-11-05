# Kotlin and Android

## Architecture

Preserve a coherent existing architecture. For a new Android app without one, use MVVM with separate models, views or Compose screens, and view models. Prefer unidirectional data flow: immutable UI state travels down, events travel up. Use repositories for actual data boundaries. Add a domain layer only for meaningful shared business behavior. Use one primary class, enum, or screen per file, following Kotlin's symbol-based filename conventions.

Expose read-only state such as `StateFlow` and retain mutation in its owner. Make loading, empty, success, and error behavior explicit. Keep navigation decisions and transient effects deliberate. Do not use a global event bus to hide dependencies or duplicate state across the screen and view model.

## Lifecycle, concurrency, and memory

Use structured coroutines in an owned scope such as `viewModelScope`. Collect UI flows with the platform's lifecycle-aware APIs. Avoid `GlobalScope`, leaking Activity contexts, unmanaged listeners, and long-running references to views. Do not block the main thread. Inject dispatchers for blocking work and testability. Preserve cancellation and do not turn `CancellationException` into a normal failure.

Bound concurrent requests, close streams, and clean up listeners and resources. Use atomic state updates or confinement where multiple coroutines modify shared state. A coroutine is not automatically race-free. Review recomposition stability, list keys, and captured state in Compose.

## Safety and verification

Use null safety, exhaustive sealed states, and explicit error results. Avoid `!!`, broad exception suppression, reflective behavior, and unnecessary mutable collections. Keep credentials in platform-backed secure storage, disable cleartext traffic where appropriate, minimize exported components and permissions, validate intents and app links, and enforce permissions on the server.

Use the checked-in Gradle wrapper, version catalog when present, compatible Kotlin/AGP/JDK versions, formatter or ktlint, static analysis, and relevant unit, coroutine, and instrumentation tests. Validate process recreation, lifecycle transitions, configuration changes, offline errors, and cancellation where affected. For non-Android Kotlin, adapt lifetime and architecture to the actual framework rather than adding Android classes.
