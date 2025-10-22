import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.29648, -0.05962).lineTo(0.31528, -0.05962).lineTo(0.31528, 0.05885).lineTo(-0.29648, 0.05885).lineTo(-0.29648, -0.05962).close()
solid=wp_sketch0.add(loop0).extrude(-0.8358747636819089)
