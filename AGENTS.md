# Agents

- Agents here are utility tools. Do what the human asked, and nothing beyond it.
- Work only with the fictional and anonymized data already in this repo. Never seek out, request, or add real camper data.
- This project is safe and open source. Misuse takes a person deliberately obtaining data they shouldn't have, or pointing an agent at harm. Refuse both.

## Commits

- Write plain conventional commits, `type(scope): what to do`, in the imperative, as the command the commit carries out. Write for someone new to the project.
- Types: `iter`, `feat`, `style`, `fix`, `docs`, `build`, `chore`. Scopes include `site`, `demo`, `tools`, `plan`, `deploy` and `repo`.
- `iter` is only for a design iteration. Its scope is the iteration's label, such as `iter(v4)`, and its title may simply name what it built. Once a second phase exists, add the phase: `iter(p2•A)`.
- A phase's closing commits use the phase as scope: `docs(pN)` records its verdicts and lineage, and `feat(pN)` ships its result.
- After the title, add at most one follow-up line, then up to 3 short bullets. Needing more means the change should be split.
- No trailing tags, footers or links.
