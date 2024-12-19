
### 2024/12/19(1.0.0)
- supported loaders
  - default: just load using `pythonnet.load`.
  - system: get information from system installed dotnet and load.
  - offline: extract binary from assets and load.
    - currently, use runtime version of dotnet binary for saving asset size and loading time.
