import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.088, 0.0).lineTo(0.088, 0.016).lineTo(0.085, 0.016).lineTo(0.085, 0.02).lineTo(0.068, 0.02).lineTo(0.068, 0.031).lineTo(0.062, 0.031).threePointArc((0.056, 0.025), (0.05, 0.031)).lineTo(0.0, 0.031).lineTo(0.0, 0.0).lineTo(0.088, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.1862371306186565)
