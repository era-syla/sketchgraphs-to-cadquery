import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00762, 0.0).lineTo(-0.06742, 0.0).lineTo(-0.06742, 0.0762).lineTo(-0.00762, 0.0762).lineTo(-0.00762, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.2107298480736343)
