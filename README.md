# World Model Atlas · 从生成到行动

面向了解 VLM、VLA，但不熟悉视频生成的读者，一份中文交互教程。

教程从 Diffusion、Flow Matching、latent 与 DiT 开始，解释视频时空建模、JEPA 表征学习、世界模型与规划，再连接到视频—动作模型。代表工作包括 Wan、Cosmos、DreamZero、LingBot-VA、GigaWorld 等。所有模型卡附一手论文、官方项目或代码链接；不同版本分开讨论。

在线阅读：https://shuochen007.github.io/world-model-atlas/

## 使用

直接打开 `index.html` 即可。HTML 已内嵌全部 CSS、JavaScript 和模型数据，无需网络依赖、构建服务或 API key。外部链接只用于阅读原论文和官方演示。

```sh
python3 build.py
python3 -m http.server 8765
```

访问 `http://localhost:8765`。在 GitHub Pages 中选择从 `main` 分支根目录部署。

## 内容与交互

- 11 个学习章节、30 个代表模型/方法条目，完整的一手资料与术语索引。
- VLM / VLA / WM / WAM 接口切换。
- 加噪与反向播放、二维流场、时空注意力、JEPA 目标对比。
- 动作条件动力学与误差累积实验。
- 每个代表模型独立的分步骤架构、训练 / 推理机制和能力边界。
- WAM 信息流与开环 / 闭环 / 异步时间线。
- 搜索、分类筛选、模型深链接、学习测验和本地进度。
- 响应式布局、键盘焦点、减少动画选项。

## 源码结构

- `template.html`：语义结构与主要教程正文。
- `styles.css`：响应式样式。
- `app.js`：原生 Canvas 绘图、交互和页面逻辑。
- `base-models.json`、`world-models.json`、`wam-models.json`：带来源的模型内容。
- `build.py`：校验模型数据并生成独立的 `index.html`。

## 教学边界

资料核对日期为 **2026-10-23**。可视化均为原创教学示意，不是模型实际推理、论文测量结果或性能排名。噪声动画的反向播放并不运行神经网络；动力学实验是一个明确标注的玩具系统。模型之间的概念连线不都代表权重继承。

不将不同 benchmark 的成功率混排；不将视觉世界先验、动作条件模拟器与可执行策略混为一谈。zero-shot、实时、开源等说法需要结合具体版本与实验设置阅读。

页面仅在当前浏览器本地保存模型选择、阅读位置与测验状态，不发送分析数据。仓库与网页不包含部署凭据。
