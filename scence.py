from manim import *
import os
import math

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)

class ChineseExample(Scene):
    def construct(self):
        # 使用特定中文字体
        title = Text("动画演示", font="Microsoft YaHei", weight=BOLD)
        subtitle = Text("中文支持示例", font="Microsoft YaHei")
        
        # 使用默认字体（需在配置中设置）
        content = Text("这是一个使用Manim制作中文动画的示例")
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(subtitle.next_to(title, DOWN)))
        self.wait()
        self.play(Write(content))
        self.wait()



class AnimateCutieMarks(Scene):
    def construct(self):
        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        image_files = [
            "cutie-mark-aj.png",  # Apple Jack
            "cutie-mark-rd.png",  # Rainbow Dash
            "cutie-mark-ts.png",  # Twilight Sparkle
            "cutie-mark-rr.png",  # Rarity
            "cutie-mark-fs.png",  # Fluttershy
            "cutie-mark-pp.png"   # Pinkie Pie
        ]
        
        # 角色名字（可选）
        names = ["Apple Jack", "Rainbow Dash", "Twilight Sparkle", 
                "Rarity", "Fluttershy", "Pinkie Pie"]
        
        images = [ImageMobject(os.path.join(assets_dir, img)).scale(0.6) for img in image_files]
        texts = [Text(name, font_size=20).next_to(img, DOWN) for name, img in zip(names, images)]
        
        # 圆形排列
        radius = 2.5
        for i, (img, text) in enumerate(zip(images, texts)):
            angle = i * TAU/6
            position = [radius * np.cos(angle), radius * np.sin(angle), 0]
            img.move_to(position)
            text.move_to(position + DOWN*1.1)
        
        # 逐个显示动画
        for img, text in zip(images, texts):
            self.play(FadeIn(img), Write(text))
            self.wait(0.5)
        
        self.wait(2)

from manim import *
import os

class CorrectedDialogueFramework(Scene):
    def construct(self):
        # 1. 设置头像参数
        avatar_positions = [
            LEFT * 5.5 + UP * 2.5,   # 左上
            RIGHT * 5.5 + UP * 1.5,   # 右上
            LEFT * 5.5 + UP * 0.5,  # 左中
            RIGHT * 5.5 + DOWN * 0.5,  # 右中
            LEFT * 5.5 + DOWN * 1.5,  # 左下
            RIGHT * 5.5 + DOWN * 2.5  # 右下
        ]
        
        avatar_scale = 0.5
        avatar_files = [
            "cutie-mark-aj.png",
            "cutie-mark-rd.png",
            "cutie-mark-ts.png",
            "cutie-mark-pp.png",
            "cutie-mark-fs.png",
            "cutie-mark-rr.png"
        ]
        
        # 2. 加载头像并固定位置
        avatars = []
        for i, (pos, file) in enumerate(zip(avatar_positions, avatar_files)):
            # 添加圆形头像背景
            circle = Circle(radius=0.8, color=BLACK, fill_opacity=0)
            circle.move_to(pos)
            
            # 加载头像图片 - 使用Group而不是VGroup
            avatar = ImageMobject(os.path.join("assets", file))
            avatar.scale(avatar_scale).move_to(pos)
            
            # 关键修改：使用Group而不是VGroup
            group = Group(circle, avatar)
            avatars.append(group)
            self.add(group)
        
        # 3. 对话内容 (文本, 说话者索引, 持续时间)
        dialogues = [
            ("朋友们！欢迎来到我们的小马利亚友谊表演会！", 2, 2.5),
            ("耶！我最喜欢表演了！(兴奋地蹦跳)", 3, 2),
            ("*清嗓子* 今天我们要展示的是...", 2, 2),
            ("超——级——酷的闪电特技！", 1, 1.5),
            ("噢不...云宝，请别在我的苹果摊附近做特技...", 0, 2.5),
            ("放轻松，亲爱的~我们会保持优雅的", 5, 2),
            ("(小声)其实我有点紧张...", 4, 1.5),
            ("没关系的柔柔！友谊魔法会支持我们！", 2, 2),
            ("那还等什么？让我们开始派对吧！", 3, 2)   
        ]
                
        # ... [前面头像部分的代码保持不变] ...

        # 4. 显示对话（修改后的部分）
        current_bubble = None
        for text, speaker_idx, duration in dialogues:

            if current_bubble:
                self.play(FadeOut(current_bubble))
                self.remove(current_bubble)
            
            speaker_pos = avatar_positions[speaker_idx]
            
            # 计算对话框最大宽度（左右头像之间的空间）
            max_width = abs(avatar_positions[0][0] - avatar_positions[1][0]) - 2
            
            # 处理文本换行
            characters_per_line = 30  # 每行字符数
            # 将文本分割成多行
            processed_text  = '\n'.join([text[i:i+characters_per_line] for i in range(0, len(text), characters_per_line)])
            # 创建固定字体大小的文本（不再使用Paragraph）
            text_obj = Text(
                text=processed_text, 
                font_size=24,  # 保持固定字体大小
                font="Microsoft YaHei",
                color=BLACK,
                line_spacing=0.4,
                should_center=False,
                # width=max_width  # 设置最大宽度自动换行
            )

            # 确定文本位置（修改后的智能定位）
            if speaker_pos[0] < 0:  # 左侧头像
                text_obj.align_to(LEFT, LEFT)
                # 动态计算X位置：头像右侧 + 0.5缓冲 + 文本框一半宽度
                bubble_x = speaker_pos[0] + 1.0 + (min(text_obj.width, max_width)/2)
                bubble_pos = np.array([
                    min(bubble_x, (avatar_positions[0][0] + avatar_positions[1][0])/2),  # 不超过中间线
                    speaker_pos[1],
                    0
                ])
            else:  # 右侧头像
                text_obj.align_to(RIGHT, RIGHT)
                # 动态计算X位置：头像左侧 - 0.5缓冲 - 文本框一半宽度
                bubble_x = speaker_pos[0] - 1.0 - (min(text_obj.width, max_width)/2)
                bubble_pos = np.array([
                    max(bubble_x, (avatar_positions[0][0] + avatar_positions[1][0])/2),  # 不超过中间线
                    speaker_pos[1],
                    0
                ])

            # 创建背景框（保持原有高度计算）
            padding = 0.2
            line_height = 0.5
            line_count = math.ceil(len(text)/characters_per_line)  # 获取实际行数
            
            background = RoundedRectangle(
                width=min(text_obj.width + padding, max_width + padding),
                height=line_count * line_height + padding,
                corner_radius=0.2,
                fill_color=WHITE,
                fill_opacity=1,
                stroke_color=WHITE
            )
            background.move_to(bubble_pos)
            text_obj.move_to(bubble_pos)

            current_bubble = VGroup(background, text_obj)
            self.play(FadeIn(current_bubble))
            self.wait(duration)

        # 5. 清理当前对话框
                    
        if current_bubble:
            self.play(FadeOut(current_bubble))
        self.wait(1)
