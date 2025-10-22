import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.002, -0.003).lineTo(-0.002, -0.003).lineTo(-0.002, 0.003).lineTo(0.002, 0.003).lineTo(0.002, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.012993796669752661)
