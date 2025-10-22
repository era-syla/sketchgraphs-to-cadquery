import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00597, -0.0762).lineTo(-0.04483, -0.0762).lineTo(-0.04483, 0.0).lineTo(0.00597, 0.0).lineTo(0.00597, -0.0762).close()
solid=wp_sketch0.add(loop0).extrude(-0.04271473943724592)
