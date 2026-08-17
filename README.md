# mi-proyecto

CLI para listar las instalaciones de GitHub Apps de tu cuenta y a qué repositorios
llega cada una — el equivalente en terminal de
<https://github.com/settings/installations>.

Solo usa la librería estándar de Python (3.8+). No hay dependencias que instalar.

## Uso

```bash
export GITHUB_TOKEN=ghp_...        # token personal con scope read:user
python3 gh_installations.py
```

Salida:

```
2 installation(s)

#12345678  claude  (account: shuart9, User)
    repository access: selected

#87654321  dependabot  (account: shuart9, User)
    repository access: all
```

### Opciones

| Opción | Qué hace |
| --- | --- |
| `--repos` | Lista además los repositorios accesibles por cada instalación |
| `--json` | Devuelve JSON en vez de texto (útil para `jq`) |
| `--token TOKEN` | Token explícito, en lugar de `$GITHUB_TOKEN` |

```bash
python3 gh_installations.py --repos
python3 gh_installations.py --json | jq '.[] | select(.repository_selection == "all")'
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Los tests no tocan la red: cubren el parseo del header `Link`, la paginación
(con `_request` sustituido), la normalización de los payloads y el formato de
salida.

## Notas

- El endpoint usado es `GET /user/installations`, que devuelve las instalaciones
  visibles para el usuario autenticado.
- Un token sin el scope adecuado responde `403`; el error se imprime tal cual
  llega de la API para que se vea el motivo.

## Licencia

MIT — ver [LICENSE](LICENSE).
