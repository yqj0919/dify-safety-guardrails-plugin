# Safety Guardrails Plugin / 安全护栏插件

[English](#english) | [中文](#中文)

---

## English

### Overview

The Safety Guardrails plugin is an AI content auditing and security filtering system designed to protect against malicious attacks and ensure generated content is safe and compliant. This external protection system provides pre-filtering and post-filtering capabilities without requiring modifications to the underlying AI models.

### Features

- **Prompt Injection Detection**: Identifies and blocks potential prompt injection attacks and malicious instructions
- **Content Value Review**: Evaluates text against content policies and community guidelines
- **Sensitive Data Checking**: Scans content for personally identifiable information and sensitive data
- **Risk Assessment**: Provides detailed risk level assessments with explanations and recommendations
- **Real-time Auditing**: Processes content in real-time with immediate feedback
- **Multi-language Support**: Supports content auditing in multiple languages

### Installation

1. Install the plugin in your Dify environment
2. Configure your API credentials (username and password)
3. Add the Safety Guardrails tool to your workflow

### Configuration

The plugin requires the following credentials:

- **API Username**: Your Safety Guardrails API username
- **API Password**: Your Safety Guardrails API password

These credentials are securely stored in your Dify environment and used for OAuth2 authentication.

### Usage

1. Add the Safety Guardrails tool to your Dify workflow
2. Configure the tool with your API credentials
3. Input the text content you want to audit in the `query` parameter
4. The tool will return a structured audit result including:
   - Risk level assessment
   - Violation details (if any)
   - Safety recommendations
   - Compliance status

### API Endpoints

- **Token Endpoint**: `https://safeai.shuanzhineng.com:8081/api/account/oauth2/token`
- **Audit Endpoint**: `https://safeai.shuanzhineng.com:8081/api/chat/audit`

### Requirements

- Python 3.12+
- Dify Plugin SDK 0.4.0+
- Internet connectivity for API communication

### Privacy & Security

- No local storage of user content
- Secure HTTPS/TLS communication
- OAuth2 token-based authentication
- Temporary processing only
- No data sharing with third parties

### Author

**yuanquanjiang**

### Version

0.0.1

### License

Please refer to the project license file for licensing information.

---

## 中文

### 概述

安全护栏插件是一个AI内容审核和安全过滤系统，旨在防御恶意攻击并确保生成内容的安全合规。这个外部防护系统提供前置审核与后置过滤功能，无需修改底层AI模型。

### 功能特性

- **提示词注入检测**: 识别并阻止潜在的提示词注入攻击和恶意指令
- **内容价值观审核**: 根据内容政策和社区准则评估文本内容
- **敏感数据检查**: 扫描内容中的个人身份信息和敏感数据
- **风险评估**: 提供详细的风险等级评估，包含解释和建议
- **实时审核**: 实时处理内容并提供即时反馈
- **多语言支持**: 支持多种语言的内容审核

### 安装

1. 在您的Dify环境中安装插件
2. 配置您的API凭据（用户名和密码）
3. 将安全护栏工具添加到您的工作流中

### 配置

插件需要以下凭据：

- **API用户名**: 您的安全护栏API用户名
- **API密码**: 您的安全护栏API密码

这些凭据安全存储在您的Dify环境中，用于OAuth2身份验证。

### 使用方法

1. 将安全护栏工具添加到您的Dify工作流中
2. 使用您的API凭据配置工具
3. 在`query`参数中输入要审核的文本内容
4. 工具将返回结构化的审核结果，包括：
   - 风险等级评估
   - 违规详情（如有）
   - 安全建议
   - 合规状态

### API端点

- **令牌端点**: `https://safeai.shuanzhineng.com:8081/api/account/oauth2/token`
- **审核端点**: `https://safeai.shuanzhineng.com:8081/api/chat/audit`

### 系统要求

- Python 3.12+
- Dify插件SDK 0.4.0+
- 用于API通信的网络连接

### 隐私与安全

- 不本地存储用户内容
- 安全的HTTPS/TLS通信
- 基于OAuth2令牌的身份验证
- 仅临时处理数据
- 不与第三方共享数据

### 作者

**yuanquanjiang**

### 版本

0.0.1

### 许可证

请参考项目许可证文件了解许可信息。



