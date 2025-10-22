import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.005, -0.008).threePointArc((-0.003, -0.01), (-0.005, -0.012)).lineTo(0.005, -0.012).threePointArc((0.003, -0.01), (0.005, -0.008)).lineTo(-0.005, -0.008).close()
solid=wp_sketch0.add(loop0).extrude(-0.0018327438968368615)
