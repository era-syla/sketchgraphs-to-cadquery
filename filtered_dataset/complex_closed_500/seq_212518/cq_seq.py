import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.54, -0.021).threePointArc((0.534, -0.015), (0.54, -0.009)).lineTo(0.495, -0.009).threePointArc((0.501, -0.015), (0.495, -0.021)).lineTo(0.54, -0.021).close()
solid=wp_sketch0.add(loop0).extrude(-0.010715782414216777)
