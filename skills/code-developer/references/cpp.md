# C++

## Standard and organization

Inspect the actual compiler and configured standard. Use the strongest appropriate facilities available in that standard. `C++21` is not an ISO standard name. If requested, clarify whether C++20 or C++23 is intended rather than inventing a compiler flag.

Keep includes direct, minimal, ordered, and self-sufficient. Do not rely on transitive includes. Keep header declarations and implementations consistent. Use one primary class or enum per file. Put application types in named project namespaces. Do not use anonymous namespaces or `using namespace` directives in headers. Under this collection's convention, application functions belong to classes, with static methods where no instance state is required. Required language entrypoints such as `main`, mandated operators, or framework hooks are explicit exceptions. Do not create unusable C++ to imitate a universal class-only rule.

Do not add descriptive method, member, or section comments in headers. Make names and types carry intent. Required tooling directives and license notices retain their exact form.

## Ownership and correctness

Prefer values, RAII, `const`, references, containers, and unique ownership. Use `std::unique_ptr` for exclusive dynamic ownership and `std::shared_ptr` only when ownership is actually shared. Use weak references to break shared cycles. A non-owning raw pointer can express optional observation where the project requires it, but never use ambiguous raw ownership or manual `new`/`delete` when RAII can express the lifetime.

Avoid C-style casts, unchecked narrowing, pointer arithmetic, macros, and C library patterns when standard C++ alternatives exist. When integrating a C API, isolate it in a C++ adapter with correct linkage, explicit sizes, ownership, custom deleters, and error translation. Do not cast away constness to satisfy an API.

Check indexing, iterator validity, object lifetime, alignment, initialization, signed overflow, unsigned wrap, numeric conversion, exception safety, and bounds before access. Use checked arithmetic for untrusted sizes. Apply the rule of zero where possible. Do not return dangling references or capture shorter-lived objects by reference in escaping lambdas.

## Concurrency

Choose clear ownership and synchronization. Guard shared mutable state consistently, use RAII locks, establish lock order, and avoid invoking unknown code while holding a lock. Join owned threads and preserve lifetime through asynchronous work. Use atomics with a justified memory model, not as a substitute for a coherent concurrency design. Review data races, deadlocks, reentrancy, cancellation, and partial initialization explicitly.

## Lambda formatting preference

Wrap the smallest region containing each lambda in balanced formatter directives, and hand-format it clearly. This is an owner preference, not a claim that clang-format cannot format lambdas.

```cpp
// clang-format off
const auto isReady = [](const Task& task) {
    return task.isReady();
};
// clang-format on
```

Keep the surrounding code formatted normally. Do not disable formatting for an entire file to avoid reviewing one expression.

## Verification

Use the declared CMake or other build system, warnings, clang-format, and configured clang-tidy checks. Run AddressSanitizer and UndefinedBehaviorSanitizer for relevant memory and arithmetic paths. Run ThreadSanitizer separately where supported for concurrent changes. Add boundary and lifetime tests where they meaningfully detect the defect. Tool availability and platform limitations must be reported. No tool proves the absence of all UB or races.
