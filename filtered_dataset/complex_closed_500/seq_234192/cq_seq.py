import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0127, 0.00317).lineTo(0.0, 0.00317).lineTo(0.0, -0.04445).lineTo(-0.0127, -0.04445).lineTo(-0.0127, 0.00317).close()
solid=wp_sketch0.add(loop0).extrude(-0.1372638963895946)
