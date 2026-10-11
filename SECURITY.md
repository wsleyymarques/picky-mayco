# Security policy

Agent skills are privileged instructions. A malicious or careless change can influence tool use, expose data, or trigger destructive commands.

Report suspected prompt injection, secret exposure, unsafe command execution, or dependency compromise through a private GitHub security advisory. Do not publish exploit details in a public issue before maintainers can assess them.

When reviewing a contribution:

- Inspect every instruction and executable file.
- Confirm external actions remain within user authorization.
- Require approval immediately before sensitive or high-impact actions.
- Reject embedded credentials, remote code downloads, and unexplained network access.
- Verify scripts operate only on explicit, narrow targets.

Supported versions are the latest tagged release and the current `main` branch.
