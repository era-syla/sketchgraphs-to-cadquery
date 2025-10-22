import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.185, -0.2).lineTo(0.185, -0.2).threePointArc((0.19561, -0.19561), (0.2, -0.185)).lineTo(0.2, 0.185).threePointArc((0.19561, 0.19561), (0.185, 0.2)).lineTo(-0.185, 0.2).threePointArc((-0.19561, 0.19561), (-0.2, 0.185)).lineTo(-0.2, -0.185).threePointArc((-0.19561, -0.19561), (-0.185, -0.2)).close()
solid=wp_sketch0.add(loop0).extrude(0.3499597566266277)
