import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.03744).lineTo(0.00896, 0.0287).lineTo(-0.00209, 0.0287).lineTo(-0.0, 0.03744).close()
solid=wp_sketch0.add(loop0).extrude(-0.013435328654584307)
