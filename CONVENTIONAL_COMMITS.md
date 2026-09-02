# Conventional Commits

Guia da convenção de mensagens de commit adotada neste repositório.

## O que é

Conventional Commits é um padrão para escrever mensagens de commit. A ideia é que a
mensagem siga uma estrutura fixa, começando por um **tipo** que diz qual é a natureza
da mudança.

Sem padrão:

```
alteracoes
ajustes finais
agora vai
corrigi o bug
```

Com padrão:

```
feat: adiciona endpoint de favoritos
fix: corrige duracao negativa ao criar musica
docs: atualiza exemplos de curl no README
```

A diferença prática: dá para ler o histórico e entender o que aconteceu sem abrir cada
commit, dá para filtrar (`git log --oneline --grep "^feat"`), e ferramentas conseguem
gerar changelog e calcular a próxima versão automaticamente.

## Estrutura

```
<tipo>(<escopo opcional>): <descrição>

<corpo opcional>

<rodapé opcional>
```

Exemplo completo:

```
feat(playlist): adiciona filtro de musicas favoritas

Adiciona o query param ?favorita=true no endpoint de musicas para
permitir listar apenas as faixas marcadas como favoritas.

Closes #12
```

Na maioria dos casos só a primeira linha basta.

## Os tipos

| Tipo | Quando usar |
| :--- | :--- |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | Nova funcionalidade para quem usa a API |
| ![fix](https://img.shields.io/badge/fix-D73A4A?style=flat-square) | Correção de um bug |
| ![docs](https://img.shields.io/badge/docs-0969DA?style=flat-square) | Só documentação (README, comentários, este arquivo) |
| ![style](https://img.shields.io/badge/style-8250DF?style=flat-square) | Formatação que não muda comportamento (espaços, identação) |
| ![refactor](https://img.shields.io/badge/refactor-BF8700?style=flat-square) | Reescrita que não corrige bug nem adiciona funcionalidade |
| ![perf](https://img.shields.io/badge/perf-E36209?style=flat-square) | Mudança que melhora desempenho |
| ![test](https://img.shields.io/badge/test-0E8A8A?style=flat-square) | Adiciona ou corrige testes |
| ![build](https://img.shields.io/badge/build-6E4C1E?style=flat-square) | Sistema de build ou dependências (`requirements.txt`, `Dockerfile`) |
| ![ci](https://img.shields.io/badge/ci-24292F?style=flat-square) | Configuração de integração contínua (GitHub Actions, pipelines) |
| ![chore](https://img.shields.io/badge/chore-6E7781?style=flat-square) | Manutenção que não entra em nenhuma categoria acima |
| ![revert](https://img.shields.io/badge/revert-82071E?style=flat-square) | Desfaz um commit anterior |

As cores agrupam os tipos por família: **verde e vermelho** são os dois que mudam o
comportamento da API (`feat` e `fix`), **azul** é documentação, **roxo, âmbar, laranja e
turquesa** mexem na qualidade do código sem alterar o que a API entrega, e os **tons de
cinza e marrom** são infraestrutura e manutenção.

### As dúvidas mais comuns

**![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) ou ![fix](https://img.shields.io/badge/fix-D73A4A?style=flat-square)?**
Se antes não existia, é `feat`. Se existia mas funcionava errado, é `fix`.

**![refactor](https://img.shields.io/badge/refactor-BF8700?style=flat-square) ou ![fix](https://img.shields.io/badge/fix-D73A4A?style=flat-square)?**
Se o comportamento visível mudou, é `fix`. Se só a organização interna do código mudou e
a saída é idêntica, é `refactor`.

**![chore](https://img.shields.io/badge/chore-6E7781?style=flat-square) ou ![build](https://img.shields.io/badge/build-6E4C1E?style=flat-square)?**
Mexeu em dependências ou no processo de gerar o projeto, é `build`. `chore` é o
guarda-chuva do que sobra: configuração inicial, `.gitignore`, limpeza de arquivos.

**![docs](https://img.shields.io/badge/docs-0969DA?style=flat-square) ou ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square)?**
Documentação nunca é `feat`, mesmo quando dá trabalho. Se o código não mudou, é `docs`.

## Escopo

O escopo é opcional e vai entre parênteses, indicando a parte do projeto afetada:

```
feat(playlist): adiciona ordenacao por ano de lancamento
fix(config): corrige ALLOWED_HOSTS vazio em producao
```

Neste projeto os escopos naturais são `playlist` e `config`, os dois apps. Em um
projeto pequeno, omitir o escopo é perfeitamente aceitável.

## Como escrever a descrição

- **Modo imperativo**: "adiciona", não "adicionado" nem "adicionando". A frase completa
  o sentido de "Se aplicado, este commit vai _adicionar..._".
- **Minúscula** na primeira letra.
- **Sem ponto final.**
- **Até ~50 caracteres.** Se não couber, o resto vai no corpo.
- **Diga o quê, não o como.** O diff já mostra o como.

| ❌ Ruim | ✅ Bom |
| :--- | :--- |
| `feat: Adicionei o serializer.` | `feat: adiciona serializer de Album` |
| `fix: bug` | `fix: impede duracao negativa em Musica` |
| `chore: mudancas` | `chore: adiciona gitignore do Python` |
| `feat: mudei o views.py e o urls.py` | `feat: expoe CRUD de albuns via router` |

## Breaking changes

Quando a mudança quebra compatibilidade com quem já consome a API, marque com `!` depois
do tipo:

```
feat!: renomeia campo duracao_segundos para duracao
```

Ou descreva no rodapé, que é o formato preferido quando precisa de explicação:

```
feat: renomeia campo duracao_segundos para duracao

BREAKING CHANGE: o campo duracao_segundos foi renomeado para duracao
em MusicaSerializer. Clientes que enviam ou leem duracao_segundos
precisam ser atualizados.
```

## Relação com versionamento semântico

Se o projeto usar [SemVer](https://semver.org/lang/pt-BR/) (`MAJOR.MINOR.PATCH`), os
tipos mapeiam direto:

| Tipo de commit | Incremento | Exemplo |
| :--- | :--- | :--- |
| ![fix](https://img.shields.io/badge/fix-D73A4A?style=flat-square) | PATCH | `1.0.0` → `1.0.1` |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | MINOR | `1.0.0` → `1.1.0` |
| ![BREAKING CHANGE](https://img.shields.io/badge/BREAKING%20CHANGE-82071E?style=flat-square) | MAJOR | `1.0.0` → `2.0.0` |

Os demais tipos (`docs`, `chore`, `style`, `test`...) não geram nova versão.

## Um commit, uma mudança

O padrão só ajuda se cada commit tiver um propósito único. Se você precisa escrever
"e" na descrição, provavelmente são dois commits:

```
# Ruim
feat: adiciona serializers e corrige bug do admin

# Bom
feat: adiciona serializers de Album e Musica
fix: corrige registro duplicado no admin
```

Para dividir mudanças que já estão no diretório de trabalho, use `git add` por arquivo
em vez de `git add -A`.

## O histórico deste projeto

Os commits iniciais seguem o padrão e servem de referência:

| Tipo | Commit |
| :--- | :--- |
| ![docs](https://img.shields.io/badge/docs-0969DA?style=flat-square) | `docs: adiciona README com instalacao e endpoints da API` |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | `feat: registra Album e Musica no Django admin` |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | `feat: expoe CRUD de albuns e musicas via router do DRF` |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | `feat: adiciona serializers de Album e Musica` |
| ![feat](https://img.shields.io/badge/feat-2EA44F?style=flat-square) | `feat: cria modelos Album e Musica com migrations` |
| ![chore](https://img.shields.io/badge/chore-6E7781?style=flat-square) | `chore: configura projeto Django com SQLite e DRF` |
| ![chore](https://img.shields.io/badge/chore-6E7781?style=flat-square) | `chore: adiciona gitignore e dependencias do projeto` |

Repare que a ordem importa: `config/urls.py` entrou junto do commit de rotas, e não do
commit de configuração, porque ele faz `include('playlist.urls')` — colocá-lo antes
deixaria aquele commit sem conseguir rodar sozinho. Cada commit deve deixar o projeto
em um estado funcional.

## Referência

Especificação oficial: <https://www.conventionalcommits.org/pt-br/v1.0.0/>
