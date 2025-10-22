import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.015, 0.0365).lineTo(-0.015, 0.0325).lineTo(-0.015, -0.0325).lineTo(-0.015, -0.0365).lineTo(-0.065, -0.0365).lineTo(-0.065, 0.0365).lineTo(-0.015, 0.0365).close()
solid=wp_sketch0.add(loop0).extrude(-0.04422182496444977)
