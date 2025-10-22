import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.017, 0.003).lineTo(-0.0155, 0.003).lineTo(-0.0155, 0.0018).lineTo(-0.017, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.003379304251181678)
