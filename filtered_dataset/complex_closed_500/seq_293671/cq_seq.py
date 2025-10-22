import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.9, 0.45).lineTo(0.9, 0.45).lineTo(0.9, -0.45).lineTo(-0.9, -0.45).lineTo(-0.9, 0.45).close()
solid=wp_sketch0.add(loop0).extrude(-2.5565862853881907)
