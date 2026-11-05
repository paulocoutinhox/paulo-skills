# Vue

Use current compatible Vue and a Vite-based setup for a new application. Follow an existing coherent structure. Prefer single-file components with one component per file and the Composition API for new code when no different project convention applies.

Keep templates declarative. Put reusable stateful behavior in focused composables. Keep pure domain operations and API access outside view components. Use explicit props and emitted events. Avoid mutating props or duplicating derived state. Use computed values for derivation and watchers only for actual side effects. Clean up effects and requests according to component lifetime.

Use Pinia when a genuine shared client store is needed. Keep server-cache ownership separate and do not put session credentials in a persisted public store. Respect SSR request boundaries so state does not leak across users. Avoid injecting untrusted HTML, unsafe URL bindings, index-based keys for mutable lists, and large deep watchers without need.

Run type checking with the project's Vue tooling, lint, production build, and relevant component and integration tests. Verify loading, errors, keyboard use, route transitions, cleanup, and any SSR hydration behavior affected by the change.
