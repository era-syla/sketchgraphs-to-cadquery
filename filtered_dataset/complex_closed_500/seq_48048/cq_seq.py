import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03653, 0.01444).threePointArc((0.03624, 0.01514), (0.03553, 0.01544)).lineTo(-0.05047, 0.01544).threePointArc((-0.05118, 0.01514), (-0.05147, 0.01444)).lineTo(-0.05147, -0.03156).threePointArc((-0.05118, -0.03227), (-0.05047, -0.03256)).lineTo(0.03553, -0.03256).threePointArc((0.03624, -0.03227), (0.03653, -0.03156)).lineTo(0.03653, 0.01444).close()
solid=wp_sketch0.add(loop0).extrude(-0.10538087645404963)
