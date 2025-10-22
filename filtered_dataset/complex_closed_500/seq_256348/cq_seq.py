import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.025, 0.003).lineTo(0.04, 0.003).lineTo(0.0325, 0.01599).lineTo(0.025, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.042937684200700224)
