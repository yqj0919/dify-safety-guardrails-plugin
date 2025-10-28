import requests
import json
from typing import Any, Dict, Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class SafetyGuardrailsTool(Tool):
    def __init__(self, **kwargs):
        """
        Initialize the Safety Guardrails Tool
        """
        super().__init__(**kwargs)
        # API endpoints - Updated with actual endpoints
        self.token_url = "https://safeai.shuanzhineng.com:8081/api/account/oauth2/token"
        self.audit_url = "https://safeai.shuanzhineng.com:8081/api/chat/audit"
    
    def get_access_token(self, username: str, password: str) -> str:
        """
        Get access token from the API
        
        Args:
            username: API username
            password: API password
            
        Returns:
            Access token string
            
        Raises:
            Exception: If token acquisition fails
        """
        token_data = {
            "username": username,
            "password": password
        }
        
        response = requests.post(
            self.token_url,
            data=token_data,  # 使用data而不是json
            timeout=10
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to get access token. Status: {response.status_code}")
        
        result = response.json()
        
        # API返回的token在details字段中
        access_token = None
        if result.get("details") and result["details"].get("access_token"):
            access_token = result["details"]["access_token"]
        elif result.get("access_token"):
            access_token = result.get("access_token")
        elif result.get("token"):
            access_token = result.get("token")
        elif result.get("accessToken"):
            access_token = result.get("accessToken")
        
        if not access_token:
            raise Exception(f"No access token in response: {result}")
        
        return access_token
    
    def audit_content(self, content: str, access_token: str) -> Dict[str, Any]:
        """
        Audit content using the Safety API
        
        Args:
            content: Content to audit
            access_token: Valid access token
            
        Returns:
            Audit result dictionary
            
        Raises:
            Exception: If audit fails
        """
        audit_data = {
            "content": content
        }
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            self.audit_url,
            json=audit_data,
            headers=headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Audit request failed. Status: {response.status_code}")
        
        return response.json()

    def _invoke(self, tool_parameters: Dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke the safety guardrails tool
        
        Args:
            tool_parameters: Tool parameters containing 'query'
            
        Yields:
            ToolInvokeMessage objects with audit results
        """
        print(f"🚀 PLUGIN INVOKED! Parameters: {tool_parameters}")
        
        try:
            # Get query parameter
            query = tool_parameters.get("query", "").strip()
            
            # Debug: print received parameters
            print(f"DEBUG: Received tool_parameters: {tool_parameters}")
            print(f"DEBUG: Extracted query: '{query}' (length: {len(query)})")
            
            if not query:
                print("❌ Query is empty, returning error")
                yield self.create_json_message({
                    "error": "Query parameter is required",
                    "status": "error"
                })
                return
            
            # Get credentials from runtime
            credentials = self.runtime.credentials
            api_username = credentials.get("api_username")
            api_password = credentials.get("api_password")
            
            if not api_username or not api_password:
                yield self.create_json_message({
                    "error": "API credentials not configured",
                    "status": "error"
                })
                return
            
            # Get access token
            access_token = self.get_access_token(api_username, api_password)
            
            # Perform content audit
            audit_result = self.audit_content(query, access_token)
            
            # Return structured result
            yield self.create_json_message({
                "status": "success",
                "query": query,
                "audit_result": audit_result,
                "message": "Content audit completed successfully"
            })
            
        except Exception as e:
            yield self.create_json_message({
                "error": str(e),
                "status": "error",
                "message": "Failed to perform safety audit"
            })
