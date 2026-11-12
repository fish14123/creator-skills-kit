# Creator Skills Kit（创作者工具包）

面向内容创作者的一组 Skill 与模板，覆盖选题评估、标题优化、长文结构、事实核查、内容复盘和多平台分发。

适合写公众号、工具教程和知识类文章的个人作者。把素材、正文或发布数据交给相应 Skill，得到可以继续修改的大纲、标题、核查台账或草稿。每个 Skill 都能单独使用。

Instruction-based skills and templates for Chinese-language content creators. Organized using the [Agent Skills format](https://agentskills.io/specification); no particular AI provider is required.

## 你可以用它做什么

| 你的问题 | 使用的 Skill | 主要交付物 |
| --- | --- | --- |
| 这个选题值得现在写吗？ | [creator-topic-evaluator](skills/creator-topic-evaluator/SKILL.md) | 选题卡、证据缺口和决策条件 |
| 哪个标题更准确、更值得点开？ | [creator-title-optimizer](skills/creator-title-optimizer/SKILL.md) | 候选评分表、推荐与误读风险 |
| 素材很多，文章怎么组织？ | [creator-longform-structure](skills/creator-longform-structure/SKILL.md) | 文章地图、大纲与每节证据缺口 |
| 这些功能、数字和案例可信吗？ | [creator-fact-checker](skills/creator-fact-checker/SKILL.md) | 带来源定位、核验状态与修改建议的主张台账 |
| 上篇文章的数据能说明什么？ | [creator-content-review](skills/creator-content-review/SKILL.md) | 同口径复盘、下一轮假设与实验 |
| 成稿如何适配其他平台？ | [creator-distribution-kit](skills/creator-distribution-kit/SKILL.md) | 各平台草稿和发布前检查清单 |

## 5 分钟体验

1. 下载本仓库，或克隆到本地：

   ```sh
   git clone https://github.com/fish14123/creator-skills-kit.git
   cd creator-skills-kit
   ```

2. 在能够读取本地文件的 AI 助手中打开这个目录，发送：

   ```text
   请读取 skills/creator-topic-evaluator/SKILL.md，并按其中引用的规则和模板评估：
   我想写“收藏的链接如何变成每周可用的阅读清单”。
   目标读者是独立内容创作者，目前没有访谈和实际使用记录。
   请列出已有信息、待补证据和写作决策；不要替我补造经历。
   ```

   如果助手不能读本地文件，手动提供该目录的 `SKILL.md`、`references/` 和 `assets/` 中相关文件。这种方式是显式提供上下文，不代表客户端已自动安装 Skill。

3. 检查结果：应说明证据缺口及决策条件；未知评分应保留待补，不能凭空给出读者反馈或作者经历。

想先看成品？阅读[完整演示](examples/README.md)：同一份素材如何走过选题、标题、结构、核查、分发和复盘。**其中的角色、记录与数据均为合成示例，不代表作者真实经历或模型效果测评。**

## 安装与兼容性

需要自动发现 Skill 时，按[安装指南](docs/installation.md)复制到所用客户端的 Skill 目录，并验证是否加载。保留整个 Skill 目录及许可文件，不要只复制 `SKILL.md`。

本项目提供按官方文档整理的 Claude Code、Codex 和 Cursor 本地目录示例，统一标注验证程度；尚未完成这三个客户端的安装与全流程验收。目录与 CSV 的静态检查、助手行为检查、客户端兼容性测试是不同的验证项，见[验证说明](docs/validation.md)。

使用方法与模板不需要购买会员或配置本项目的 API Key。模型服务费用、联网搜索与文件访问能力由你使用的 AI 助手决定；事实核查缺少联网能力时，应交付待核台账和资料缺口。

## 使用边界

- 核查结论应能追溯到支持或反对它的材料；没有依据的数字、引用、案例和作者经历不能补写。
- 标题评分与选题判断用于辅助编辑决策，不预测打开率或保证流量。
- 复盘应使用相同统计窗口与指标口径；观察到差异后先提出假设。
- 分发只生成草稿，不登录社交账号或自动发布。
- 会员知识库与外部内容未包含在本仓库中。

## 维护与贡献

欢迎提交实际使用中可复现的问题、匿名化案例、规则修正与平台适配建议。请先读[贡献指南](CONTRIBUTING.md)，版本变更见 [CHANGELOG.md](CHANGELOG.md)。

维护者可运行以下检查（需要 Python 3.10+；不运行任何模型，也不调用外部服务）：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

需要远端持续检查时，可参考 [GitHub Actions 配置样例](docs/ci-workflow.example.yml)。本版本仅提供样例，尚未启用仓库工作流；启用方式见[验证说明](docs/validation.md)。

## 可选资源：懒笔头会员知识库

开源工具包提供方法、模板与公开演示，可以独立使用。如果你另外需要持续维护的作者写作参考资料，可了解腾讯 IMA 中的「懒笔头 · 公众号写作助手（会员版）」：

[查看会员知识库介绍](https://ima.qq.com/wiki/?shareId=5ca82565e36f0fd30a6c66aa2349a438e5c2f0328b8ec9b9435298917544ae52) · [查看宣传海报](assets/ima-member-poster-with-qr.png)

会员库的资料、访问权和订阅以产品页面为准，不随本仓库安装；付费不会改变本仓库的功能。海报中的价格等信息可能变化，请以实际产品页面为准。

## 许可

本仓库文件按 [MIT License](LICENSE) 授权；外部会员库与第三方标识的范围说明见 [NOTICE.md](NOTICE.md)。
