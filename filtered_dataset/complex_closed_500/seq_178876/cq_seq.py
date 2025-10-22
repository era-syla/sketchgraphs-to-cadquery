import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02, 0.064).lineTo(0.01, 0.064).lineTo(0.01, 0.069).lineTo(0.03, 0.069).lineTo(0.03, 0.064).lineTo(0.02, 0.064).close()
solid=wp_sketch0.add(loop0).extrude(0.042346996709728364)
