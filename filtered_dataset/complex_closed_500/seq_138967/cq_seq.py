import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.032, 0.0283).lineTo(0.015, 0.0283).lineTo(0.015, 0.0248).lineTo(0.032, 0.0248).lineTo(0.032, 0.0283).close()
solid=wp_sketch0.add(loop0).extrude(0.012067302442255944)
