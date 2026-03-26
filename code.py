"""
大侠内力恢复模拟

规则：
1. 打坐每小时恢复总内力的 10%
2. 吃一个馒头恢复剩余空虚内力的 10%
3. 每个馒头需要 2 小时消化
"""

import matplotlib.pyplot as plt
import numpy as np

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def simulate_neili_recovery(max_neili=100, show_plot=True):
    """
    模拟内力恢复过程

    Args:
        max_neili: 最大内力值
        show_plot: 是否显示图表

    Returns:
        total_time: 恢复到满值的总时间（小时）
        mantou_count: 吃的馒头数量
        time_points: 时间点列表
        neili_points: 内力值列表
        events: 事件列表（打坐/吃馒头）
    """
    # 初始状态：内力耗尽，设为1%避免完全0无法计算
    current_neili = 1.0
    total_neili = max_neili

    time = 0.0
    mantou_count = 0
    mantou_digesting = 0  # 剩余消化时间

    # 记录数据用于绘图
    time_points = [time]
    neili_points = [current_neili]
    events = [(time, "开始", 1.0)]

    # 模拟时间步长（小时）
    dt = 0.01

    while current_neili < total_neili - 0.1:  # 接近满值就停止
        # 打坐恢复：每小时恢复总内力的10%
        recovery_per_hour = total_neili * 0.1
        recovery = recovery_per_hour * dt
        current_neili += recovery
        time += dt

        # 消化馒头
        if mantou_digesting > 0:
            mantou_digesting -= dt
            if mantou_digesting < 0:
                mantou_digesting = 0

        # 判断是否应该吃馒头
        # 策略：只要馒头消化完了，并且还有空虚内力，就吃馒头
        # 因为吃馒头是立即恢复，对总时间没有负面影响
        if mantou_digesting <= 0 and current_neili < total_neili - 0.5:
            # 剩余空虚内力
            empty_neili = total_neili - current_neili
            # 吃一个馒头能恢复的量
            mantou_recovery = empty_neili * 0.1

            # 吃馒头
            mantou_count += 1
            current_neili += mantou_recovery
            mantou_digesting = 2.0  # 开始消化
            events.append((time, f"吃馒头#{mantou_count}", current_neili))

        # 确保不超过最大值
        current_neili = min(current_neili, total_neili)

        # 记录数据（每0.1小时记录一次，减少数据量）
        if len(time_points) == 0 or time - time_points[-1] >= 0.1:
            time_points.append(time)
            neili_points.append(current_neili)

    events.append((time, "恢复满值", current_neili))

    # 绘制图表
    if show_plot:
        fig, ax = plt.subplots(figsize=(14, 7))

        # 设置背景色
        fig.patch.set_facecolor('white')
        ax.set_facecolor('#f8f9fa')

        # 绘制内力曲线
        ax.plot(time_points, neili_points, linewidth=3, color='#e74c3c',
                label='内力值', alpha=0.9, zorder=2)

        # 添加渐变填充
        ax.fill_between(time_points, 0, neili_points, alpha=0.15, color='#e74c3c', zorder=1)

        # 标记吃馒头事件
        mantou_times = []
        mantou_neili = []
        mantou_labels = []
        for event_time, event_desc, neili in events:
            if "吃馒头" in event_desc:
                mantou_times.append(event_time)
                mantou_neili.append(neili)
                mantou_labels.append(event_desc)

        if mantou_times:
            ax.scatter(mantou_times, mantou_neili, color='#f39c12', s=200, zorder=5,
                      marker='o', edgecolors='#d35400', linewidths=2, label='吃馒头时机')

            # 添加文字标注
            for i, (t, n, label) in enumerate(zip(mantou_times, mantou_neili, mantou_labels)):
                ax.annotate(label, xy=(t, n),
                           xytext=(10, 20), textcoords='offset points',
                           fontsize=10, color='#d35400', fontweight='bold',
                           bbox=dict(boxstyle='round,pad=0.5', fc='#fff3cd', ec='#f39c12', alpha=0.9),
                           arrowprops=dict(arrowstyle='->', color='#d35400', lw=1.5))

        # 设置坐标轴
        ax.set_xlabel('时间（小时）', fontsize=13, fontweight='bold')
        ax.set_ylabel('内力值', fontsize=13, fontweight='bold')
        ax.set_title(f'🥋 大侠内力恢复过程\n共吃{mantou_count}个馒头，耗时{time:.2f}小时',
                    fontsize=16, fontweight='bold', pad=20, color='#2c3e50')

        # 美化网格
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8, color='#95a5a6')
        ax.set_xlim(-0.2, max(10, time * 1.05))
        ax.set_ylim(-2, total_neili * 1.05)

        # 添加图例
        ax.legend(loc='lower right', fontsize=11, framealpha=0.95,
                 edgecolor='#7f8c8d', fancybox=True, shadow=True)

        # 美化边框
        for spine in ax.spines.values():
            spine.set_edgecolor('#7f8c8d')
            spine.set_linewidth(1.5)

        plt.tight_layout()
        plt.savefig('neili_recovery.png', dpi=200, bbox_inches='tight', facecolor='white')
        print(f"✅ 图表已保存为: neili_recovery.png")
        plt.show()

    return time, mantou_count, time_points, neili_points, events


