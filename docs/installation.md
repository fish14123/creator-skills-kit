# 安装与更新

本项目按 Agent Skills 格式组织。下面给出本地文件安装方式；客户端是否发现、选择并完整执行 Skill，需要在所用环境中验证。

## 选择目录

以下路径于 2026-11-06 对照各客户端官方文档整理，按名称排列，不代表推荐顺序。`<项目根目录>` 是你准备使用 Skill 的工作项目，个人目录中的 `~` 是用户主目录。

| 客户端 | 项目级目录 | 个人级目录 | 文档依据 | 本项目验证程度 |
| --- | --- | --- | --- | --- |
| Claude Code | `<项目根目录>/.claude/skills/` | `~/.claude/skills/` | [官方文档](https://code.claude.com/docs/en/skills#choose-where-skills-load) | 文档路径核对；客户端运行待测 |
| Codex | `<项目根目录>/.agents/skills/` | `~/.agents/skills/` | [官方文档](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills) | 文档路径核对；客户端运行待测 |
| Cursor | `<项目根目录>/.cursor/skills/` | `~/.cursor/skills/` | [官方文档](https://cursor.com/docs/skills) | 文档路径核对；客户端运行待测 |

只选择一个适用目录，避免同名 Skill 被多次发现。上表针对本地会话，云端会话、团队策略和插件市场的安装要求请另查客户端文档。本仓库目前不提供客户端插件市场包。

## 复制一个 Skill

先下载或克隆仓库。在仓库根目录运行以下 macOS / Linux shell 示例，**将 `target_dir` 改为上表中你选择的实际目录**。初次体验建议使用项目级目录。

```sh
skill_name='creator-topic-evaluator'
target_dir='/你的项目绝对路径/.agents/skills'

if [ -e "$target_dir/$skill_name" ] || [ -L "$target_dir/$skill_name" ]; then
  printf '目标已存在，请先检查旧版本：%s\n' "$target_dir/$skill_name"
else
  if mkdir -p "$target_dir" &&
     cp -R "skills/$skill_name" "$target_dir/$skill_name" &&
     cp LICENSE "$target_dir/$skill_name/LICENSE"; then
    printf '已复制，请继续在客户端验证：%s\n' "$target_dir/$skill_name"
  else
    printf '复制失败，请检查路径、权限和目标中已复制的文件。\n' >&2
    false
  fi
fi
```

Windows 用户可通过文件管理器完成相同步骤：复制 `skills/` 下所选目录到客户端目录，再把根目录 `LICENSE` 复制进该 Skill 目录。以上命令只用于首次复制，不自动覆盖已有版本。

安装多个 Skill 时，逐个复制需要的目录即可；它们没有相互依赖。每个目录最终应包含：

```text
creator-topic-evaluator/
├── SKILL.md
├── LICENSE
├── references/
└── assets/
```

## 验证成功

1. 在目标项目启动客户端的新会话，查看其 Skill 列表；如没有出现，按官方文档刷新或重启。
2. 用客户端提供的方式显式选择 `creator-topic-evaluator`，或明确要求使用它。Claude Code、Cursor 可在 `/` 菜单查找；Codex CLI / IDE 可用 `/skills` 或 `$` 选择。
3. 已选中 Skill 后发送下面的任务，要求助手先确认读取了参考规则与模板。README 的文件路径提示词用于直接打开源仓库的场景，这里无需填写源仓库路径。
4. 检查输出是否包含目标读者、证据缺口、未知项和决策条件。仅看到 Skill 名称还不能证明执行正确。

```text
请使用已选择的 creator-topic-evaluator，按它的规则和模板评估：
我想写“收藏的链接如何变成每周可用的阅读清单”。
目标读者是独立内容创作者，目前没有访谈和实际使用记录。
请列出已有信息、待补证据和写作决策；不要替我补造经历。
```

如果客户端不能读取相关文件，可手动附上它们。联网能力不足时，其他文字工作仍可继续；事实核查必须说明尚未核验，不能把模型记忆当成最新依据。

## 更新、回退与卸载

- 更新：在源仓库运行 `git pull --ff-only`，查看 `CHANGELOG.md` 与差异；先备份已安装目录中的自定义内容，再替换所选 Skill 的整个目录并保留 `LICENSE`。复制安装不会自动更新。
- 回退：恢复自己保留的旧目录，或从明确的旧提交取回文件。记录来源提交有助于复现问题。
- 卸载：确认路径后移除自己安装的该 Skill 目录，刷新客户端列表。不要删除整个客户端配置目录。

## 常见问题

- **找不到 Skill**：检查目录层级，应为 `skills/<名称>/SKILL.md`，而非多套了一层仓库目录；同时检查项目范围与客户端策略。
- **结果仍像普通对话**：显式选择 Skill，补充必要输入，并确认参考文件能被读取。
- **重复出现同名 Skill**：检查项目级与个人级目录是否同时安装。
- **安装成功但不能查资料**：本项目不提供搜索服务；联网工具由客户端提供。
