import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03769, 0.0).lineTo(-0.07169, 0.0).lineTo(-0.03769, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.018442694123794828)
