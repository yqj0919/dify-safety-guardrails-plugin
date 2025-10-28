#!/usr/bin/env python3
"""
测试脚本：直接测试Safety Guardrails API端点
用于调试API响应格式和token字段名称
"""

import requests
import json

def test_token_endpoint():
    """测试token获取端点"""
    print("🔍 测试Token获取端点...")
    
    token_url = "https://safeai.shuanzhineng.com:8081/api/account/oauth2/token"
    
    # 测试凭据 - 请替换为实际的API凭据
    credentials = {
        "username": "your_username_here",
        "password": "your_password_here"
    }
    
    print(f"📡 请求URL: {token_url}")
    print(f"📝 请求数据: {credentials}")
    
    try:
        # 使用form-data格式发送请求
        response = requests.post(
            token_url,
            data=credentials,
            timeout=10
        )
        
        print(f"📊 响应状态码: {response.status_code}")
        print(f"📋 响应头: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                result = response.json()
                print(f"✅ 响应JSON: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
                # 检查各种可能的token字段
                token_fields = ["access_token", "token", "accessToken", "access-token", "authToken"]
                found_token = None
                
                # 首先检查details字段中的token
                if "details" in result and isinstance(result["details"], dict):
                    for field in token_fields:
                        if field in result["details"]:
                            found_token = result["details"][field]
                            print(f"🎯 在details中找到token字段: '{field}' = '{found_token[:50]}...'")
                            break
                
                # 如果details中没找到，再检查根级别
                if not found_token:
                    for field in token_fields:
                        if field in result:
                            found_token = result[field]
                            print(f"🎯 在根级别找到token字段: '{field}' = '{found_token[:50]}...'")
                            break
                
                if not found_token:
                    print("❌ 未找到任何token字段")
                    print(f"📋 根级别字段: {list(result.keys())}")
                    if "details" in result:
                        print(f"📋 details字段: {list(result['details'].keys())}")
                else:
                    print("✅ Token获取成功！")
                
            except json.JSONDecodeError as e:
                print(f"❌ JSON解析失败: {e}")
                print(f"📄 原始响应: {response.text}")
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
            try:
                error_detail = response.json()
                print(f"📄 错误详情: {json.dumps(error_detail, indent=2, ensure_ascii=False)}")
            except:
                print(f"📄 原始错误响应: {response.text}")
                
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误: {e}")

def test_audit_endpoint():
    """测试内容审核端点（需要先获取token）"""
    print("\n🔍 测试内容审核端点...")
    
    # 这里可以添加审核端点的测试
    audit_url = "https://safeai.shuanzhineng.com:8081/api/chat/audit"
    print(f"📡 审核URL: {audit_url}")
    print("ℹ️  需要先获取有效token才能测试此端点")

if __name__ == "__main__":
    print("🚀 开始测试Safety Guardrails API...")
    print("=" * 50)
    
    test_token_endpoint()
    test_audit_endpoint()
    
    print("\n" + "=" * 50)
    print("✅ 测试完成！")




