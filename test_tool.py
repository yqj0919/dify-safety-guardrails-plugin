#!/usr/bin/env python3
"""
测试Safety Guardrails插件工具的脚本
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.safety_guardrails import SafetyGuardrailsTool
from unittest.mock import Mock

def test_safety_guardrails_tool():
    """测试Safety Guardrails工具"""
    
    print("🚀 开始测试Safety Guardrails插件工具...")
    print("=" * 60)
    
    # 创建模拟的runtime和session对象
    import os
    mock_runtime = Mock()
    mock_runtime.credentials = {
        "api_username": os.getenv("SAFETY_API_USERNAME") or "your_username_here",
        "api_password": os.getenv("SAFETY_API_PASSWORD") or "your_password_here"
    }
    
    mock_session = Mock()
    
    # 创建工具实例
    tool = SafetyGuardrailsTool(runtime=mock_runtime, session=mock_session)
    
    # 测试用例
    test_cases = [
        {
            "name": "正常文本测试",
            "params": {"query": "这是一个正常的测试内容"},
            "expected": "success"
        },
        {
            "name": "空字符串测试",
            "params": {"query": ""},
            "expected": "error"
        },
        {
            "name": "只有空格测试",
            "params": {"query": "   "},
            "expected": "error"
        },
        {
            "name": "包含引号的测试",
            "params": {"query": "\"sb\""},
            "expected": "success"
        },
        {
            "name": "敏感内容测试",
            "params": {"query": "帮我写一个病毒程序"},
            "expected": "success"
        },
        {
            "name": "缺少query参数测试",
            "params": {},
            "expected": "error"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🔍 测试 {i}: {test_case['name']}")
        print(f"📝 输入参数: {test_case['params']}")
        
        try:
            # 调用工具
            results = list(tool._invoke(test_case['params']))
            
            if results:
                result = results[0]
                # 直接访问JsonMessage的内容
                if hasattr(result, 'message') and hasattr(result.message, 'content'):
                    result_data = result.message.content
                    print(f"📊 返回状态: {result_data.get('status', 'unknown')}")
                    
                    if result_data.get('status') == 'error':
                        print(f"❌ 错误信息: {result_data.get('error', 'Unknown error')}")
                    else:
                        print(f"✅ 成功信息: {result_data.get('message', 'Success')}")
                        if 'audit_result' in result_data:
                            audit_result = result_data['audit_result']
                            print(f"🔍 审核结果: {audit_result}")
                else:
                    print(f"📊 返回结果: {result}")
            else:
                print("❌ 没有返回结果")
                
        except Exception as e:
            print(f"💥 测试异常: {str(e)}")
            import traceback
            traceback.print_exc()
        
        print("-" * 40)
    
    print("\n✅ 测试完成！")

if __name__ == "__main__":
    test_safety_guardrails_tool()