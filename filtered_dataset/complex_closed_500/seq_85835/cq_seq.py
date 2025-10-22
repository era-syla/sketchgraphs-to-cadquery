import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0127).lineTo(0.0, 0.0).lineTo(0.00429, -0.0).threePointArc((0.00319, 0.0067), (0.0, 0.0127)).close()
solid=wp_sketch0.add(loop0).extrude(-0.02774036038561624)
