import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02857, 0.03493).lineTo(0.02858, 0.03493).threePointArc((0.03307, 0.03307), (0.03493, 0.02858)).lineTo(0.03492, -0.02857).threePointArc((0.03307, -0.03307), (0.02857, -0.03493)).lineTo(-0.02857, -0.03493).threePointArc((-0.03307, -0.03307), (-0.03493, -0.02857)).lineTo(-0.03492, 0.02858).threePointArc((-0.03307, 0.03307), (-0.02857, 0.03493)).close()
solid=wp_sketch0.add(loop0).extrude(-0.14588817263375808)
