import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00853, 0.0144).lineTo(0.00743, 0.0144).lineTo(0.00743, 0.00865).lineTo(0.00853, 0.00865).lineTo(0.00853, 0.0144).close()
solid=wp_sketch0.add(loop0).extrude(0.015366017509291716)
