# React

For a new client-rendered application, use Vite unless the user requests a framework with its own supported toolchain. Keep one component per file. Separate components by meaningful responsibility, and put reusable lifecycle behavior in focused hooks. Keep pure computations outside effects and avoid unnecessary wrappers or abstractions.

Choose the smallest owner for state. Derive values rather than synchronizing duplicate state. Use stable domain keys for dynamic lists. Treat render as pure. Use effects for synchronization with external systems, with correct dependencies and cleanup. Do not suppress hook dependency warnings to hide a lifecycle defect. Prevent stale async responses and clean up subscriptions on unmount.

Start with local state and context where appropriate. For substantial shared client state, evaluate the project's existing library and a current compatible store such as Redux Toolkit or Zustand according to the real requirements. There is no universal best store. Use a dedicated query cache when server-state semantics warrant it, rather than copying remote data into multiple stores.

Avoid unsafe HTML injection, token exposure, mutation of React state, unstable callback assumptions, and excessive memoization without evidence. Verify accessibility, loading, empty and error states, navigation, and relevant concurrent behavior. Run type checking, lint, a production build, and focused component or integration tests.
