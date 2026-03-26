"""
武学融合系统 - 龙游凌波掌
=========================

融合武学：
1. 降龙十八掌 - 刚猛霸道，掌力无双
2. 凌波微步 - 身法飘逸，步伐玄妙

创新武学：龙游凌波掌
- 融合降龙掌的刚猛掌力与凌波步的灵动身法
- 以柔克刚，刚柔并济
- 步随掌转，掌借步势
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from matplotlib.patheffects import withStroke
import matplotlib.patches as mpatches

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


class WugongFusion:
    """武功融合系统"""

    def __init__(self):
        self.wugong1 = {
            'name': '降龙十八掌',
            'type': '掌法',
            'power': 95,
            'agility': 30,
            'essence': '刚猛霸道',
            'color': '#e74c3c',
            'moves': ['亢龙有悔', '飞龙在天', '见龙在田', '潜龙勿用', '神龙摆尾']
        }

        self.wugong2 = {
            'name': '凌波微步',
            'type': '步法',
            'power': 25,
            'agility': 98,
            'essence': '轻灵飘逸',
            'color': '#3498db',
            'moves': ['踏雪无痕', '云中漫步', '水上飘', '穿花绕柳', '鬼影迷踪']
        }

        # 融合新武功
        self.new_wugong = self.fusion()

    def fusion(self):
        """融合两门武学"""
        w1 = self.wugong1
        w2 = self.wugong2

        return {
            'name': '龙游凌波掌',
            'type': '掌法+步法',
            'power': int((w1['power'] * 0.7 + w2['power'] * 0.3)),
            'agility': int((w1['agility'] * 0.3 + w2['agility'] * 0.7)),
            'essence': '刚柔并济，步掌合一',
            'color': '#9b59b6',
            'description': '融降龙掌之刚猛与凌波步之轻灵，刚柔并济，步随掌转，掌借步势。',
            'moves': [
                {'name': '游龙戏凤', 'desc': '身形如龙游云间，掌力蓄于步法之中，步到掌至', 'power': 75, 'agility': 85},
                {'name': '凌波震海', 'desc': '步踏凌波，掌震八方，以柔化刚，刚柔并济', 'power': 88, 'agility': 70},
                {'name': '云龙三现', 'desc': '身法连环，三掌叠加，虚实难辨，掌掌致命', 'power': 82, 'agility': 90},
                {'name': '踏浪惊龙', 'desc': '步踏浪花，龙吟九天，掌力随步而涨，势不可挡', 'power': 92, 'agility': 78},
                {'name': '微步亢龙', 'desc': '融凌波微步与亢龙有悔，退中有进，守中带攻', 'power': 85, 'agility': 88},
                {'name': '龙影千幻', 'desc': '身化千影，掌分八方，真真假假，虚虚实实', 'power': 70, 'agility': 95},
            ]
        }

    def visualize_fusion_process(self):
        """可视化武功融合过程"""
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
        fig.patch.set_facecolor('#f8f9fa')

        # 武功1 - 降龙十八掌
        self._draw_wugong(ax1, self.wugong1, position='left')

        # 武功2 - 凌波微步
        self._draw_wugong(ax2, self.wugong2, position='right')

        # 融合后的新武功
        self._draw_new_wugong(ax3, self.new_wugong)

        plt.tight_layout()
        plt.savefig('wugong_fusion_process.png', dpi=200, bbox_inches='tight', facecolor='#f8f9fa')
        print("✅ 武功融合过程图已保存: wugong_fusion_process.png")
        plt.show()

    def _draw_wugong(self, ax, wugong, position):
        """绘制单个武功"""
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#ffffff')

        # 标题
        ax.text(5, 9, wugong['name'], fontsize=20, fontweight='bold',
               ha='center', color=wugong['color'])

        # 类型
        ax.text(5, 8.2, f"[{wugong['type']}]", fontsize=14,
               ha='center', color='#7f8c8d', style='italic')

        # 雷达图数据
        categories = ['威力', '敏捷']
        values = [wugong['power'], wugong['agility']]

        # 绘制能力条
        y_pos = 7
        bar_width = 6
        for i, (cat, val) in enumerate(zip(categories, values)):
            ax.text(2, y_pos - i*0.8, f"{cat}:", fontsize=12, fontweight='bold')

            # 背景条
            rect_bg = FancyBboxPatch((3, y_pos - i*0.8 - 0.2), bar_width, 0.4,
                                     boxstyle="round,pad=0.05",
                                     facecolor='#ecf0f1', edgecolor='none')
            ax.add_patch(rect_bg)

            # 数值条
            rect = FancyBboxPatch((3, y_pos - i*0.8 - 0.2), bar_width * val/100, 0.4,
                                 boxstyle="round,pad=0.05",
                                 facecolor=wugong['color'], edgecolor='none', alpha=0.8)
            ax.add_patch(rect)

            # 数值
            ax.text(9.2, y_pos - i*0.8, f"{val}", fontsize=11, fontweight='bold',
                   color=wugong['color'])

        # 精髓
        ax.text(5, 5, f"精髓：{wugong['essence']}", fontsize=13,
               ha='center', style='italic',
               bbox=dict(boxstyle='round,pad=0.8', facecolor='#fff3cd',
                        edgecolor=wugong['color'], linewidth=2))

        # 招式列表
        ax.text(5, 3.8, "代表招式", fontsize=12, ha='center', fontweight='bold')
        for i, move in enumerate(wugong['moves'][:3]):
            ax.text(5, 3.2 - i*0.5, f"• {move}", fontsize=10,
                   ha='center', color='#2c3e50')

    def _draw_new_wugong(self, ax, wugong):
        """绘制融合后的新武功"""
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#ffffff')

        # 光芒效果
        circle = Circle((5, 7), 2.5, color=wugong['color'], alpha=0.1)
        ax.add_patch(circle)
        circle2 = Circle((5, 7), 2, color=wugong['color'], alpha=0.15)
        ax.add_patch(circle2)

        # 标题
        title = ax.text(5, 9.2, '✨ ' + wugong['name'] + ' ✨', fontsize=22, fontweight='bold',
                       ha='center', color=wugong['color'])
        title.set_path_effects([withStroke(linewidth=3, foreground='white')])

        # 类型
        ax.text(5, 8.5, f"[{wugong['type']}]", fontsize=14,
               ha='center', color='#7f8c8d', style='italic')

        # 能力值
        categories = ['威力', '敏捷']
        values = [wugong['power'], wugong['agility']]

        y_pos = 5.5
        bar_width = 6
        for i, (cat, val) in enumerate(zip(categories, values)):
            ax.text(2, y_pos - i*0.8, f"{cat}:", fontsize=12, fontweight='bold')

            # 背景条
            rect_bg = FancyBboxPatch((3, y_pos - i*0.8 - 0.2), bar_width, 0.4,
                                     boxstyle="round,pad=0.05",
                                     facecolor='#ecf0f1', edgecolor='none')
            ax.add_patch(rect_bg)

            # 渐变效果的数值条
            rect = FancyBboxPatch((3, y_pos - i*0.8 - 0.2), bar_width * val/100, 0.4,
                                 boxstyle="round,pad=0.05",
                                 facecolor=wugong['color'], edgecolor='#7f8c8d',
                                 linewidth=1.5, alpha=0.9)
            ax.add_patch(rect)

            # 数值
            ax.text(9.2, y_pos - i*0.8, f"{val}", fontsize=12, fontweight='bold',
                   color=wugong['color'])

        # 精髓
        ax.text(5, 3.2, f"精髓：{wugong['essence']}", fontsize=13,
               ha='center', style='italic', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.8', facecolor='#fff3cd',
                        edgecolor=wugong['color'], linewidth=2.5))

        # 说明
        ax.text(5, 2.2, wugong['description'], fontsize=10,
               ha='center', color='#34495e', wrap=True)

    def visualize_moves(self):
        """可视化招式图解"""
        moves = self.new_wugong['moves']

        # 创建3x2的子图
        fig = plt.figure(figsize=(16, 20))
        fig.patch.set_facecolor('#f8f9fa')
        fig.suptitle('🐉 龙游凌波掌 - 六式图解 🐉',
                    fontsize=24, fontweight='bold', y=0.98, color='#9b59b6')

        for idx, move in enumerate(moves):
            ax = plt.subplot(3, 2, idx + 1)
            self._draw_move(ax, move, idx + 1)

        plt.tight_layout(rect=[0, 0, 1, 0.97])
        plt.savefig('wugong_moves.png', dpi=200, bbox_inches='tight', facecolor='#f8f9fa')
        print("✅ 招式图解已保存: wugong_moves.png")
        plt.show()

    def _draw_move(self, ax, move, move_num):
        """绘制单个招式"""
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#ffffff')

        # 招式名称
        ax.text(0, 4.5, f"第{move_num}式：{move['name']}",
               fontsize=16, fontweight='bold', ha='center', color='#9b59b6')

        # 招式描述
        ax.text(0, 3.8, move['desc'], fontsize=10, ha='center',
               color='#7f8c8d', wrap=True, style='italic')

        # 根据不同招式绘制不同的运行轨迹
        self._draw_move_pattern(ax, move_num, move)

        # 能力标签
        power_text = f"威力: {'⚡' * int(move['power']/20)}"
        agility_text = f"敏捷: {'💨' * int(move['agility']/20)}"

        ax.text(0, -4.2, power_text, fontsize=10, ha='center', color='#e74c3c')
        ax.text(0, -4.6, agility_text, fontsize=10, ha='center', color='#3498db')

    def _draw_move_pattern(self, ax, move_num, move):
        """绘制招式运行轨迹图案"""

        if move_num == 1:  # 游龙戏凤 - S形曲线
            t = np.linspace(0, 4*np.pi, 100)
            x = 3 * np.sin(t/2)
            y = 3 * np.cos(t/2) * np.sin(t/4)
            ax.plot(x, y, color='#9b59b6', linewidth=3, alpha=0.6)
            ax.scatter([x[0]], [y[0]], s=200, color='#2ecc71', zorder=5, marker='o', edgecolors='black', linewidth=2)
            ax.scatter([x[-1]], [y[-1]], s=200, color='#e74c3c', zorder=5, marker='*', edgecolors='black', linewidth=2)

        elif move_num == 2:  # 凌波震海 - 波浪形
            t = np.linspace(-np.pi, np.pi, 100)
            for i in range(3):
                y = i - 1
                x = t
                ax.plot(x, y + 0.3*np.sin(3*x), color='#3498db', linewidth=2.5, alpha=0.7-i*0.2)
            # 掌印
            circle = Circle((0, 0), 1.5, color='#e74c3c', alpha=0.3)
            ax.add_patch(circle)
            ax.text(0, 0, '掌', fontsize=30, ha='center', va='center',
                   color='#e74c3c', fontweight='bold')

        elif move_num == 3:  # 云龙三现 - 三个圆形轨迹
            for i, angle in enumerate([0, 120, 240]):
                theta = np.linspace(0, 2*np.pi, 50)
                r = 1.5
                center_x = 2 * np.cos(np.radians(angle))
                center_y = 2 * np.sin(np.radians(angle))
                x = center_x + r * np.cos(theta)
                y = center_y + r * np.sin(theta)
                ax.plot(x, y, color='#9b59b6', linewidth=2.5, alpha=0.7)
                ax.scatter([center_x], [center_y], s=300, color='#e74c3c',
                          alpha=0.5, zorder=5, marker='o')
                ax.text(center_x, center_y, str(i+1), fontsize=16,
                       ha='center', va='center', color='white', fontweight='bold')

        elif move_num == 4:  # 踏浪惊龙 - 之字形上升
            points_x = [-3, -1, 1, 3]
            points_y = [-2, 0, 0.5, 2.5]

            for i in range(len(points_x)-1):
                arrow = FancyArrowPatch((points_x[i], points_y[i]),
                                       (points_x[i+1], points_y[i+1]),
                                       arrowstyle='->', mutation_scale=30,
                                       linewidth=3, color='#3498db', alpha=0.7)
                ax.add_patch(arrow)

                # 脚印
                circle = Circle((points_x[i], points_y[i]), 0.3,
                              color='#2ecc71', alpha=0.6)
                ax.add_patch(circle)

            # 最后的龙形
            ax.text(3, 3.5, '🐉', fontsize=40, ha='center')

        elif move_num == 5:  # 微步亢龙 - 八卦图案
            # 八卦阵
            for i in range(8):
                angle = i * 45
                x1 = 2.5 * np.cos(np.radians(angle))
                y1 = 2.5 * np.sin(np.radians(angle))
                x2 = 1.2 * np.cos(np.radians(angle))
                y2 = 1.2 * np.sin(np.radians(angle))

                ax.plot([x1, x2], [y1, y2], color='#9b59b6', linewidth=2, alpha=0.6)
                circle = Circle((x1, y1), 0.3, color='#3498db', alpha=0.7)
                ax.add_patch(circle)

            # 中心圆
            circle_center = Circle((0, 0), 1, color='#e74c3c', alpha=0.4)
            ax.add_patch(circle_center)
            ax.text(0, 0, '龙', fontsize=24, ha='center', va='center',
                   color='white', fontweight='bold')

        elif move_num == 6:  # 龙影千幻 - 多重影像
            # 创建放射状的影子效果
            for i in range(12):
                angle = i * 30
                distance = 2.5
                x = distance * np.cos(np.radians(angle))
                y = distance * np.sin(np.radians(angle))

                alpha = 1 - i/12
                circle = Circle((x, y), 0.5, color='#9b59b6', alpha=alpha*0.5)
                ax.add_patch(circle)

                # 连线
                ax.plot([0, x], [0, y], color='#3498db',
                       linewidth=1, alpha=alpha*0.3, linestyle='--')

            # 中心真身
            circle_center = Circle((0, 0), 0.7, color='#e74c3c', alpha=0.8,
                                  edgecolor='#9b59b6', linewidth=3)
            ax.add_patch(circle_center)
            ax.text(0, 0, '真', fontsize=18, ha='center', va='center',
                   color='white', fontweight='bold')

    def generate_manual(self):
        """生成武功秘籍文本"""
        print("\n" + "="*60)
        print(" "*15 + "🐉 龙游凌波掌秘籍 🐉")
        print("="*60)
        print(f"\n【武学名称】{self.new_wugong['name']}")
        print(f"【武学类型】{self.new_wugong['type']}")
        print(f"【融合武学】{self.wugong1['name']} + {self.wugong2['name']}")
        print(f"【武学精髓】{self.new_wugong['essence']}")
        print(f"\n【武学说明】")
        print(f"  {self.new_wugong['description']}")
        print(f"\n【能力评估】")
        print(f"  威力: {self.new_wugong['power']}/100  {'█' * (self.new_wugong['power']//5)}")
        print(f"  敏捷: {self.new_wugong['agility']}/100  {'█' * (self.new_wugong['agility']//5)}")

        print(f"\n【六式详解】")
        print("-"*60)
        for i, move in enumerate(self.new_wugong['moves'], 1):
            print(f"\n第{i}式：{move['name']}")
            print(f"  心法：{move['desc']}")
            print(f"  威力：{move['power']}/100  敏捷：{move['agility']}/100")

        print("\n" + "="*60)
        print("  习此功法者，需内外兼修，刚柔并济，方可大成！")
        print("="*60 + "\n")


def main():
    """主函数"""
    print("🥋 开始融合武学...")
    print()

    # 创建武功融合系统
    fusion = WugongFusion()

    # 生成文字秘籍
    fusion.generate_manual()

    # 生成融合过程可视化
    print("📊 生成武功融合过程图...")
    fusion.visualize_fusion_process()

    # 生成招式图解
    print("📖 生成招式图解...")
    fusion.visualize_moves()

    print("\n✅ 武功秘籍创作完成！")
    print("   - wugong_fusion_process.png (融合过程图)")
    print("   - wugong_moves.png (招式图解)")


if __name__ == "__main__":
    main()
