import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.2032, 0.0).lineTo(0.2032, -0.1016).lineTo(0.0, -0.1016).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.5111734568991898)
