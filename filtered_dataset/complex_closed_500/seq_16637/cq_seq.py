import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.90514, 0.0).lineTo(-0.90514, -0.045).lineTo(-0.095, -0.045).lineTo(-0.095, 0.0).lineTo(-0.90514, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-1.6969016636192373)