def analyze_strategy():
    """
    分析不同策略下的恢复时间
    """
    max_neili = 100

    print("=" * 50)
    print("大侠内力恢复分析")
    print("=" * 50)

    # 策略1：只打坐
    print("\n【策略1：只打坐】")
    # 每小时恢复10%，从1恢复到100
    recovery_per_hour = max_neili * 0.1
    time_meditate_only = (max_neili - 1) / recovery_per_hour
    print(f"恢复时间: {time_meditate_only:.2f} 小时")
    print(f"吃馒头数: 0 个")

    # 策略2：最优策略（打坐+馒头）
    print("\n【策略2：打坐+馒头（最优策略）】")
    time_optimal, mantou_count, _, _, events = simulate_neili_recovery(max_neili, show_plot=False)
    print(f"恢复时间: {time_optimal:.2f} 小时")
    print(f"吃馒头数: {mantou_count} 个")
    print(f"\n事件记录:")
    for t, desc, neili in events:
        print(f"  {t:5.2f}h - {desc:12s} (内力: {neili:6.2f})")

    # 策略3：边打坐边吃馒头（从开始就吃）
    print("\n【策略3：一开始就边打坐边吃馒头】")
    current_neili = 1.0
    time = 0.0
    mantou_count = 0
    mantou_digesting = 0

    while current_neili < max_neili - 0.1:
        # 打坐恢复
        current_neili += recovery_per_hour * 0.01
        time += 0.01

        # 消化
        if mantou_digesting > 0:
            mantou_digesting -= 0.01
            if mantou_digesting < 0:
                mantou_digesting = 0

        # 尽可能多吃馒头
        if mantou_digesting <= 0 and current_neili < max_neili - 1:
            empty_neili = max_neili - current_neili
            current_neili += empty_neili * 0.1
            mantou_count += 1
            mantou_digesting = 2.0

        current_neili = min(current_neili, max_neili)

    print(f"恢复时间: {time:.2f} 小时")
    print(f"吃馒头数: {mantou_count} 个")

    print("\n" + "=" * 50)
    print("策略对比:")
    print("=" * 50)
    print(f"只打坐:        {time_meditate_only:6.2f}h, 0 个馒头")
    print(f"最优策略:      {time_optimal:6.2f}h, {mantou_count} 个馒头  ⭐")
    print(f"边打边吃:      {time:6.2f}h, {mantou_count} 个馒头")
    print(f"\n最优策略比只打坐快 {time_meditate_only - time_optimal:.2f} 小时 ({(1 - time_optimal/time_meditate_only)*100:.1f}%)")
    print("=" * 50)


if __name__ == "__main__":
    # 运行分析
    analyze_strategy()

    # 绘制详细图表
    print("\n正在生成详细恢复曲线...")
    time, mantou_count, _, _, _ = simulate_neili_recovery(show_plot=True)

    print("\n" + "=" * 50)
    print("最终答案")
    print("=" * 50)
    print(f"内力恢复到满值需要: {time:.2f} 小时")
    print(f"恢复过程中总共吃了: {mantou_count} 个馒头")
    print("=" * 50)
