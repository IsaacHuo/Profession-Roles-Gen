[English Version](#english) | [中文版本](#chinese)

<a name="english"></a>

# AI Role Card Generator

A professional role card generation tool based on DeepSeek API that creates detailed character settings according to profession and specialized fields.

## Features

- Support role card generation for multiple professional fields
- Customizable role description aspects
- Professional terminology database ensures content accuracy
- User-friendly graphical interface

## Installation

1. Ensure Python 3.x is installed
2. Clone or download this project locally
3. Run the following command in the project directory to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Usage

### Windows
Double-click `start.bat` file

### macOS/Linux
Run in terminal:
```bash
chmod +x start.sh  # Only needed for first run
./start.sh
```

## API Configuration

This project uses DeepSeek API to generate role card content. You need to:

1. Visit [DeepSeek Platform](https://platform.deepseek.com/) to register an account
2. Get API key from personal settings page
3. Open `main.py` file, locate the following code line:
   ```python
   # Configure API key here
   DEEPSEEK_API_KEY = "your-api-key-here"  # Replace with your actual key
   ```
4. Replace the content in quotes with your API key

## Important Notes

- Keep your API key secure and do not share it with others
- Ensure your computer is connected to the internet when running the program
- Role card generation may take 30-40 seconds, please be patient

## FAQ

### Q: Program fails to start with "Python environment not detected"
A: Please ensure Python 3.x is properly installed and added to system environment variables.

### Q: Failed to install dependencies
A: Try using the following command:
```bash
pip3 install -r requirements.txt --user
```

### Q: API error when generating role card
A: Please check:
1. API key is correctly configured
2. Network connection is normal
3. API balance is sufficient

## Terminology Database Guide

### Introduction to Terminology Databases

The project includes terminology databases for 10 professional fields. Each database contains:
- Authoritative reference resources
- Standard terminology collections
- Industry-specific vocabulary

### Database Selection Guidelines

1. **Translation & Cross-cultural Communication**
   - Suitable for: Translators, Foreign Affairs, Cultural Communication
   - Features: China-specific discourse, UN standard terminology

2. **Science & Engineering**
   - Suitable for: Engineers, Researchers, Technical Experts
   - Features: Academic vocabulary, Engineering standards

3. **Medical & Biomedical**
   - Suitable for: Doctors, Pharmacists, Biological Researchers
   - Features: Professional medical terms, Latest pharmaceutical vocabulary

4. **Legal & Judicial**
   - Suitable for: Lawyers, Legal Affairs, Judicial Workers
   - Features: Legal professional vocabulary, Judicial procedure terminology

5. **Finance & Economics**
   - Suitable for: Financial Analysts, Economists, Investment Advisors
   - Features: Financial market terminology, Economic indicator vocabulary

6. **IT & Computer Science**
   - Suitable for: Programmers, System Architects, IT Experts
   - Features: Technical framework terminology, Programming language vocabulary

7. **Education & Professional Competency**
   - Suitable for: Teachers, Trainers, Education Workers
   - Features: Education standard terminology, Competency assessment vocabulary

8. **Marketing & Management**
   - Suitable for: Marketing Managers, Brand Directors, Management Consultants
   - Features: Marketing strategy terminology, Management theory vocabulary

9. **Architecture & Manufacturing**
   - Suitable for: Architects, Engineers, Manufacturing Experts
   - Features: Engineering standard terminology, Manufacturing process vocabulary

10. **Emerging Industries & Cross-domain**
    - Suitable for: Innovators, Cross-domain Talents
    - Features: Emerging technology terminology, Cross-domain professional vocabulary

### Usage Tips

1. **Selecting Appropriate Database**
   - Choose based on primary job responsibilities
   - Reference multiple related field databases when needed
   - Consider cross-domain terminology support for new professions

2. **Optimizing Generation Results**
   - Use standard vocabulary from the database
   - Reference recommended authoritative sources
   - Ensure accurate and standard use of professional terms

## Model Parameter Configuration

### Temperature Setting

The Temperature parameter controls the creativity and randomness of generated content, with a default value of 1.0. Here are recommended settings for different scenarios:

| Use Case | Recommended Temperature |
|----------|----------------------|
| Code Generation/Math Problems | 0.0 |
| Data Extraction/Analysis | 1.0 |
| General Conversation | 1.3 |
| Translation | 1.3 |
| Creative Writing/Poetry | 1.5 |

You can modify the Temperature parameter in `main.py` file:
```python
TEMPERATURE = 1.0  # Adjust this value as needed
```

### Switching AI Models

This project supports multiple AI models that you can switch between as needed:

1. **OpenAI Model**
   - Get OpenAI API key: Visit [OpenAI Platform](https://platform.openai.com)
   - Change model provider to OpenAI in `main.py`:
     ```python
     MODEL_PROVIDER = "openai"
     OPENAI_API_KEY = "your-api-key"
     ```

2. **Google Gemini**
   - Get Gemini API key: Visit [Google AI Studio](https://makersuite.google.com)
   - Configure Gemini:
     ```python
     MODEL_PROVIDER = "gemini"
     GEMINI_API_KEY = "your-api-key"
     ```

3. **Anthropic Claude**
   - Get Claude API key: Visit [Anthropic Console](https://console.anthropic.com)
   - Configure Claude:
     ```python
     MODEL_PROVIDER = "claude"
     CLAUDE_API_KEY = "your-api-key"
     ```

## Technical Support

### 中文文档

<a name="chinese"></a>

# AI角色卡生成器

一个基于DeepSeek API的专业角色卡生成工具，可以根据职业和专业领域生成详细的角色设定。

## 功能特点

- 支持多个专业领域的角色卡生成
- 可自定义角色描述方面
- 使用专业术语库确保生成内容的专业性
- 简单易用的图形界面

## 安装步骤

1. 确保已安装Python 3.x版本
2. 克隆或下载本项目到本地
3. 在项目目录中运行以下命令安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 使用方法

### Windows
双击运行`start.bat`文件

### macOS/Linux
在终端中运行：
```bash
chmod +x start.sh  # 只需要第一次运行时执行
./start.sh
```

## API配置说明

本项目使用DeepSeek API生成角色卡内容。您需要：

1. 访问[DeepSeek官网](https://platform.deepseek.com/)注册账号
2. 在个人设置页面获取API密钥
3. 打开`main.py`文件，找到以下代码行：
   ```python
   # Configure API key here
   DEEPSEEK_API_KEY = "your-api-key-here"  # Replace with your actual key
   ```
4. 将引号中的内容替换为您的API密钥

## 注意事项

- 请妥善保管您的API密钥，不要分享给他人
- 确保运行程序时电脑已连接到互联网
- 生成角色卡可能需要30-40秒，请耐心等待

## 常见问题

### Q: 程序启动失败，提示"未检测到Python环境"
A: 请确保已正确安装Python 3.x版本，并将Python添加到系统环境变量中。

### Q: 安装依赖包失败
A: 尝试使用以下命令：
```bash
pip3 install -r requirements.txt --user
```

### Q: 生成角色卡时提示API错误
A: 请检查：
1. API密钥是否正确配置
2. 网络连接是否正常
3. API余额是否充足

## Prompt优化指南

### 职业描述优化

在输入职业时，建议：
- 提供具体的职业方向，如"前端开发工程师"比"程序员"更好
- 可以加入行业背景，如"互联网公司产品经理"
- 可以指明职级/年资，如"高级财务分析师"

### 专业领域选择

选择专业领域时注意：
- 选择最贴近职业的主要领域
- 对于跨领域职业，可以参考新兴行业术语库
- 确保选择的领域与职业描述相匹配

### 角色描述方面

根据不同职业特点，重点选择：
- 技术类职业：重点选择专业背景、工作特征
- 管理类职业：侧重人际网络、价值观和职业操守
- 创意类职业：可以突出职业形象、工作特征

## 术语库使用指南

### 术语库简介

本项目内置了10个专业领域的术语库，每个术语库都包含：
- 权威参考资源
- 标准术语集合
- 行业专业词汇

### 术语库选择建议

1. **翻译与跨文化沟通术语库**
   - 适用于：翻译、外事、文化传播等职业
   - 特色：中国特色话语、联合国标准术语

2. **科技与工程术语库**
   - 适用于：工程师、研究员、技术专家
   - 特色：学术词汇、工程标准术语

3. **医学与生物医药术语库**
   - 适用于：医生、药剂师、生物研究员
   - 特色：专业医学术语、最新医药词汇

4. **法律与司法术语库**
   - 适用于：律师、法务、司法工作者
   - 特色：法律专业词汇、司法程序术语

5. **金融与经济术语库**
   - 适用于：金融分析师、经济学家、投资顾问
   - 特色：金融市场术语、经济指标词汇

6. **信息技术与计算机科学术语库**
   - 适用于：程序员、系统架构师、IT专家
   - 特色：技术框架术语、编程语言词汇

7. **教育与职业能力术语库**
   - 适用于：教师、培训师、教育工作者
   - 特色：教育标准术语、能力评估词汇

8. **市场营销与管理术语库**
   - 适用于：市场经理、品牌主管、管理咨询师
   - 特色：营销策略术语、管理理论词汇

9. **建筑工程与制造业术语库**
   - 适用于：建筑师、工程师、制造业专家
   - 特色：工程标准术语、制造工艺词汇

10. **新兴行业与跨领域术语库**
    - 适用于：创新创业者、跨界人才
    - 特色：新兴技术术语、跨领域专业词汇

### 术语库使用技巧

1. **选择合适的术语库**
   - 根据职业主要工作内容选择
   - 可以参考多个相关领域的术语库
   - 注意新职业可能需要跨领域术语支持

2. **优化生成效果**
   - 使用术语库中的标准词汇描述职业
   - 参考术语库推荐的权威资源
   - 确保专业术语使用准确规范

## 模型参数配置

### Temperature参数设置

Temperature参数用于控制生成内容的创造性和随机性，默认值为1.0。以下是不同场景的推荐设置：

| Use Case | Recommended Temperature |
|---------|----------------|
| 代码生成/数学解题 | 0.0 |
| 数据抽取/分析 | 1.0 |
| 通用对话 | 1.3 |
| 翻译 | 1.3 |
| 创意类写作/诗歌创作 | 1.5 |

您可以在`main.py`文件中修改Temperature参数：
```python
TEMPERATURE = 1.0  # 根据需要调整此值
```

### 切换AI模型

本项目支持多种AI模型，您可以根据需要切换使用：

1. **OpenAI模型**
   - 获取OpenAI API密钥：访问[OpenAI平台](https://platform.openai.com)
   - 在`main.py`中将模型提供商改为OpenAI：
     ```python
     MODEL_PROVIDER = "openai"
     OPENAI_API_KEY = "your-api-key"
     ```

2. **Google Gemini**
   - 获取Gemini API密钥：访问[Google AI Studio](https://makersuite.google
