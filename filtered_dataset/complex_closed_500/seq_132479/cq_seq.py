import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.05).lineTo(0.02, 0.05).lineTo(0.02, -0.05).lineTo(-0.02, -0.05).lineTo(-0.02, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(0.26801434068702784)
