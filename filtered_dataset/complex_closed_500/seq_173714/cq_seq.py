import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00189, 0.0).lineTo(0.0, -0.00327).lineTo(-0.00189, 0.0).threePointArc((-0.0, 0.00327), (0.00189, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.005249698074218706)
