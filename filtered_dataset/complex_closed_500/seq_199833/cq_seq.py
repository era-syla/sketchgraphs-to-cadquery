import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01209, 0.00732).lineTo(-0.01209, 0.00732).lineTo(-0.01209, -0.00732).lineTo(0.01209, -0.00732).lineTo(0.01209, 0.00732).close()
solid=wp_sketch0.add(loop0).extrude(-0.039903018038259935)
