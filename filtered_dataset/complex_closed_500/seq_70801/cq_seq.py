import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.002, 0.0).lineTo(-0.0264, 0.0).threePointArc((-0.02781, 0.00059), (-0.0284, 0.002)).lineTo(-0.0284, 0.0433).threePointArc((-0.02781, 0.04471), (-0.0264, 0.0453)).lineTo(-0.002, 0.0453).threePointArc((-0.00059, 0.04471), (-0.0, 0.0433)).lineTo(0.0, 0.002).threePointArc((-0.00059, 0.00059), (-0.002, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.025071007475329102)
