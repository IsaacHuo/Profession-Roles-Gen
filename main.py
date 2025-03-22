# -*- coding: utf-8 -*-

import gradio as gr
import requests
import json
import time

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = "<Your API Key>"

TERMINOLOGY_DATABASES = {
    "翻译与跨文化沟通术语库": "推荐资源：中国特色话语对外翻译标准化术语库、联合国术语库(UNTERM)、中华思想文化术语库",
    "科技与工程术语库": "推荐资源：术语在线、微软术语库、SCIdict学术词库",
    "医学与生物医药术语库": "推荐资源：生物医学大词典、医学英语在线翻译词典、BiCovid术语库",
    "法律与司法术语库": "推荐资源：元照英美法词典、香港法律中英术语库",
    "金融与经济术语库": "推荐资源：MBA智库金融专业术语文档、中国核心词汇",
    "信息技术与计算机科学术语库": "推荐资源：微软术语库、行业职位术语库",
    "教育与职业能力术语库": "推荐资源：新版职业教育专业教学标准、BCC汉语语料库",
    "市场营销与管理术语库": "推荐资源：行业职位术语库、中国关键词",
    "建筑工程与制造业术语库": "推荐资源：MBA智库建筑工程术语文档、术语在线",
    "新兴行业与跨领域术语库": "推荐资源：Linguee术语库、互联网行业术语文档"
}

def generate_character_card(occupation, terminology_type, *aspect_values):
    selected_aspects = [aspect for aspect, value in zip(ASPECTS.keys(), aspect_values) if value]
    if not selected_aspects:
        return "请至少选择一个角色描述方面。"
    terminology_info = TERMINOLOGY_DATABASES.get(terminology_type, "")
    aspects_description = ""
    for i, aspect in enumerate(ASPECTS.keys(), 1):
        if aspect in selected_aspects:
            aspects_description += f"\n{i}. {aspect}\n"
            for detail in ASPECTS[aspect]:
                aspects_description += f"- {detail}\n"
    
    prompt = f"请创建{terminology_type}领域角色卡，要求：\n1. 职业：{occupation}\n2. 参考资源：{terminology_info}\n3. 按以下要点描述（600字）：\n{aspects_description}\n• 使用行业标准术语\n• 突出专业深度与特色\n• 结构清晰分段落"
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": f"你是一个专业的{terminology_type}领域专家，对该领域的专业术语、行业标准和最佳实践有深入的理解。你需要基于专业知识创建一个符合该领域特点的角色设定。请确保所有描述都符合行业规范，使用恰当的专业术语，呈现出角色在该领域的专业素养和特色。请注意保持描述的连贯性和逻辑性，同时突出角色的独特个性。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 1.4,
        "max_tokens": 7120,
        "stream": False
    }
    
    max_retries = 3
    retry_delay = 5
    timeout = 120
    
    # 前置网络检查
    try:
        requests.get('https://api.deepseek.com', timeout=5)
    except requests.exceptions.RequestException:
        return "生成失败：网络连接异常，请检查网络后重试"

    for attempt in range(max_retries):
        try:

            response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=timeout)
            response.raise_for_status()
            result = response.json()
            if not result.get('choices') or not result['choices'][0].get('message', {}).get('content'):
                return "生成失败：API返回数据格式异常"
            return result['choices'][0]['message']['content']
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return "生成失败：请求超时，请稍后重试"
        except requests.exceptions.RequestException as e:
            error_msg = f"生成失败：{str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_details = e.response.json()
                    if isinstance(error_details, dict) and 'error' in error_details:
                        error_msg += f"\n详细错误：{error_details['error']}"
                except (ValueError, AttributeError):
                    error_msg += "\n无法解析错误详情"
            return error_msg
        except json.JSONDecodeError:
            return "生成失败：API返回数据格式错误"
        except Exception as e:
            return f"生成失败：发生未知错误 - {str(e)}"

ASPECTS = {
    "专业背景": ["学历背景", "专业资质", "特殊成就", "行业见解"],
    "工作特征": ["专业技能", "工作方式", "问题处理方法"],
    "职业形象": ["穿着仪表", "行为礼仪", "气质特点"],
    "人际网络": ["人脉资源", "团队协作", "行业交流"],
    "价值观和职业操守": ["职业伦理", "发展规划", "行业责任"]
}

def create_interface():
    with gr.Blocks(theme=gr.themes.Soft()) as app:
        gr.Markdown("""
        # 🎭 AI角色卡生成器
        ## 创建专业且个性化的角色设定
        > 💡 Tips: 预计生成时间为40秒，您可以将生成的角色卡粘贴到其他AI模型对话框，使AI回复更加贴切、专业。
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                with gr.Column(scale=1):
                    with gr.Column(scale=1):
                        gr.Markdown("### 📝 基本信息")
                        occupation = gr.Textbox(
                            label="职业",
                            placeholder="请输入角色的职业，例如：软件工程师、医生、律师等",
                            container=True
                        )
                        terminology_type = gr.Dropdown(
                            choices=list(TERMINOLOGY_DATABASES.keys()),
                            label="专业领域",
                            value=list(TERMINOLOGY_DATABASES.keys())[0],
                            container=True
                        )
                
                with gr.Column(scale=1):
                    with gr.Column(scale=1):
                        gr.Markdown("### 🎯 角色描述方面")
                        gr.Markdown("选择您希望重点描述的方面：")
                        aspects = {}
                        for category, items in ASPECTS.items():
                            with gr.Row():
                                aspects[category] = gr.Checkbox(label=category, value=True)
                
                generate_btn = gr.Button("✨ 生成角色卡", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="生成结果",
                    lines=50,
                    show_copy_button=True
                )
        
        generate_btn.click(
            fn=generate_character_card,
            inputs=[occupation, terminology_type] + list(aspects.values()),
            outputs=output
        )
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(server_name="0.0.0.0", server_port=7860, share=True)