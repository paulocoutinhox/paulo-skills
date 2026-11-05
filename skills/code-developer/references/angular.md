# Angular

Use a current compatible Angular release and its supported CLI and build system. Angular CLI integrates Vite in its development tooling, but a standalone generic Vite scaffold is not a drop-in replacement for Angular's compiler and builder. Preserve the supported Angular toolchain while satisfying the intent of modern frontend tooling.

Use one component, service, directive, pipe, or primary type per file with hyphenated filenames. Organize by feature. Use current standalone component APIs for new code where supported. Keep templates focused, business behavior in an appropriate service or domain boundary, and dependencies explicit through dependency injection.

Use signals for suitable local reactive state and RxJS for streams where they fit. Use lifecycle-aware subscription cleanup and cancellation. Do not nest subscriptions to hide control flow or retain subscriptions after destruction. Keep derived state computed and avoid multiple mutable sources for the same concept.

Use the existing store when coherent. Consider NgRx Store or SignalStore for substantial shared state only when its structure solves an actual problem. Validate forms and external payloads, use the framework's safe bindings, and do not bypass sanitization without a proven trusted boundary.

Run the actual Angular build, type/template checks, lint when configured, and relevant tests. Exercise routing, forms, request errors, change detection, and SSR hydration when affected. Do not assume a successful TypeScript compile validates every template or browser behavior.
