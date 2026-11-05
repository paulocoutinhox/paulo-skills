# Sources and rule ownership

Verified: 2026-11-05. Check version-specific APIs again when working in a concrete repository.

- [uv projects](https://docs.astral.sh/uv/guides/projects/) and [Ruff](https://docs.astral.sh/ruff/): Python environment, lint, and formatting tools.
- [Swift ARC](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) and [Swift 6 concurrency](https://developer.apple.com/documentation/swift/adoptingswift6): ownership and isolation. The full bodies were verified through the official [ARC documentation data](https://docs.swift.org/swift-book/data/documentation/the-swift-programming-language/automaticreferencecounting.json) and [concurrency Markdown](https://developer.apple.com/documentation/swift/adoptingswift6.md) after the JavaScript frontends proved unsuitable for static reading.
- [Android architecture recommendations](https://developer.android.com/topic/architecture/recommendations) and [Kotlin coroutines](https://kotlinlang.org/docs/coroutines-basics.html): state flow, lifecycle, layering, and structured concurrency.
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) and [clang-format options](https://clang.llvm.org/docs/ClangFormatStyleOptions.html): resource ownership, concurrency, and formatter controls.
- [Thinking in React](https://react.dev/learn/thinking-in-react), [Vue state management](https://vuejs.org/guide/scaling-up/state-management.html), [Angular style guide](https://angular.dev/style-guide), and [Vite](https://vite.dev/guide/): component responsibility, state choices, filenames, and tooling.

MVVM defaults, helper naming, one primary type per file, empty Python initializers, no `TYPE_CHECKING`, no anonymous C++ namespaces, class-owned C++ functions, and lambda format guards are owner conventions. They are not universal requirements imposed by the languages. Safe language or framework exceptions are stated in each profile.
