import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01096, 0.02).lineTo(0.00745, 0.02).lineTo(0.00745, 0.002).lineTo(-0.01096, 0.002).lineTo(-0.01096, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.05424518520736232)
