import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.17, -0.27456).lineTo(-2.17, 0.0).lineTo(-2.33679, -0.00207).lineTo(-2.17, -0.27456).close()
solid=wp_sketch0.add(loop0).extrude(-0.3250196643725196)
