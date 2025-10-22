import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, -0.06661).lineTo(-0.00544, -0.06661).lineTo(-0.00544, 0.0).threePointArc((-0.00272, 0.03452), (0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06502821327312935)
