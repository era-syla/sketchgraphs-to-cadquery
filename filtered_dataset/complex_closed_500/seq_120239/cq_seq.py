import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.024, 0.015).lineTo(-0.024, 0.013).lineTo(-0.016, 0.013).lineTo(-0.016, 0.003).lineTo(-0.024, 0.003).lineTo(-0.024, 0.001).lineTo(-0.001, 0.001).lineTo(-0.001, 0.00262).lineTo(-0.009, 0.00262).lineTo(-0.009, 0.013).lineTo(-0.001, 0.013).lineTo(-0.001, 0.015).lineTo(-0.024, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.0250290639789176)
