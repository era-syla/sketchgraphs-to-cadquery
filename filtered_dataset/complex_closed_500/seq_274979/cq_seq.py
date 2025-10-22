import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0075, -0.02402).lineTo(-0.0075, -0.02402).lineTo(-0.0075, -0.02859).lineTo(0.0075, -0.02859).lineTo(0.0075, -0.02402).close()
solid=wp_sketch0.add(loop0).extrude(0.04473356020677334)
