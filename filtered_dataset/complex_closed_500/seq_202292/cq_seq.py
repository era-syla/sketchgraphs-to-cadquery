import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0045, 0.01328).lineTo(-0.0045, 0.015).lineTo(-0.0063, 0.015).threePointArc((-0.00557, 0.01396), (-0.0045, 0.01328)).close()
solid=wp_sketch0.add(loop0).extrude(0.00364508349922414)
