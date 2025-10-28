# Privacy Policy

This Safety Guardrails plugin provides AI content auditing and security filtering services to protect against malicious attacks and ensure content compliance. Here's how your data is handled:

## Data Processing

- **Text Content Auditing**: Your text content is sent to the Safety Guardrails API service for security analysis and compliance checking
- **API Communication**: The plugin communicates with Safety Guardrails servers  to process content audit requests
- **Security Analysis**: Content is analyzed for prompt injection attacks, inappropriate content, policy violations, and sensitive information
- **Audit Results**: The service returns structured audit results including risk levels, violation details, and safety recommendations

## Data Storage

- **No Local Storage**: The plugin does not permanently store your text content or audit results locally
- **Temporary Processing**: All data processing is temporary and happens only during the content auditing process
- **Credential Security**: Your API username and password are stored securely within your Dify environment and are not logged or transmitted elsewhere
- **Session Management**: Access tokens are obtained dynamically and used only for the duration of the audit request

## Third-Party Services

- **Safety Guardrails API**: Your text content is sent to the Safety Guardrails service for security analysis
- **Network Communication**: The plugin requires internet connectivity to communicate with Safety Guardrails servers
- **Service Provider**: Safety Guardrails API service processes your requests according to their privacy policy
- **Authentication Service**: The plugin uses OAuth2 token-based authentication for secure API access

## Content Analysis Features

- **Prompt Injection Detection**: Content is analyzed for potential prompt injection attacks and malicious instructions
- **Content Value Review**: Text is evaluated against content policies and community guidelines
- **Sensitive Data Checking**: Content is scanned for personally identifiable information and sensitive data
- **Risk Assessment**: Each piece of content receives a risk level assessment with detailed explanations

## Data Retention

- The plugin does not retain any user content after audit completion
- Audit results are temporarily processed and immediately returned to your workflow
- No persistent storage of text content, audit results, or user information within the plugin
- Access tokens are discarded after each audit session

## Data Transmission

- Text content is transmitted securely over HTTPS to the Safety Guardrails API
- Audit results are returned securely over HTTPS
- All API communications use encrypted connections (TLS/SSL)
- Authentication credentials are transmitted using secure OAuth2 protocols
- No data is shared with any other third parties beyond the Safety Guardrails service

## User Control

- Users can control what content is submitted for auditing
- The plugin only processes content when explicitly invoked
- Users maintain full control over their API credentials and can revoke access at any time
- Audit results are returned directly to the user's workflow without intermediate storage
