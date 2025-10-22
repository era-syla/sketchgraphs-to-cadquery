import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.20587, 0.075).lineTo(0.03413, 0.075).lineTo(0.03413, 0.014).threePointArc((0.03149, 0.00764), (0.02513, 0.005)).lineTo(-0.19687, 0.005).threePointArc((-0.20324, 0.00764), (-0.20587, 0.014)).lineTo(-0.20587, 0.075).close()
solid=wp_sketch0.add(loop0).extrude(-0.5058802197342462)
