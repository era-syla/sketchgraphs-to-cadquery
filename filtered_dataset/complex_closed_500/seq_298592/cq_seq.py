import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.24983, -0.95512).lineTo(-0.23983, -0.95512).lineTo(-0.23983, -1.27512).lineTo(-0.24983, -1.27512).lineTo(-0.24983, -0.95512).close()
solid=wp_sketch0.add(loop0).extrude(-0.6965117713576058)
