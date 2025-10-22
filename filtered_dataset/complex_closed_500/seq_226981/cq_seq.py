import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0866, 0.0).lineTo(-0.0656, 0.0).lineTo(-0.0656, 0.018).lineTo(-0.0866, 0.018).lineTo(-0.0866, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.04312254945673276)
