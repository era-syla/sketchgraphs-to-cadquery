import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.80522, 0.0508).threePointArc((-0.40261, 0.0), (-0.0, 0.0508)).lineTo(0.0, 0.1016).lineTo(-0.80522, 0.1016).lineTo(-0.80522, 0.0508).close()
solid=wp_sketch0.add(loop0).extrude(-0.40853172079012584)
