import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.005, 0.018).lineTo(0.12, 0.018).lineTo(0.12, -0.003).lineTo(-0.005, -0.003).lineTo(-0.005, 0.018).close()
solid=wp_sketch0.add(loop0).extrude(-0.2229602703873589)
