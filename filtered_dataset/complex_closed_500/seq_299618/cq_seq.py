import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0755, -0.049).lineTo(-0.0755, -0.049).lineTo(-0.0755, 0.049).lineTo(0.0755, 0.049).lineTo(0.0755, -0.049).close()
solid=wp_sketch0.add(loop0).extrude(-0.2457692183583693)
