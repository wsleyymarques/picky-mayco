# Picky Mayco

O Picky Mayco é uma suíte de *Agent Skills* para conduzir mudanças full-stack com mais consistência. Ela transforma um pedido de implementação em um fluxo explícito de análise, estratégia, execução, testes e documentação, para que detalhes de interface, API, validação, segurança e qualidade não sejam esquecidos.

O repositório é a fonte única das skills. Ele segue o formato aberto de Agent Skills: cada skill é uma pasta com um `SKILL.md` e, quando necessário, referências e metadados. Por isso pode ser usado no Codex, no Claude Code e em outros agentes que reconheçam esse formato.

## Quando usar

Use Picky Mayco ao implementar, revisar ou planejar uma mudança que possa afetar frontend, backend, contratos de API, imagens, testes ou documentação. É especialmente útil para formulários, fluxos de usuário, endpoints, regras de domínio, uploads e mudanças que precisam ser fáceis de verificar.

Ele não substitui as convenções do projeto: primeiro inspeciona o repositório e suas instruções e, depois, aplica o fluxo da skill dentro desses limites.

## O fluxo de trabalho

1. Lê o pedido, as instruções do repositório, o código relacionado, os testes e referências visuais fornecidas.
2. Separa o impacto em **Frontend**, **Backend** e **Contrato compartilhado**, registrando também o que não muda.
3. Carrega apenas as especialidades necessárias e produz uma estratégia com riscos, casos de borda e verificação.
4. Aguarda aprovação da estratégia antes de alterar código, exceto quando a implementação imediata foi solicitada.
5. Durante e ao fim da implementação, verifica testes, automação Cypress, documentação, mapa do repositório e aprendizados reutilizáveis.

O resultado esperado é uma entrega que explica claramente o que mudou em cada camada, quais verificações foram executadas e quais riscos permanecem, se houver.

## Skills incluídas

| Skill | Responsabilidade |
| --- | --- |
| `picky-mayco` | Coordena a análise, escolhe as especialidades aplicáveis, monta a estratégia e padroniza a entrega final. |
| `picky-mayco-frontend` | Cobre UI, formulários, validação, responsividade, acessibilidade, estados de tela e referências visuais. |
| `picky-mayco-backend` | Cobre validação de entrada, regras de domínio, autorização, persistência, falhas e contratos de API. |
| `picky-mayco-images` | Cobre o ciclo completo de imagens: seleção, upload, validação, transformação, armazenamento, entrega e exclusão. |
| `picky-mayco-qa` | Define a matriz de testes, a preparação para Cypress e a validação final baseada em evidências. |
| `picky-mayco-docs` | Mantém Markdown, catálogo de seletores Cypress e o `index.md` de navegação do repositório coerentes com o código. |
| `consume` | Lê e registra aprendizados duráveis, baseados em evidências, sem guardar segredos ou histórico inútil de tarefas. |

## Instalação

Pré-requisitos para os comandos abaixo: Git e Python 3. O repositório é público em [wsleyymarques/picky-mayco](https://github.com/wsleyymarques/picky-mayco).

### Codex

Clone o repositório e execute o instalador:

```bash
git clone https://github.com/wsleyymarques/picky-mayco.git
cd picky-mayco
python3 scripts/install.py
```

Por padrão, ele instala todas as skills em `~/.codex/skills`; se `CODEX_HOME` estiver configurado, usa `<CODEX_HOME>/skills`. Inicie uma nova interação do Codex após a instalação e peça explicitamente, por exemplo:

```text
$picky-mayco analise e implemente esta tarefa: ...
```

Para instalar somente uma skill, repita `--skill`:

```bash
python3 scripts/install.py --skill picky-mayco --skill picky-mayco-qa
```

O projeto também contém `plugin.json`, portanto é um plugin portátil. Hosts que oferecem instalação de plugins podem instalar o repositório como plugin; veja a [documentação de plugins do Codex](https://developers.openai.com/plugins/build/plugins) para a interface disponível na sua versão.

### Claude Code

Claude Code descobre skills no sistema de arquivos. Instale o mesmo pacote no diretório global de skills:

```bash
git clone https://github.com/wsleyymarques/picky-mayco.git
cd picky-mayco
python3 scripts/install.py --dest ~/.claude/skills
```

Para compartilhar as skills com quem trabalha em um único projeto, use o diretório do projeto e versione-o junto com o código:

```bash
python3 scripts/install.py --dest .claude/skills
```

Abra uma nova sessão do Claude Code depois da instalação. Ele pode selecionar uma skill automaticamente quando a descrição da tarefa corresponder; quando quiser garantir o fluxo completo, peça para usar `picky-mayco` na tarefa. O layout `.claude/skills/<nome>/SKILL.md` é o local recomendado pelo [Claude Code](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips).

### Outros agentes compatíveis com Agent Skills

Muitos agentes usam o mesmo formato: uma pasta por skill contendo `SKILL.md`, com suas referências e scripts. Para eles:

1. Descubra na documentação do agente qual é o diretório de skills ou a opção de importação de uma skill.
2. Execute o instalador apontando para esse diretório:

   ```bash
   python3 scripts/install.py --dest /caminho/para/o/diretorio-de-skills
   ```

3. Reinicie a sessão do agente e solicite a skill pelo nome, caso o host não faça seleção automática.

Também é possível importar manualmente as pastas de `skills/`. Mantenha cada pasta intacta — não copie apenas o `SKILL.md`, pois algumas skills possuem arquivos em `references/` e `agents/`.

Para integrações por API, faça o upload ou anexe os diretórios de skill de acordo com o provedor. A [documentação de Skills da OpenAI](https://developers.openai.com/api/docs/guides/tools-skills) e a [documentação de Agent Skills da Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) descrevem as opções de API e seus limites.

## Atualizações e distribuição

Não edite uma cópia instalada em `~/.codex/skills` ou `~/.claude/skills`: ela é apenas uma cópia de execução. Faça as mudanças neste repositório, valide-as, publique-as no GitHub e então atualize a instalação de cada ambiente.

```bash
git checkout -b minha-alteracao
# edite as skills, referências, scripts ou documentação necessários
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git add .
git commit -m "descrição da alteração"
git push -u origin minha-alteracao
```

Depois que a alteração for integrada à `main`, cada consumidor atualiza seu clone com `git pull --ff-only` e reinstala as skills no diretório do seu agente. O instalador se recusa intencionalmente a sobrescrever uma instalação existente; isso evita apagar alterações locais sem aviso. Remova ou substitua conscientemente as pastas antigas antes de executar a reinstalação.

Para uma equipe, mantenha um clone ou submódulo apontando para uma versão revisada do repositório. Assim todos usam a mesma revisão e uma atualização passa por revisão e testes antes de chegar aos agentes.

## Desenvolvimento e validação

Antes de abrir uma alteração, execute:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo de contribuição e [SECURITY.md](SECURITY.md) para relatar questões de segurança.

## Licença

[MIT](LICENSE).
