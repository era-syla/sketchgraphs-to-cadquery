import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.012).threePointArc((0.00447, -0.01094), (0.008, -0.008)).lineTo(0.0, -0.008).lineTo(0.0, -0.012).close()
solid=wp_sketch0.add(loop0).extrude(0.009512708093232985)
