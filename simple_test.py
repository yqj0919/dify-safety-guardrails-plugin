#!/usr/bin/env python3
"""
简单测试脚本 - 只测试参数接收逻辑
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.safety_guardrails import SafetyGuardrailsTool

def test_parameter_extraction():
    """测试参数提取逻辑"""
    print("🧪 测试参数提取逻辑")
    print("=" * 50)
    
    # 创建工具实例（不需要runtime和session）
    tool = SafetyGuardrailsTool()
    
    # 测试用例
    test_cases = [
        {"query": "sb"},
        {"query": ""},
        {"query": "   "},
        {"query": '"sb"'},
        {},
        {"other_param": "value"}
    ]
    
    for i, params in enumerate(test_cases, 1):
        print(f"\n🔍 测试 {i}: {params}")
        
        # 直接测试参数提取逻辑
        query = params.get("query", "").strip()
        print(f"   提取的query: '{query}' (长度: {len(query)})")
        
        if not query:
            print("   ❌ 结果: Query parameter is required")
        else:
            print("   ✅ 结果: Query参数有效，会继续处理")

if __name__ == "__main__":
    test_parameter_extraction()